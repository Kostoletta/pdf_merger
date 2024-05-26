# PDF Merger

This Python script merges two PDF files: one with even pages scanned from a document and the other with odd pages. Useful when you have used a single-sided scanner to scan double-sided documents in two passes.

## Prerequisites

- Python 3.x
- `PyPDF2` library

## Usage

1. Scanned PDF files need to be in the same folder as the script. You will be prompted to enter the names of the odd and even PDF files.


2. Run the script:

    ```bash
    python pdf_merger.py
    ```

3. The script will generate a merged PDF file named `merged.pdf` in the same directory.
