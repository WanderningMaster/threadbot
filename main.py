import telebot
import config #create config.py with BOT_TOKEN and CHAT_ID

BOT_TOKEN = config.BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["help"])
def help_command(message):
    f = open('help.txt', 'r')
    content = f.read()
    bot.send_message(message.chat.id, content)



@bot.message_handler(commands=["commands"])
def help_command(message):
    f = open('commands.txt', 'r')
    content = f.read()
    bot.send_message(message.chat.id, content)



@bot.message_handler(content_types=['text'])
def start_message(message):
    if('/thread' in message.text):
        thread = message.text.strip('/thread')
        id = message.chat.id
        thread = '_'.join(thread.split())
        channel_msg = bot.send_message(chat_id=config.CHAT_ID, text="#" + thread)
        bot.forward_message(id, config.CHAT_ID, channel_msg.message_id, True)

if __name__ == "__main__":
    print('Bot started polling')
    bot.polling()
