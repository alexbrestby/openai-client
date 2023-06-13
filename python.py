import os
import openai
import asyncio
import telegram
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.organization = os.getenv('OPENAI_ORGANIZATION_KEY')
bot_api_key = os.getenv('BOT_API_KEY')

async def main():
    bot = telegram.Bot(bot_api_key)
    async with bot:
        print(await bot.get_me())

if __name__ == '__main__':
    asyncio.run(main())

# images = openai.Image.create(
#   prompt="A cute baby sea otter",
#   n=2,
#   size="1024x1024"
# )

# print(images)

# messages = []

# while True:
#     message = input("User: ")   # Prompt the user for input
#     if message == "quit":
#         break

#     messages.append({"role": "user", "content": message})
#     chat = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         temperature=0.8,
#         messages=messages
#     )
#     reply = chat
#     # reply = chat.choices[0].message.content
#     print(f"ChatGPT: {reply}")
#     messages.append({"role": "assistant", "content": reply})
