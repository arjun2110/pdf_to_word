import PyPDF2
from docx import Document

def pdf_to_word(pdf_path, word_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Create a Word document
        word_document = Document()

        # Iterate through each page and extract text
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text = page.extract_text()

            # Add the extracted text to the Word document
            word_document.add_paragraph(text)

        print(word_document)
        # Save the Word document
        word_document.save(word_path)

# # Example usage
# pdf_file_path = 'input.pdf'
# word_file_path = 'output.docx'
# pdf_to_word(pdf_file_path, word_file_path)
