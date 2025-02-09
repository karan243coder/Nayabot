from flask import Flask
import requests
import random
from telegram import Bot
from telegram.ext import Application, CommandHandler, MessageHandler
from telegram.ext.filters import TEXT

app = Flask(__name__)

# Your Telegram Bot Token
BOT_TOKEN = '7429555769:AAE8lvgGc5uJLP7fH44_WT6-pdHNWwbXe9w'
bot = Bot(token=BOT_TOKEN)

# Function to handle messages from users
async def start(update, context):
    await update.message.reply_text('Welcome! Send me a prompt and I will generate an image for you.')

async def generate_image(update, context):
    prompt = ' '.join(context.args)
    if not prompt:
        await update.message.reply_text("Please provide a prompt.")
        return
    
    # Generating the image URL
    image_url = f'https://img.hazex.workers.dev/?prompt={prompt}&improve=true&format=square&random={random.random()}'
    
    # Send the image to the user
    await update.message.reply_text(f'Here is your image based on the prompt: {image_url}')

# Set up the bot application
app_telegram = Application.builder().token(BOT_TOKEN).build()

# Start command
app_telegram.add_handler(CommandHandler('start', start))

# Message handler
app_telegram.add_handler(MessageHandler(TEXT, generate_image))

# Start the bot in the background
async def run_bot():
    await app_telegram.run_polling()

import threading
threading.Thread(target=lambda: app_telegram.run_polling(), daemon=True).start()

@app.route('/')
def index():
    return "Your bot is running!"

if __name__ == '__main__':
    app.run(port=8080)
