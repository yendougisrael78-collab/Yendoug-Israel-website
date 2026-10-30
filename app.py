
import streamlit as st

st.set_page_config(
    page_title="Yendoug Israel Website",
    page_icon="🌍"
)

st.title("WELCOME TO YENDOUG ISRAEL WEBSITE")

st.write("My first personal website.")

st.header("About Me")

st.write("My name is Yendoug Israel Yenpumaat.")

st.write("Welcome! Thank you for visiting my website.")

st.header("Visitor Information")

name = st.text_input("What is your name?")

if st.button("Submit"):
    if name:
        st.success(f"Nice to meet you, {name}!")
    else:
        st.warning("Please enter your name.")

st.header("Thank You")

st.write("Thank you for visiting my website!")
