# Import modules
import streamlit as st

# Import other dependencies
from views import Pages


# List of Pages
page_list = [
    "Introduction"
]

# Sidebar with project title
st.sidebar.title(':scroll: Team Hortons')
page = st.sidebar.radio('Explore: ', page_list)


# Showing which pages are shown
if page == "Introduction":
    Pages.intro()