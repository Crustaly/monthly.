import streamlit as st
import time
from PIL import Image


st.title("Write in your period diary here!")
st.header("How are you feeling today?")

option = st.selectbox("How are you feeling today?", ("Happy", "Middle", "Sad"))

st.write(" ")


st.subheader("Write about your day!")
st.write("(We will give you customized advice)")


text = st.text_area("Enter Your Feelings Below:", height=300)

submit = st.button("Done!")

if submit:
    with st.spinner("Generating personalized advice..."):
        time.sleep(3)
    st.success("Done!")

    with open("advice.png", "rb") as file:
        btn = st.download_button(
            label="Download image", data=file, file_name="advice.png", mime="image/png"
        )
