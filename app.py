import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
import chromadb
load_dotenv()


st.title("My ai app ")

with st.sidebar:
    st.header("Settings")
    name=st.text_input("Enter your name")
    mood=st.selectbox("what will ai mood be today?", ["happy","sad","fuck u"])
    creativity = st.slider("creativity ", 0, 2 )
    if st.button("save"):
        st.write(f"saved, your name is {name} and your mood is {mood} and your creativity is {creativity}")

prompt=st.chat_input("ask smth")
fullprompt=f"mood is:{mood} user name is this:{name}and creativity is this:{creativity}. the user prompt:{prompt}"

if prompt:
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GITHUB_TOKEN"),
    )

    r = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=creativity,
        messages=[{"role": "user", "content": mood + prompt}],
    )
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        st.write(f"{r.choices[0].message.content}")













