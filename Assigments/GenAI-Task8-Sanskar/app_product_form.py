import streamlit as st

product_name = st.sidebar.text_input("Enter product name")

category = st.sidebar.selectbox(
    "Enter Product Category",
    ["Electronics", "Healthcare", "Hardware"]
)

price = st.sidebar.number_input("Enter price", min_value=0.0, step=10000.0)

click = st.button("Add Product")
if click:
    st.success("Product Added")
    st.write(f"Product Name: {product_name}")
    st.write(f"Category: {category}")
    st.write(f"Price: {price}")



