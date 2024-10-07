import sys
from PyPDF2 import PdfReader
from os import name as path
from pathlib import Path


def process_pdf(file_path):
    print(f"Processing file: {file_path}")
    reader = PdfReader(file_path)
    page_text = []

    for page in reader.pages:
        page_text.append(page.extract_text())

    page_text = '\n'.join(page_text)

    return page_text
    

def write_text_to_file(page_text):
    file_path = path.join(Path.home(), "Documents", "pdf_extracted.txt")
    with open(file_path, "w") as file:
        file.write(page_text)
        file.close()
    print(f"Text written to file: {file_path}")
    return file_path


if __name__ == "__main__":
	# Process arguments from command line
	if len(sys.argv) < 2:
		print("Usage: python pdf_to_markdown.py <file_path>")
		sys.exit(1)
	pdf_file = sys.argv[1]
	page_text = process_pdf(pdf_file)
	txt_file_path = write_text_to_file(page_text)



