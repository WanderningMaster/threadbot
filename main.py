import telebot
import config #config.py

BOT_TOKEN = config.BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(content_types=['text'])
def start_message(message):
    if('/thread' in message.text):
        thread = message.text.strip('/thread')
        print(thread)
        id = message.chat.id
        thread = '_'.join(thread.split())
        channel_msg = bot.send_message(chat_id=config.CHAT_ID, text="#" + thread)
        bot.forward_message(id, config.CHAT_ID, channel_msg.message_id)

if __name__ == "__main__":
    bot.polling()
