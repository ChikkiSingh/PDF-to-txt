import streamlit as st
import pdfplumber
from PIL import Image

def scan_pdf(file):
    with pdfplumber.open(file) as pdf:
        pages = pdf.pages
        text = ""
        for page in pages:
            text += page.extract_text()
        return text

def main():
    st.title("PDF Scanner App")
    st.sidebar.title("upload now ")

    # Upload PDF file
    uploaded_file = st.sidebar.file_uploader("Upload PDF", type="pdf")

    if uploaded_file is not None:
        st.sidebar.text("PDF uploaded successfully!")
        st.sidebar.text(f"Filename: {uploaded_file.name}")

        if st.sidebar.button("Scan PDF"):
            text = scan_pdf(uploaded_file)
            st.subheader("Scanned Text:")
            st.write(text)

            # Save scanned text to PDF file
            save_button = st.sidebar.button("Save as PDF")
            if save_button:
                save_as_pdf(text)

def save_as_pdf(text):
    file_name = "scanned_text.pdf"
    with open(file_name, "w") as f:
        f.write(text)
    st.sidebar.success(f"Scanned text saved as {file_name}")

if __name__ == "__main__":
    main()
