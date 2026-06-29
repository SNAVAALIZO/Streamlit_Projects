import streamlit as st

st.title("Hello, Streamlit! 🎉")
st.write("If you can see this, Streamlit is working on your Mac.")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name}!")

number = st.slider("Pick a number", 0, 100, 50)
st.write(f"You picked: **{number}**")

if st.button("Click me"):
    st.balloons()