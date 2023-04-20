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
    st.title('Select Files')
    files = st.sidebar.file_uploader('Select up to 6 Excel files', type='xlsx', accept_multiple_files=True)
    if files:
        data = load_data(files)
        st.success('Data loaded successfully!')
        st.sidebar.success('Files selected successfully!')
        st.sidebar.markdown('---')
        st.sidebar.markdown('## Navigation')
        if st.sidebar.button('Page 2'):
            page_2()
        if st.sidebar.button('Page 3'):
            page_3()
        if st.sidebar.button('Page 4'):
            page_4()
        if st.sidebar.button('Page 5'):
            page_5()
        if st.sidebar.button('Page 6'):
            page_6()

def page_2():
    st.title('Page 2')

def page_3():
    st.title('Page 3')

def page_4():
    st.title('Page 4')

def page_5():
    st.title('Page 5')

def page_6():
    st.title('Page 6')

# Define app
def app():
    st.sidebar.markdown('## Pages')
    if st.sidebar.button('Page 1'):
        page_1()
    if st.sidebar.button('Page 2'):
        page_2()
    if st.sidebar.button('Page 3'):
        page_3()
    if st.sidebar.button('Page 4'):
        page_4()
    if st.sidebar.button('Page 5'):
        page_5()
    if st.sidebar.button('Page 6'):
        page_6()

# Run app
if __name__ == '__main__':
    app()
