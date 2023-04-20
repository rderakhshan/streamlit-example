import streamlit as st
import pandas as pd
import plotly.express as px

# Define function to load data from selected files
@st.cache(allow_output_mutation=True)
def load_data(files):
    data = []
    for file in files:
        df = pd.read_excel(file, engine='openpyxl')
        data.append(df)
    return data

# Define function to create visualizations
def create_viz(data):
    fig = px.scatter(data, x='x', y='y', color='category')
    return fig

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
        page = st.sidebar.radio("Go to", ("Page 2", "Page 3", "Page 4", "Page 5", "Page 6"))
        if page == "Page 2":
            page_2(data)
        elif page == "Page 3":
            page_3(data)
        elif page == "Page 4":
            page_4(data)
        elif page == "Page 5":
            page_5(data)
        elif page == "Page 6":
            page_6(data)

def page_2(data):
    st.title('Page 2')
    fig = create_viz(data[0])
    st.plotly_chart(fig)

def page_3(data):
    st.title('Page 3')
    fig = create_viz(data[1])
    st.plotly_chart(fig)

def page_4(data):
    st.title('Page 4')
    fig = create_viz(data[2])
    st.plotly_chart(fig)

def page_5(data):
    st.title('Page 5')
    fig = create_viz(data[3])
    st.plotly_chart(fig)

def page_6(data):
    st.title('Page 6')
    fig = create_viz(data[4])
    st.plotly_chart(fig)

# Define app
def app():
    page = st.sidebar.radio("Go to", ("Page 1", "Page 2", "Page 3", "Page 4", "Page 5", "Page 6"))
    if page == "Page 1":
        page_1()
    elif page == "Page 2":
        page_2()
    elif page == "Page 3":
        page_3()
    elif page == "Page 4":
        page_4()
    elif page == "Page 5":
        page_5()
    elif page == "Page 6":
        page_6()

# Run app
if __name__ == '__main__':
    app()
