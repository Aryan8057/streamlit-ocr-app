import pytesseract
from PIL import Image
import streamlit as st

# OCR function with error handling
def process_image(image):
    try:
        extracted_text = pytesseract.image_to_string(image, lang="hin+eng")
        if not extracted_text.strip():
            return "No text found in the image. Please try another image."
        return extracted_text
    except Exception as e:
        return f"Error during OCR: {str(e)}"

# Keyword search function
def search_keywords(text, keyword):
    try:
        if keyword.lower() in text.lower():
            return f'Keyword "{keyword}" found!'
        return f'Keyword "{keyword}" not found.'
    except Exception as e:
        return f"Error during search: {str(e)}"

# Streamlit app layout
st.title("Hindi and English OCR with Keyword Search")

# Upload an image
uploaded_image = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

# Input for keyword search
keyword = st.text_input("Enter Keyword to Search")

# If image is uploaded and keyword is entered
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    extracted_text = process_image(image)

    st.subheader("Extracted Text")
    st.text(extracted_text)

    if keyword:
        search_result = search_keywords(extracted_text, keyword)
        st.subheader("Search Result")
        st.text(search_result)
