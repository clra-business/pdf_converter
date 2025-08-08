# SOC 2 Report Analyzer and PDF-to-Markdown Converter

## Overview

This project is a Python-based tool designed to automate the analysis of Third-Party Technical Risk Management (TPTRM) documents, specifically SOC 2 reports. It ingests PDF documents, converts them into a clean markdown format, and uses a multi-agent system to perform intelligent analysis of the content.

The core architecture is designed to be modular, separating the document processing logic from the AI-driven analysis workflows.

## Features

* **PDF to Markdown Conversion**: Utilizes `pymupdf4llm` to accurately convert PDF content into structured markdown.
* **Multi-Agent Analysis**: Implements a graph-based workflow using LangGraph to analyze different sections of a document in parallel for efficiency.
* **Modular Architecture**: Core components for parsing, agentic workflows, and analysis are separated for maintainability.
* **Type Safety**: Leverages Pydantic for robust data validation and clear data schemas.

## Getting Started

### Prerequisites

* Python 3.13 or later

### Installation

Clone the repository and install the required dependencies using your preferred package manager:

```bash
# Using uv
uv sync

# Or using pip
pip install -r requirements.txt
````

## Usage

### Convert a PDF to Markdown

Place your PDF files in the `docs/soc-reports/` directory. Then, run the parser:

Bash

```
python src/parser.py
```

Converted markdown files will be saved to the `output/` directory.

### Visualize the Architecture Design

To see a visualization of the multi-agent workflow, run:

Bash

```
python src/architecture/architect-design.py
```

## Architecture

The system is built around a few core components:

- `src/parser.py`: Handles the initial PDF ingestion and conversion to markdown.
    
- `src/agent.py`: Defines the LangGraph agent setup for analysis tasks. (Note: This component is currently incomplete).
    
- `src/architecture/architect-design.py`: Implements the multi-agent graph, which includes:
    
    - A **Router** to split the document for parallel processing.
        
    - Parallel **Analysis Nodes** for descriptive and control-based sections.
        
    - A **Synthesizer** to merge the results into a final report.
        

## Code Style and Quality

This project adheres to strict coding standards to ensure maintainability and readability. All contributions must follow:

- The **Google Python Style Guide**.
    
- PEP 8 (Style Guide for Python Code).
    
- PEP 257 (Docstring Conventions).
    

Reference guides are available in the `python_style_guides/` directory.