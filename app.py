import requests
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
URL= os.getenv("URL")
st.title("Yogendra's Personal Assistant")


st.subheader("Chat with me")

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
            st.session_state.messages.append({"role":"assistant","content":"Some internal error occurs"})

