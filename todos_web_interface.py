import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.write_todos(todos)


st.title("Todo App")
st.subheader("This app is used to increase your productivity.")
st.write("Type in the input box to add a todo.")
st.write('Check off a checkbox to complete a todo.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.title(), key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo...", on_change=add_todo, key='new_todo')