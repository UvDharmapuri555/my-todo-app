import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout='wide')


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.write_todos(todos)


st.title("Todo App")
st.subheader("This app is used to increase your productivity.")
st.write("Type in the <b>input box</b> to <b>add</b> a todo.", unsafe_allow_html=True)
st.write('Check off a <b>checkbox</b> to <b>complete</b> a todo.', unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.title(), key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo...", on_change=add_todo, key='new_todo')