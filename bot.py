import os
from pyrogram import Client, filters
from uploader import upload_to_drive

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document)
async def handle_doc(client, message):
    await message.reply_text("📥 Downloading file...")
    path = await message.download()
    await message.reply_text("☁️ Uploading to Google Drive...")
    link = upload_to_drive(path)
    await message.reply_text(f"✅ Uploaded:\n🔗 {link}")
    os.remove(path)

app.run()
