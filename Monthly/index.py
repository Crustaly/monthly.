import openai
import streamlit as st
from PIL import Image
from streamlit.components.v1 import html
from PIL import Image


col1, mid, col2 = st.columns([1, 4, 20])
with col1:
    st.image("logo.png", width=130)
with col2:
    st.write("")
    st.write("")

    st.title("         " + "       Monthly.")

st.header("Helping you manage your emotions with NLP")
st.write("Created by Crystal Yang")
simple = "Just write down the emotions you feel on your period, and we will generate a customized mental health plan for you!"
st.subheader(simple)
st.title("")
st.title("")
st.title("")


col1, col3 = st.columns([1.3, 1])
with col1:
    st.button("Get Started!")
with col3:
    with open("cal.png", "rb") as file:
        btn = st.download_button(
            label="My Calendar", data=file, file_name="cal.png", mime="image/png"
        )
