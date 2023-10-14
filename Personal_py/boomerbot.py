import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Handlers
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Welcome to my bot.")

def about_me(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I am a bot. Nice to meet you!")

def hello(update, context):
    message_text = update.message.text.lower()
    if 'hello' in message_text:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hello there!")

def option_1(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Option 1 selected!")

def option_2(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Option 2 selected!")

def handle_direct_message(update, context):
    user_id = update.message.from_user.id
    message_text = update.message.text

    reply_text = "Thanks for reaching out! I will check your message shortly."

    context.bot.send_message(chat_id=user_id, text=reply_text)

def help(update, context):
    help_text = "Here are the available commands:\n\n" \
                "/start - Start the bot\n" \
                "/aboutme - Learn about the bot\n" \
                "/hello - Greet the bot\n" \
                "/option1 - Select option 1\n" \
                "/option2 - Select option 2\n" \
                "/help - Show this help message"
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

def unknown(update, context):
    unknown_text = "Sorry, I didn't understand that command. Type /help to see the list of available commands."
    context.bot.send_message(chat_id=update.effective_chat.id, text=unknown_text)

def echo(update, context):
    echo_text = f"You said: {update.message.text}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=echo_text)

def inline_query(update, context):
    query = update.inline_query.query
    results = [
        telegram.InlineQueryResultArticle(
            id="1",
            title="Echo",
            input_message_content=telegram.InputTextMessageContent(message_text=query)
        )
    ]
    context.bot.answer_inline_query(update.inline_query.id, results)

# Main Function
def main():
    token = "YOUR_TOKEN_HERE"  # Replace with your actual bot token
    bot = telegram.Bot(token=token)
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("aboutme", about_me))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command) & Filters.regex(r'(?i)hello'), hello))
    dispatcher.add_handler(CommandHandler("option1", option_1))
    dispatcher.add_handler(CommandHandler("option2", option_2))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
    dispatcher.add_handler(MessageHandler(Filters.inline_query, inline_query))

    updater.start_polling()

if __name__ == '__main__':
    main()
