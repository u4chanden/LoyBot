from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hello! This is your bot.')

def main():
    updater = Updater("6645928461:AAGQgPwVnyRrco7blo_lgg0oEWoyptPR7-c", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
