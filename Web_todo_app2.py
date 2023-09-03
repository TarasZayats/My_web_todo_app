import streamlit as st
import functions

todos = functions.get_todos()
done_todos = functions.get_done_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("Манюні завдання на щодень ^_^")
st.subheader("Збільш свою продуктивність ;-)")
st.subheader("")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        done_todos.append(todo)
        todos.pop(index)
        functions.write_todos(todos)
        functions.write_done_todos(done_todos)
        del st.session_state[todo]
        st.experimental_rerun()
#st.write("")
st.text_input(label="", placeholder="Введи нове завдання",
              on_change=add_todo, key='new_todo')
st.subheader("")
st.subheader("")
#st.subheader("")
st.subheader("Виконані завдання:")
for done_todo in done_todos:
    st.checkbox(done_todo, key=done_todo, disabled=True)

