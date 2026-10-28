import streamlit as st

st.title("Simple Sales Dashboard")
st.write("This is simple sales dashboard where we keep track of all the sales")

month = st.selectbox(
    "Enter the month",
    ["January", "February", "March", "April"]
)

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

if month:
    st.write(f"Sales of {month} is {sales[month]}")

st.bar_chart(list(sales.values()))

