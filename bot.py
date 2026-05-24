from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8286171417:AAHEfJu9DOHL95K3aUJNaIYItU_5snH9lAE"

CAT_GIF = "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif"

async def reply_cat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_animation(
        animation=CAT_GIF,
        caption="🐱 Miyov!"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & (~filters.COMMAND), reply_cat)
)

print("Bot ishlayapti...")
app.run_polling()