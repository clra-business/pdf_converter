import pymupdf4llm
import re
from pathlib import Path
from typing import List, Optional

try:
    from .models import ParsedDocument, DocumentSections
except ImportError:
    # Handle running as main script
    from models import ParsedDocument, DocumentSections


class DocumentParser:
    """SOC 2 document parser with section splitting capabilities."""
    
    def __init__(self):
        self.section_4_patterns = [
            # AWS format (verified from actual document)
            r"Section IV[:\-\s–—]*Description of Criteria.*Controls.*Tests.*Results",
            # Perplexity format (verified - found at line 1563)
            r"SECTION 4[:\-\s]*TRUST SERVICES",
            r"SECTION 4[:\-\s]*.*TRUST SERVICES",
            # Generic patterns for other SOC 2 formats
            r"Section (?:IV|4)[:\-\s]*.*Controls.*Tests",
            r"SECTION (?:IV|4)[:\-\s]*.*Controls.*Tests",
            # Simple fallback patterns
            r"SECTION 4",
            r"Section IV",
            r"Section 4"
        ]
    
    def parse_pdf(self, file_path: Path) -> ParsedDocument:
        """Main parsing method that converts PDF and splits sections."""
        content = self._convert_pdf_to_markdown(file_path)
        sections = self._split_document_sections(content)
        
        return ParsedDocument(
            content=content,
            file_name=file_path.stem,
            sections=sections,
            total_lines=len(content.splitlines()),
            file_path=file_path
        )
    
    def _convert_pdf_to_markdown(self, file_path: Path) -> str:
        """Convert PDF to markdown using pymupdf4llm."""
        try:
            md_text = pymupdf4llm.to_markdown(str(file_path))
            return md_text
        except Exception as e:
            raise ValueError(f"Failed to convert PDF {file_path}: {str(e)}")
    
    def _split_document_sections(self, content: str) -> DocumentSections:
        """Split document at Section IV by skipping early content and finding first occurrence."""
        total_chars = len(content)
        
        # Skip the first portion of the document to avoid TOC entries
        # Use a more conservative approach: skip first 500 lines or 20% of document, whichever is smaller
        content_lines = content.split('\n')
        skip_by_lines = len('\n'.join(content_lines[:500])) if len(content_lines) > 500 else 0
        skip_by_percentage = total_chars // 5  # Skip first 20% instead of 50%
        
        skip_point = min(skip_by_lines, skip_by_percentage)  # Use smaller skip to be safer
        
        # Search only in the latter portion of the document
        search_content = content[skip_point:]
        
        for pattern in self.section_4_patterns:
            match = re.search(pattern, search_content, re.IGNORECASE | re.DOTALL)
            
            if match:
                # Calculate the actual position in the full document
                actual_split_point = skip_point + match.start()
                
                return DocumentSections(
                    sections_1_3=content[:actual_split_point].strip(),
                    section_4_plus=content[actual_split_point:].strip(),
                    split_successful=True,
                    split_pattern_used=pattern
                )
        
        # No split found - return whole document as sections_1_3
        return DocumentSections(
            sections_1_3=content,
            section_4_plus="",
            split_successful=False,
            split_pattern_used=None
        )
    
    def validate_section_split(self, sections: DocumentSections) -> bool:
        """Validate that section 4+ contains actual control testing content."""
        if not sections.split_successful:
            return False
        
        # Look for indicators of actual control testing content
        control_indicators = [
            r"CC\d+\.\d+",  # Common Criteria references (CC1.1, CC6.4, etc.)
            r"Tests Performed",
            r"Results of Tests", 
            r"No deviations noted",
            r"No exceptions noted",  # Perplexity format
            r"Exception",
            r"Control\s+(?:Description|Criterion|Activities|Number)",
            r"Detailed Tests of Controls",  # Perplexity table headers
            r"Test Results"  # Perplexity table headers
        ]
        
        section_4_content = sections.section_4_plus.lower()
        matches_found = sum(1 for pattern in control_indicators 
                          if re.search(pattern, section_4_content, re.IGNORECASE))
        
        # Require at least 3 control indicators to consider split valid
        return matches_found >= 3


# Backward compatibility functions
def convert_pdf(file: Path) -> ParsedDocument:
    """Backward compatible function that returns structured data."""
    parser = DocumentParser()
    parsed_doc = parser.parse_pdf(file)
    
    # Maintain backward compatibility by also writing to output directory
    file_name = file.name.split('.')[0].replace('+', '_')
    output_file = Path(__file__).parent.parent / "output" / f"{file_name}.md"
    output_file.write_bytes(parsed_doc.content.encode())
    
    print(f"{file_name}.pdf is being processed and converted to a markdown file. This may take a while.")
    
    return parsed_doc


def convert_all_pdfs(soc_dir: Path) -> List[ParsedDocument]:
    """Process all PDFs and return structured results."""
    parser = DocumentParser()
    results = []
    
    for file in soc_dir.iterdir():
        if file.suffix == '.pdf':
            try:
                parsed_doc = parser.parse_pdf(file)
                
                # Create directory structure for testing
                file_name = file.name.split('.')[0].replace('+', '_')
                output_base = Path(__file__).parent.parent / "output"
                
                # Write full document for backward compatibility
                output_file = output_base / f"{file_name}.md"
                output_file.write_bytes(parsed_doc.content.encode())
                
                # Create directory for split sections (testing only)
                doc_dir = output_base / file_name
                doc_dir.mkdir(exist_ok=True)
                
                # Save sections separately for analysis
                sections_1_3_file = doc_dir / "sections_1_3.md"
                section_4_plus_file = doc_dir / "section_4_plus.md"
                metadata_file = doc_dir / "parsing_metadata.txt"
                
                sections_1_3_file.write_text(parsed_doc.sections.sections_1_3, encoding='utf-8')
                section_4_plus_file.write_text(parsed_doc.sections.section_4_plus, encoding='utf-8')
                
                # Save parsing metadata
                metadata = f"""Document: {file.name}
File Name: {parsed_doc.file_name}
Total Lines: {parsed_doc.total_lines}
Split Successful: {parsed_doc.sections.split_successful}
Pattern Used: {parsed_doc.sections.split_pattern_used}
Section 1-3 Length: {len(parsed_doc.sections.sections_1_3)} characters
Section 4+ Length: {len(parsed_doc.sections.section_4_plus)} characters
Validation: {'✓' if parser.validate_section_split(parsed_doc.sections) else '✗'}
"""
                metadata_file.write_text(metadata, encoding='utf-8')
                
                results.append(parsed_doc)
                print(f"✓ Processed {file.name}")
                print(f"  Split successful: {parsed_doc.sections.split_successful}")
                print(f"  Created directory: {doc_dir}")
                if parsed_doc.sections.split_successful:
                    validation = parser.validate_section_split(parsed_doc.sections)
                    print(f"  Section validation: {'✓' if validation else '✗'}")
            except Exception as e:
                print(f"✗ Failed to process {file.name}: {str(e)}")
        else:
            print(f"{file} is not a pdf.")
    
    return results


if __name__ == "__main__":
    soc_dir = Path(__file__).parent.parent / "docs" / "soc-reports"
    results = convert_all_pdfs(soc_dir)
    print(f"\nProcessed {len(results)} documents successfully.")