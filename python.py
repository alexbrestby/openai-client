import os
import openai
import logging
from telegram import Update
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

messages = []   #Context storage for ChatGPT

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.organization = os.getenv('OPENAI_ORGANIZATION_KEY')
bot_api_key = os.getenv('BOT_API_KEY')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я ЧатДжиПиТи на минималках. Можешь задать мне свой вопрос...")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text   # Prompt the user for input

    messages.append({"role": "user", "content": msg})
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.8,
        messages=messages
    )
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    await update.message.reply_text(reply)

if __name__ == '__main__':
    application = ApplicationBuilder().token(bot_api_key).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()
