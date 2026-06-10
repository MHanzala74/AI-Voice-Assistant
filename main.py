import streamlit as st
from ai_assistant import commands
import keyboard

st.title("🎙️ Voice Assistant")

if "running" not in st.session_state:
    st.session_state.running = False

col1, col2 = st.columns(2)

with col1:
    if st.button("Start Listening"):
        st.session_state.running = True

with col2:
    if st.button("Stop"):
        st.session_state.running = False

status = st.empty()

if st.session_state.running:

    if keyboard.is_pressed('esc'):
        st.session_state.running = False
        status.warning("Assistant stopped by ESC key.")

    else:
        status.success("Listening...")
        commands()
        st.rerun()