import streamlit as st
import os
from utils import pdf_to_word
st.set_page_config("pdf to word converter",layout="wide")
# uploaded_file=f"./pdf_to_word/uploaded_file"
uploaded_file="C:/Users/ASUS/Documents/projects/pdf_to_word/pdf_to_word/uploaded_file"
# converted_file=f"./pdf_to_word/converted_files"
converted_file="C:/Users/ASUS/Documents/projects/pdf_to_word/pdf_to_word/converted_files/convertedfile.docx"
file=st.file_uploader("Upload your file here",type=".pdf")
upload=st.button("Upload")
if file and upload:
    st.spinner()
    if not os.path.exists(uploaded_file):
        os.mkdir(uploaded_file)

    file_path= os.path.join(uploaded_file, file.name)
    with open(file_path, 'wb') as f:
        f.write(file.getvalue())
    
    pdf_to_word(file_path, converted_file)
    st.success("file converted successfully")
    # st.download_button(file_path=conver)

else:
    st.warning('please upload dile to continue ')
