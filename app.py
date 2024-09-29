import streamlit as st
import pytesseract
from PIL import Image

# Set the Tesseract command (default path for Linux)
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

# Function to process the uploaded image
def process_image(image):
    try:
        extracted_text = pytesseract.image_to_string(image, lang="hin+eng")
        if not extracted_text.strip():
            return "No text found in the image. Please try another image."
        return extracted_text
    except Exception as e:
        return f"Error during OCR: {str(e)}"

# Function for keyword search
def search_keywords(text, keyword):
    try:
        if keyword.lower() in text.lower():
            return f'Keyword "{keyword}" found!'
        return f'Keyword "{keyword}" not found.'
    except Exception as e:
        return f"Error during search: {str(e)}"

# Main function for OCR and keyword search
def ocr_app(image, keyword):
    extracted_text = process_image(image)
    search_result = search_keywords(extracted_text, keyword)
    return extracted_text, search_result

# Streamlit interface
st.title("Hindi and English OCR with Keyword Search")

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

# Input for keyword search
keyword = st.text_input("Enter Keyword to Search")

if uploaded_file is not None and keyword:
    # Open the image file
    image = Image.open(uploaded_file)
    
    # Call the OCR app function
    extracted_text, search_result = ocr_app(image, keyword)
    
    # Display the results
    st.text_area("Extracted Text", value=extracted_text, height=300)
    st.write(search_result)
