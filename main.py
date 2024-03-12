import streamlit as st
import os
from utils import pdf_to_word
st.set_page_config("pdf to word converter",layout="wide")
uploaded_file="./uploaded_file"
converted_file="./converted_files"
file=st.file_uploader("Upload your file here",type=".pdf")
if file:
    if not os.path.exists(uploaded_file):
        os.mkdir(uploaded_file)

    file_path= os.path.join(uploaded_file, file.name)
    with open(file_path, 'wb') as f:
        f.write(file.getvalue())
    
    pd
