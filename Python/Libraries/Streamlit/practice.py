import streamlit as st
import pandas as pd


st.title("Student Dashboard")

st.header("Student Information")

st.subheader("Academic details")
st.write("It will contains all information about the Academic details")
st.caption("Updated data")

st.subheader("Code")
code = "def add: \n x=10 \n y=16 \n return x+y"
st.code(code, language="python")

data = {
    "Name": ["Aman", "Riya", "Karan"],
    "Marks": [85, 92, 78]
}

df = pd.DataFrame(data)
st.dataframe(df)

data1 = {
    "name": "Aman",
    "age": 22,
    "skills": ["Python", "SQL"]
}

st.json(data1)

data3 = pd.DataFrame({
    "Sales": [100, 150, 130, 200]
})

st.line_chart(data3)

date4 = pd.DataFrame({
    "Product": [120, 179, 189],
    "Sales": [78, 98, 90]
})

st.bar_chart(date4, x="Product", y="Sales")

show_data = st.checkbox("Show data")

language = st.radio(
    "Choose a language",
    ["Cpp", "Python", "C"]
)

st.write("Language: ", language)

language = st.multiselect(
    "Choose a language",
    ["Cpp", "Python", "C"]
)



