import PyPDF2
from docx import Document

def pdf_to_word(pdf_path, word_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Create a Word document
        word_document = Document()

        # Iterate through each page and extract text
        for page_number in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_number)
            text = page.extractText()

            # Add the extracted text to the Word document
            word_document.add_paragraph(text)s

        # Save the Word document
        word_document.save(word_path)
        

# # Example usage
# pdf_file_path = 'input.pdf'
# word_file_path = 'output.docx'
# pdf_to_word(pdf_file_path, word_file_path)
