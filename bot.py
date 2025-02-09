from flask import Flask
import asyncio
import random
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes
from telegram.ext.filters import TEXT

app = Flask(__name__)

# Your Telegram Bot Token
BOT_TOKEN = '7429555769:AAE8lvgGc5uJLP7fH44_WT6-pdHNWwbXe9w'
bot = Bot(token=BOT_TOKEN)

# Function to handle /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome! Send me any text, and I will generate an image for you.')

# Function to handle text messages
async def generate_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text  # जो भी यूजर भेजे, वही टेक्स्ट लेंगे

    if not prompt:
        await update.message.reply_text("Please provide a valid prompt.")
        return
    
    # Generating the image URL
    image_url = f'https://img.hazex.workers.dev/?prompt={prompt}&improve=true&format=square&random={random.random()}'
    
    # Send the image to the user
    await update.message.reply_text(f'Here is your image based on the prompt: {image_url}')

# Set up the bot application
app_telegram = Application.builder().token(BOT_TOKEN).build()

# Start command
app_telegram.add_handler(CommandHandler('start', start))

# Message handler (text messages)
app_telegram.add_handler(MessageHandler(TEXT & ~TEXT.COMMAND, generate_image))  # अब यह सिर्फ टेक्स्ट मैसेज लेगा

@app.route('/')
def index():
    return "Your bot is running!"

# Function to run Flask and Telegram together
def run():
    loop = asyncio.new_event_loop()  
    asyncio.set_event_loop(loop)  

    loop.create_task(app_telegram.run_polling())  # Run Telegram bot as a background task
    app.run(host="0.0.0.0", port=8080, threaded=True)  # Flask server

if __name__ == '__main__':
    run()
