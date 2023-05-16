import streamlit as st
import os
import matplotlib.pyplot as plt

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(FILE_DIR, "Image", "laptop-bg.jpg")

st.title('Flipkart Laptop Data - Business Insights on Product Pricing')

st.write(''.join(['This App allows you to estimate the price of laptops']))
#st.markdown('Ilon Musk is welcome to check it out \N{winking face}')
img = plt.imread(IMAGE_PATH)
st.image(img, width=500)
st.caption('Innomatics Research Labs Internship - February 2023')