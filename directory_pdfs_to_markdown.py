import sys
import os
from pdf_to_markdown import pdf_to_html, html_to_markdown, write_markdown_to_file

def get_pdf_files(directory):
	# Recursively get all PDF files in the directory
	pdf_files = []
	for root, _, files in os.walk(directory):
		for file in files:
			if file.endswith(".pdf"):
				pdf_files.append(os.path.join(root, file))
	return pdf_files


if __name__ == "__main__":
	# Process arguments from command line
	if len(sys.argv) < 2:
		print("Usage: python pdf_to_markdown.py <file_path>")
		sys.exit(1)
	pdf_directory = sys.argv[1]
	pdf_files = get_pdf_files(pdf_directory)
	for pdf_file in pdf_files:
		html = pdf_to_html(pdf_file)
		md = html_to_markdown(html)
		if len(md) == 0 or not md:
			print("No text extracted from PDF")
		else:
			write_markdown_to_file(pdf_file, md)
