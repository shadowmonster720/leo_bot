import telebot

bot = telebot.TeleBot("8223654707:AAHz7Lnkhd_SuVv1VNIvaoqGDXYZBZq-1yQ")

@bot.message_handler(func=lambda message: True)
def welcome(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id, "سلام جانم ؟")

print("ربات روشن شد ✅")
bot.polling()
