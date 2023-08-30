import streamlit as st
from streamlit_chat import message
from utils import get_initial_message, get_chatgpt_response, update_chat
import os
from dotenv import load_dotenv

load_dotenv()

# Get the initial message
initial_message = get_initial_message()

# Get the chatGPT response
chatgpt_response = get_chatgpt_response(initial_message)

# Update the chat history
update_chat(chatgpt_response)

# Display the chat
message(initial_message, chatgpt_response)
