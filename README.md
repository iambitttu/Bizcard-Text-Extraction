# Biz Card Data Extraction

## Introduction
The Biz Card Data project focuses on extracting and processing data from business card images using the EasyOCR library. By leveraging optical character recognition (OCR) techniques, we can automatically extract text from business card images and convert it into structured data for further analysis or storage. This documentation outlines the steps involved in extracting business card data and demonstrates how to use the Streamlit framework to create a user-friendly interface for the data extraction process.

## Setup and Dependencies
To get started with the Biz Card Data project, follow these steps:

1. Install the EasyOCR library using pip: `pip install easyocr`.
2. Import the EasyOCR module and set the language to English using `reader = easyocr.Reader(['en'])`.
3. Import the PIL (Python Imaging Library) module for image handling: `from PIL import Image, ImageDraw`.
4. Open an image using PIL's `Image.open` function: `image = Image.open('business_card.jpg')`.
5. Use the `reader.readtext` function to extract text from the image: `result = reader.readtext(image)`.

## Data Extraction
To extract data from business card images, we will perform the following steps:

1. Create a function to read text from a business card image: `def extract_biz_card_data(image_path): ...`.
2. Inside the function, open the image using `Image.open` and pass it to `reader.readtext` to obtain the text results.
3. Process the extracted text to identify relevant information such as name, phone number, email address, etc.
4. Return the extracted data in a structured format, such as a dictionary or a list of key-value pairs.

## Data Conversion and Storage
To convert the extracted data into a DataFrame and store it for further analysis, follow these steps:

1. Install the Pandas library: `pip install pandas`.
2. Import the Pandas module: `import pandas as pd`.
3. Convert the extracted data into a DataFrame: `df = pd.DataFrame(extracted_data)`.
4. Perform any necessary data cleaning or manipulation on the DataFrame.
5. Store the DataFrame in a suitable format, such as a CSV file or a database, using Pandas' `to_csv` or `to_sql` functions.

## Streamlit Integration
To create a user-friendly interface for the Biz Card Data project, we will utilize the Streamlit framework. Follow these steps to integrate Streamlit:

1. Install Streamlit: `pip install streamlit`.
2. Import the Streamlit module: `import streamlit as st`.
3. Add a header to the Streamlit app: `st.header('Biz Card Data Extraction')`.
4. Create a file uploader using Streamlit's `file_uploader` function.
5. Inside the file uploader callback, open the uploaded image using PIL's `Image.open`.
6. Pass the image to the OCR function to extract the data.
7. Display the extracted data using Streamlit's `write` or `dataframe` functions.
8. Customize the Streamlit app layout and appearance as desired.

## Conclusion
The Biz Card Data project provides a convenient solution for extracting and processing data from business card images. By leveraging the EasyOCR library and Streamlit framework, we can automate the extraction process and create an intuitive user interface for users to upload and extract data from their business card images. This documentation serves as a guide to set up and utilize the Biz Card Data project effectively.
