from aiogram import Bot
from io import BytesIO

async def send_telegram_msg(bot: Bot, chat_id: int, message: str):
    return (await bot.send_message(chat_id=chat_id, text=message))

async def send_telegram_bytes_file(bot: Bot, chat_id: int, file: str, caption: str = None, reply_to_message_id: int = None):
    obj = BytesIO(file)
    obj.name = caption

    return (await bot.send_document(chat_id=chat_id, document=obj, caption=caption, reply_to_message_id=reply_to_message_id))