import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler

TELEGRAM_TOKEN = '7765658438:AAEPVNkDTIlTpt8TV_KBAR3wba0M295NRdg'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎨 Salom! Rasm chizuvchi AI botga xush kelibsiz. Matn yuboring.")

async def generate_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text
    await update.message.reply_text("⏳ Rasm chizilmoqda...")

    try:
        api_url = "https://hf.space/embed/stabilityai/st
