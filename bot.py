from flask import Flask, request
import requests
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

app = Flask(__name__)

# Your Telegram Bot Token
BOT_TOKEN = 'YOUR_BOT_TOKEN'
bot = Bot(token=BOT_TOKEN)

# Function to handle messages from users
def start(update, context):
    update.message.reply_text('Welcome! Send me a prompt and I will generate an image for you.')

def generate_image(update, context):
    prompt = ' '.join(context.args)
    if not prompt:
        update.message.reply_text("Please provide a prompt.")
        return
    
    # Generating the image URL
    image_url = f'https://img.hazex.workers.dev/?prompt={prompt}&improve=true&format=square&random={Math.random()}'
    
    # Send the image to the user
    update.message.reply_text(f'Here is your image based on the prompt: {image_url}')

# Set up the command handlers
updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Start the bot command
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Image generation based on user input
message_handler = MessageHandler(Filters.text, generate_image)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()

@app.route('/')
def index():
    return "Your bot is running!"

if __name__ == '__main__':
    app.run(port=5000)
