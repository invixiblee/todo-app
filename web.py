
import streamlit as st
import functions

todos = functions.gtodos()

st.title('Todos')
st.subheader("This is a todo app")
st.write("This app wil increase ur productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder="Add a new todo...")