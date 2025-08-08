from pydantic import BaseModel, Field
from typing import Optional
from pathlib import Path


class DocumentSections(BaseModel):
    """Represents the split sections of a SOC 2 document."""
    
    sections_1_3: str = Field(
        description="Management assertion, auditor opinion, system description"
    )
    section_4_plus: str = Field(
        description="Controls testing and results"
    )
    split_successful: bool = Field(
        description="Whether section splitting was successful"
    )
    split_pattern_used: Optional[str] = Field(
        default=None,
        description="Which regex pattern succeeded"
    )


class ParsedDocument(BaseModel):
    """Represents a fully parsed SOC 2 document with structured sections."""
    
    content: str = Field(
        description="Full document content"
    )
    file_name: str = Field(
        description="Original PDF filename without extension"
    )
    sections: DocumentSections = Field(
        description="Split document sections"
    )
    total_lines: int = Field(
        description="Total lines in document"
    )
    file_path: Path = Field(
        description="Original file path"
    )
    
    class Config:
        arbitrary_types_allowed = True