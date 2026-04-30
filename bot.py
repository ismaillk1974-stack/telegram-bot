import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8131253936:AAFFBV0qFAhqkNnGvFtmouoaao9ZdFCEnnI"

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    ydl_opts = {
        'outtmpl': 'video.mp4',
        'format': 'best',
        'noplaylist': True,
    }

    try:
        await update.message.reply_text("⏳ جاري التحميل...")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        await update.message.reply_video(video=open("video.mp4", "rb"))

    except Exception as e:
        await update.message.reply_text("❌ صار خطأ")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, download))

app.run_polling()
