import requests
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
URL= os.getenv("URL")
st.title("Yogendra's Personal Assistant")
st.subheader("What can I  do?")

st.markdown("""
            1. Answer questions on various topics.   
            2. Arrange Calendar events and meetings.  
            3. Read your emails and send replies, can even summarize them for you.
            4. Manage your tasks and to-do lists.
            5. Take quick notes for you.
            6. Track your expenses and budgeting.
            """)


st.subheader("💬 Chat with your assistant")

if "messages" not in st.session_state:
    st.session_state.messages=[]


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



user_message = st.chat_input()

if user_message:
    with st.chat_message("user"):
        st.markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message})
    


    try:
        response = requests.post(
            URL, 
            json={"message": user_message},
            timeout=120
        )
        
        ai_response = response.json()[0]["output"]
                
        with st.chat_message("assistant"):
            st.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})

    except requests.exceptions.Timeout:
        with st.chat_message("error"):
            st.markdown("Taking Longer time to respond")

    except Exception as e:
        with st.chat_message("assistant"):
            st.markdown("Some Internal Error occurs")    
            st.session_state.messages.append({"role":"assistant","content":"SOme internal error occurs"})

