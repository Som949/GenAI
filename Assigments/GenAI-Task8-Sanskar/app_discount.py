import streamlit as st

product_price = st.number_input("Enter product price", min_value=0.0, step=100.0)
dis_percentage = st.slider("Select Discount percentage", min_value=0, max_value=50)
click = st.button("Click")
if click:
    discount_price = product_price - (dis_percentage/100)*product_price
    st.write(f"Original Price: Rs{product_price}")
    st.write(f"Discount Percentage: {dis_percentage}%")
    st.success(f"Discount Successfully applied \n New Price: {discount_price}")


