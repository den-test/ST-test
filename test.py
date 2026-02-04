import streamlit as st
import streamlit_chat
from streamlit_chat import message


def main():
    if "messages" not in st.session_state:
        st.session_state.messages = []



    with st.sidebar:
        st.title("sidebar")
        b = st.button("clear")
        if b:
            st.session_state.messages.clear()



    st.title("steamlit test")
    st.header("header")
    st.write("test")
    st.write("")
    st.text("text")

    q = st.text_input("input")
    st.write(q)


    w = st.chat_input("Input")
    if w:
        st.session_state.messages.append(w)






    mess = st.session_state.get("messages", [])

    for i, m in enumerate(mess):
        if i % 2 == 0:
            message(m, is_user=True, key=str(i))
        else:
            message(m, is_user=False, key=str(i))







if __name__ == '__main__':
    main()