import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Welcome to my bot.")

def aboutme(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I am a bot. Nice to meet you!")

def hello(update, context):
    message_text = update.message.text.lower()
    if 'hello' in message_text:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hello there!")

def option1(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Option 1 selected!")

def option2(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Option 2 selected!")

def handle_dm2(update, context):
    # Retrieve the message text and sender's ID
    message_text = update.message.text
    sender_id = update.message.from_user.id

    # Send a response to the DM sender
    response_text = f"Thank you for reaching out! Your message: {message_text}"
    context.bot.send_message(chat_id=sender_id, text=response_text)

def handle_dm(update, context):
    user_id = update.message.from_user.id
    message_text = update.message.text

    reply_text = "Thanks for reaching out! I will check your message shortly."

    context.bot.send_message(chat_id=user_id, text=reply_text)

def main():
    token = "YOUR_TOKEN_HERE"  # Replace with your actual bot token
    bot = telegram.Bot(token=token)
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)
    aboutme_handler = CommandHandler("aboutme", aboutme)
    hello_handler = MessageHandler(Filters.text & (~Filters.command) & Filters.regex(r'(?i)hello'), hello)
    option1_handler = CommandHandler("option1", option1)
    option2_handler = CommandHandler("option2", option2)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(aboutme_handler)
    dispatcher.add_handler(hello_handler)
    dispatcher.add_handler(option1_handler)
    dispatcher.add_handler(option2_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()
