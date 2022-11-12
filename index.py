# Import modules
import streamlit as st

# Import other dependencies
# from views import Pages


# List of Pages
page_list = []

# Sidebar with project title
st.sidebar.title(':scroll: Team Hortons')
st.sidebar.radio('Explore: ', page_list)


# Showing which pages are shown