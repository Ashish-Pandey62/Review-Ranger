# import streamlit as st
# from PIL import Image
# from rasa.core.agent import Agent

# agent = Agent.load(model_path='models')

# # For Rasa 2 (I tried it with 2.8.8)
# # def generate_response(text):
# #     response = agent.parse_message_using_nlu_interpreter(
# #                 message_data='Hello there')
# #     return response

# # For Rasa 3


# def generate_response(text):
#     response = agent.parse_message(
#         message_data='Hello there')
#     return response


# st.title("Automatic Review Bot")

# image = Image.open("image.jpeg")
# st.image(image, use_column_width=True)

# user_text = st.text_area("Enter your text:", "")

# if st.button("Generate Review"):
#     if user_text:
#         response = generate_response(user_text)
#         st.success(response)
#     else:
#         st.warning("Please enter some text.")

# st.info("Enter some text to generate a review.")

import asyncio
from rasa.core.agent import Agent
from rasa.shared.utils.io import json_to_string

class Model:

    def __init__(self, model_path: str) -> None:
        self.agent = Agent.load(model_path)
        print("NLU model loaded")


    def message(self, message: str) -> str:
        message = message.strip()
        result = asyncio.run(self.agent.parse_message(message))
        return json_to_string(result)

mdl = Model("./models/model.tar.gz")
sentence = "hello"
print(mdl.message(sentence))
