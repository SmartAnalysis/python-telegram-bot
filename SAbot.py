import telegram
from telegram.ext import CommandHandler, Updater

# Ganti YOUR_BOT_TOKEN dengan token bot Telegram Anda
TOKEN = '5960627478:AAH0StbGviok152TkbCeoCjCu5A3BNrIjbc'

# Fungsi untuk menangani perintah /start
def start(update, context):
    # Kirim pesan balasan ke pengguna
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hai apa kabar, saya adalah bot dari perusahaan Smart Analysis")

# Inisialisasi bot dan tambahkan handler perintah /start
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Jalankan bot
updater.start_polling()