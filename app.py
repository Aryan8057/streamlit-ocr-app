import streamlit as st
import pytesseract
from PIL import Image

# Set the Tesseract command (adjust if necessary based on your setup)
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"  # Adjust this path for your Streamlit environment

# Define a function for OCR processing
def ocr_image(image, languages="hin+eng"):
    # Perform OCR using Tesseract
    extracted_text = pytesseract.image_to_string(image, lang=languages)
    return extracted_text

# Keyword search function
def search_keywords(text, keyword):
    if keyword.lower() in text.lower():
        return f'Keyword "{keyword}" found!'
    return f'Keyword "{keyword}" not found.'

# Streamlit UI
st.title("Hindi and English OCR with Keyword Search")

# Upload image
uploaded_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    # Open and display the image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Perform OCR on the image
    extracted_text = ocr_image(image)
    st.subheader("Extracted Text")
    st.text_area("Text Output", value=extracted_text, height=200)

    # Keyword input
    keyword = st.text_input("Enter Keyword to Search")

    if st.button("Search"):
        search_result = search_keywords(extracted_text, keyword)
        st.subheader("Search Result")
        st.write(search_result)

# Run the Streamlit app
if __name__ == "__main__":
    st.write("App is running...")
