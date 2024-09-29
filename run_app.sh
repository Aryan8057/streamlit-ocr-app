#!/bin/bash

# Set the LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/mount/src/streamlit-ocr-app/tesseract_build/tesseract/leptonica/lib:$LD_LIBRARY_PATH

# Run the Streamlit app
streamlit run app.py 
