import sys
from pdfminer.high_level import extract_text
from bs4 import BeautifulSoup
from os import path


def pdf_to_html(pdf_file):
	# Extract text from the PDF
	text = extract_text(pdf_file)

	# Create a simple HTML document
	soup = BeautifulSoup('<html><body></body></html>', 'html.parser')
	body = soup.body

	# Add extracted text to the body
	for line in text.splitlines():
		p = soup.new_tag('p')
		p.string = line
		body.append(p)

	return str(soup)

def write_html_to_file(pdf_file, html):
	file_name = path.basename(pdf_file)
	file_path = path.join("out", file_name.replace(".pdf", ".html"))

	with open(file_path, "w") as file:
		file.write(html)
		file.close()

	print(f"Text written to file: {file_path}")
	return file_path


if __name__ == "__main__":
	# Process arguments from command line
	if len(sys.argv) < 2:
		print("Usage: python pdf_to_markdown.py <file_path>")
		sys.exit(1)
	pdf_file = sys.argv[1]
	html = pdf_to_html(pdf_file)
	write_html_to_file(pdf_file, html)
