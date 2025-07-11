
import streamlit as st
import functions


todos = functions.gtodos()


def atodo():
    todo = st.session_state['ntodo'] + '\n'
    todos.append(todo)
    functions.wtodos(todos)


st.title('Todos')
st.subheader("This is a todo app")
st.write("This app wil increase ur productivity")


for todo in todos:
    st.checkbox(todo)


st.text_input(label='Add a todo:', placeholder="Add a new todo...", 
              on_change=atodo, key='ntodo')



print('Hello')
st.session_state
