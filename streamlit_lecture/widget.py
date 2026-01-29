import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")

name=st.text_input("Enter your name:")

age=st.slider("Select yout age",0,100,25)

st.write(f'Your age is {age}')

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your fav language:", options)
st.write(f'Your slected {choice}')

if name:
    st.write(f"Hello, {name}")

data = {
    "Name": ["John", "Jane", "Doe", "Smith"],
    "Age": [28, 34, 29, 42],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]   
}

df=pd.DataFrame(data)
st.write(df)

uploaded_files = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_files is not None:
    df=pd.read_csv(uploaded_files)
    st.write(df)
