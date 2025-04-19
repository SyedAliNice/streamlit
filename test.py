import streamlit as st

st.header("Wrist Watch detection")
st.subheader("by Syed Ali Hassan")
st.markdown("""# Welcome to My Jupyter Notebook

## ✨ Introduction
This notebook is created to demonstrate the use of **Markdown** for writing formatted text in Jupyter Notebooks. You can use it to create headers, lists, links, code snippets, and more.

---

## 📚 Topics Covered
- Markdown formatting
- Python code integration
- Inline code and code blocks
- Displaying images and links

---

## 🧠 Example Code
You can include code like this:

```python
def greet(name):
    return f"Hello, {name}!"

greet("World")
""")



st.code("""
        name = "Ali"
        age = 23
        print(f"My name is {name} and age is {age}") 
""")

#age = 23
age = st.text_input("Enter your age: ")

st.markdown(f"My age is **{age}**")



import pandas as pd

data = pd.read_csv(r"C:\Users\NEC\Desktop\Classification Project in R\assign3_test.csv")

col = data['x5']

st.bar_chart(col)

st.radio("what is your age", ["age", "gender", "age1"])

st.selectbox("what is your age", ["age", "gender", "age1"])


img = st.file_uploader("Choose the image:", type=['png', 'jpg', 'jpeg'])

st.image(img, caption="Caption")