import telebot

# التوكن مالتك الصحيح
API_TOKEN = '8447745974:AAFVl9y3wS_RRWKb99HiwqkWCqK6q02fQbA'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 البوت شغال دائمياً! دزلي الفيديو.")

@bot.message_handler(content_types=['video'])
def handle_video(message):
    bot.reply_to(message, "⏳ جاري التنظيف... انتظر ثواني.")

bot.infinity_polling()

