import streamlit as st
import pandas as pd

# Define function to load data from selected files
@st.cache(allow_output_mutation=True)
def load_data(files):
    data = []
    for file in files:
        df = pd.read_excel(file, engine='openpyxl')
        data.append(df)
    return data

# Define pages
def page_1():
    st.write("<h1 style='text-align: center'>Select Files</h1>", unsafe_allow_html=True)
    files = st.file_uploader('Select up to 6 Excel files', type='xlsx', accept_multiple_files=True)
    if files:
        data = load_data(files)
        st.success('Data loaded successfully!')
        st.write("<h2 style='text-align: center'>Navigation</h2>", unsafe_allow_html=True)
        if st.button('Page 2', key='2', help='Go to Page 2', width=100, height=50, bg_color='#4CAF50', text_color='#FFFFFF'):
            page_2()
        if st.button('Page 3', key='3', help='Go to Page 3', width=100, height=50, bg_color='#2196F3', text_color='#FFFFFF'):
            page_3()
        if st.button('Page 4', key='4', help='Go to Page 4', width=100, height=50, bg_color='#f44336', text_color='#FFFFFF'):
            page_4()
        if st.button('Page 5', key='5', help='Go to Page 5', width=100, height=50, bg_color='#9C27B0', text_color='#FFFFFF'):
            page_5()
        if st.button('Page 6', key='6', help='Go to Page 6', width=100, height=50, bg_color='#FF9800', text_color='#FFFFFF'):
            page_6()

def page_2():
    st.write("<h1 style='text-align: center'>Page 2</h1>", unsafe_allow_html=True)

def page_3():
    st.write("<h1 style='text-align: center'>Page 3</h1>", unsafe_allow_html=True)

def page_4():
    st.write("<h1 style='text-align: center'>Page 4</h1>", unsafe_allow_html=True)

def page_5():
    st.write("<h1 style='text-align: center'>Page 5</h1>", unsafe_allow_html=True)

def page_6():
    st.write("<h1 style='text-align: center'>Page 6</h1>", unsafe_allow_html=True)

# Define app
def app():
    st.sidebar.write("<h1 style='text-align: center; color: #FFFFFF; margin-top: 50px; margin-bottom: 50px;'>Navigation</h1>", unsafe_allow_html=True)
    if st.sidebar.button('Page 1', key='1', help='Go to Page 1', width=150, height=75, bg_color='#3F51B5', text_color='#FFFFFF'):
        page_1()
    if st.sidebar.button('Page 2', key='2', help='Go to Page 2', width=150, height=75, bg_color='#4CAF50', text_color='#FFFFFF'):
        page_2()
    if st.sidebar.button('Page 3', key='3', help='Go to Page 3', width=150, height=75, bg_color='#2196F3',
