import streamlit as st

st.header('Bizcard data')
file = st.file_uploader("file uploader")
st.text('Here is the business card data:-')

from PIL import Image

image1 = Image.open('1.png')
image2 = Image.open('2.png')
image3 = Image.open('3.png')
image4 = Image.open('4.png')
image5 = Image.open('5.png')


st.image(image1, caption='BizcardX')
st.image(image2, caption='BizcardX')
st.image(image3, caption='BizcardX')
st.image(image4, caption='BizcardX')
st.image(image5, caption='BizcardX')