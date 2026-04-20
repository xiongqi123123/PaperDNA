#!/usr/bin/env python3
"""
Lightweight utility to extract text from a local PDF file.
Usage: python parse_pdf.py /path/to/document.pdf
Requires: pypdf (pip install pypdf)
"""
import sys
import os

try:
    from pypdf import PdfReader
except ImportError:
    print("Error: 'pypdf' is not installed. Please run 'pip install pypdf'")
    sys.exit(1)

def extract_text_from_pdf(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File not found at {file_path}")
        sys.exit(1)
        
    try:
        reader = PdfReader(file_path)
        output = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                output.append(f"--- Page {i + 1} ---")
                output.append(text.strip())
                output.append("")
                
        return "\n".join(output)
    except Exception as e:
        print(f"Error parsing PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_pdf.py <path_to_pdf>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    result = extract_text_from_pdf(file_path)
    print(result)
