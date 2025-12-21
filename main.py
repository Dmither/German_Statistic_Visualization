import streamlit as st
from general import general
from demographics import demographics
from economics import economics
from socials import socials
from infrastructure import infrastructure
from environment import environment
from climate import climate

if "page" not in st.session_state:
    st.session_state.page = "General"


st.sidebar.header('Menu')
if st.sidebar.button("General"):
    st.session_state.page = "General"
if st.sidebar.button("Demographics"):
    st.session_state.page = "Demographics"
if st.sidebar.button("Economics"):
    st.session_state.page = "Economics"
if st.sidebar.button("Socials"):
    st.session_state.page = "Socials"
if st.sidebar.button("Infrastructure"):
    st.session_state.page = "Infrastructure"
if st.sidebar.button("Environment"):
    st.session_state.page = "Environment"
if st.sidebar.button("Climate"):
    st.session_state.page = "Climate"


pages = {
    "General": general,
    "Demographics": demographics,
    "Economics": economics,
    "Socials": socials,
    "Infrastructure": infrastructure,
    "Environment": environment,
    "Climate": climate,
}
pages[st.session_state.page]()