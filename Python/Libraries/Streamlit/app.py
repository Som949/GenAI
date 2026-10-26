import streamlit as st

st.write("Hello, Streamlit!")

st.title("Hello Streamlit")
st.write("This is my first streamlit app")
st.header("Welcome to streamlit")
st.subheader("This is subheader")
st.text("This is my plain text")

## Buttons check boxes and sliders

if st.button("Click me!"):
    st.write("Button clicked")

agree = st.checkbox("I agree")
if agree:
    print("You agreed")

level = st.slider("Select a level: ", 1, 10, 5)
st.write(f"Selected level: {level}")

# file upload
uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())



