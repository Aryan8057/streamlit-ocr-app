# import pytesseract
# from PIL import Image
# import streamlit as st
# import os
# import subprocess

# # Function to install custom Tesseract (v5.4.0)
# def install_custom_tesseract():
#     if not os.path.exists("/usr/local/bin/tesseract"):  # Check if Tesseract is already installed
#         # Download the source code for the custom Tesseract version
#         subprocess.run(["git", "clone", "https://github.com/tesseract-ocr/tesseract.git"], check=True)
#         os.chdir("tesseract")
#         subprocess.run(["git", "checkout", "5.4.0"], check=True)  # Use your specific version tag

#         # Install Leptonica (Tesseract dependency)
#         subprocess.run(["git", "clone", "https://github.com/DanBloomberg/leptonica.git"], check=True)
#         os.chdir("leptonica")
#         subprocess.run(["./autogen.sh"], check=True)
#         subprocess.run(["./configure"], check=True)
#         subprocess.run(["make"], check=True)
#         subprocess.run(["sudo", "make", "install"], check=True)
#         os.chdir("../tesseract")

#         # Compile and install Tesseract
#         subprocess.run(["./autogen.sh"], check=True)
#         subprocess.run(["./configure"], check=True)
#         subprocess.run(["make"], check=True)
#         subprocess.run(["sudo", "make", "install"], check=True)
#         subprocess.run(["sudo", "ldconfig"], check=True)

#         # Check installation
#         subprocess.run(["tesseract", "--version"], check=True)

# # Install Tesseract if needed
# install_custom_tesseract()

# # Set path for Tesseract executable
# if os.name == 'nt':
#     pytesseract.pytesseract.tesseract_cmd = "C://Program Files//Tesseract-OCR//tesseract.exe"  # Windows-specific path
# else:
#     pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"  # Linux-specific path

# # OCR function with error handling
# def process_image(image):
#     try:
#         extracted_text = pytesseract.image_to_string(image, lang="hin+eng")
#         if not extracted_text.strip():
#             return "No text found in the image. Please try another image."
#         return extracted_text
#     except Exception as e:
#         return f"Error during OCR: {str(e)}"

# # Keyword search function
# def search_keywords(text, keyword):
#     try:
#         if keyword.lower() in text.lower():
#             return f'Keyword "{keyword}" found!'
#         return f'Keyword "{keyword}" not found.'
#     except Exception as e:
#         return f"Error during search: {str(e)}"

# # Streamlit app layout
# st.title("Hindi and English OCR with Keyword Search")

# # Upload an image
# uploaded_image = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

# # Input for keyword search
# keyword = st.text_input("Enter Keyword to Search")

# # If image is uploaded and keyword is entered
# if uploaded_image is not None:
#     image = Image.open(uploaded_image)
#     extracted_text = process_image(image)

#     st.subheader("Extracted Text")
#     st.text(extracted_text)

#     if keyword:
#         search_result = search_keywords(extracted_text, keyword)
#         st.subheader("Search Result")
#         st.text(search_result)



import pytesseract
from PIL import Image
import streamlit as st
import os
import subprocess

# Function to check if Tesseract is installed
def is_tesseract_installed():
    try:
        subprocess.run(["tesseract", "--version"], check=True)
        return True
    except Exception:
        return False

# Function to install custom Tesseract (v5.4.0) locally
def install_custom_tesseract():
    if is_tesseract_installed():
        st.success("Tesseract is already installed.")
        return

    try:
        st.info("Installing Tesseract...")
        # Create a local directory for installation
        os.makedirs("tesseract_build", exist_ok=True)
        os.chdir("tesseract_build")

        # Download the source code for Tesseract
        subprocess.run(["git", "clone", "https://github.com/tesseract-ocr/tesseract.git"], check=True)
        os.chdir("tesseract")
        subprocess.run(["git", "checkout", "5.4.0"], check=True)  # Use your specific version tag

        # Install Leptonica (Tesseract dependency)
        subprocess.run(["git", "clone", "https://github.com/DanBloomberg/leptonica.git"], check=True)
        os.chdir("leptonica")
        subprocess.run(["./autogen.sh"], check=True)
        subprocess.run(["./configure", "--prefix=" + os.path.abspath("../leptonica")], check=True)
        subprocess.run(["make"], check=True)
        subprocess.run(["make", "install"], check=True)  # Install to local directory
        os.chdir("../tesseract")

        # Compile and install Tesseract
        subprocess.run(["./autogen.sh"], check=True)
        subprocess.run(["./configure", "--prefix=" + os.path.abspath("../tesseract")], check=True)
        subprocess.run(["make"], check=True)
        subprocess.run(["make", "install"], check=True)  # Install to local directory

        # Check installation
        subprocess.run(["tesseract", "--version"], check=True)
        st.success("Tesseract installed successfully.")
    except Exception as e:
        st.error(f"Installation failed: {str(e)}")

# Install Tesseract if needed
install_custom_tesseract()

# Set path for Tesseract executable
if os.name == 'nt':
    pytesseract.pytesseract.tesseract_cmd = "C://Program Files//Tesseract-OCR//tesseract.exe"  # Windows-specific path
else:
    pytesseract.pytesseract.tesseract_cmd = os.path.abspath("../tesseract/bin/tesseract")  # Local Linux path

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
