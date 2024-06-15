"""
See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
# genai.configure(api_key="")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)
chat_history = [ 
        {
            "role": "user",
            "parts":[

        "Your Name is Dilum Induwara",
            
            ]
        },
        {
            "role": "user",
            "parts":[

        "Your Age is 22 years old",
            
            ]
        },
        {
        "role": "model",
        "parts": [
            "Hi! How can I help you today? \n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "hi",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Hi there! 👋  \n\nWhat can I do for you today? 😊 \n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "hi",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Hi! 👋  It's nice to hear from you. 😊  \n\nWhat's on your mind today?  I'm ready to help with anything you need. \n",
        ],
        },
    ]


def chat_response():
    chat_session = model.start_chat(history=chat_history)

    userInput= input("What do you need to ask from me ? ")

    response = chat_session.send_message(userInput)

    print(response.text)

