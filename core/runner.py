"""Runs UI for interacting with a chatbot."""
import gradio as gr
from .bots import ChatBot


def run_chat_ui(bot: ChatBot):
    """Runs the UI for the given chatbot."""

    # the function to wrap the chat interface around. Should accept two parameters: a string input message and list of two-element lists of the form [[user_message, bot_message], ...] representing the chat history, and return a string response. See the Chatbot documentation for more information on the chat history format.
    def chat(message, history):
        return bot.chat(message)

    gr.ChatInterface(
        fn=chat,
        textbox=gr.Textbox(lines=5, placeholder="Type your message here..."),
        retry_btn=None,
        stop_btn=None,
        undo_btn=None,
        clear_btn=None,
        title=bot.name,
        description=bot.description,
        chatbot=gr.Chatbot(height=500),
    ).launch()
