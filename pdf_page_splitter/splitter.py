import PyPDF2
import os

def extract_pages_to_pdfs(input_pdf, output_folder):
    # Open the input PDF file
    with open(input_pdf, 'rb') as input_pdf:
        pdf_reader = PyPDF2.PdfReader(input_pdf)
        num_pages = len(pdf_reader.pages)

        # Iterate through each page and save it as an individual PDF
        for page_num in range(num_pages):
            # Create a new PDF writer for each page
            pdf_writer = PyPDF2.PdfWriter()

            # Extract the page and add it to the writer
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

            # Define the output PDF file path
            output_pdf_path = os.path.join(output_folder, f"{page_num + 1}.pdf")

            # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)

            # Write the individual page to a new PDF file
            with open(output_pdf_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

            print(f"Saved page {page_num + 1} to {output_pdf_path}")

# Specify the file paths
input_pdf = './pdf_page_splitter/input.pdf'
output_folder = './pdf_page_splitter/output_pages'

extract_pages_to_pdfs(input_pdf, output_folder)