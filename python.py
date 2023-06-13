import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API')
openai.organization = os.getenv('OPENAI_ORGANIZATION')
tg_bot_api = os.getenv('BOT_API')

print(tg_bot_api)

messages = []

while True:
    message = input("User: ")   # Prompt the user for input
    if message == "quit":
        break

    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
