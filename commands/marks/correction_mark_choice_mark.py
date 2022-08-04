from typing import Text
from vkbottle.bot import Message
from vkbottle.bot import Blueprint
from PostgreSQLighter import db
from vkbottle import Keyboard, KeyboardButtonColor, Text
import logging


bp = Blueprint('correction_mark_choice_mark') # Объявляем команду
bp.on.vbml_ignore_case = True # Игнорируем регистр сообщений



@bp.on.private_message(payload={'cmd': 'correction_mark_choice_mark'})
async def private_correction_mark_choice_mark(message: Message):
    logging.info(f'{message.peer_id}: I get correction_mark_choice_mark')
    # Информация о юзере
    userInfo = await bp.api.users.get(message.from_id) 
    user_id = userInfo[0].id

    lesson = message.text

    db.edit_account_correction_lesson(user_id, lesson)
    db.commit()

    #Создаем клавиатуру
    keyboard = (
        Keyboard()
        #Добавить кнопку
        .add(Text('5️⃣', {"cmd": "correction_mark"}))
        .add(Text('4️⃣', {"cmd": "correction_mark"}))
        .add(Text('3️⃣', {"cmd": "correction_mark"}))
        .row()
        .add(Text("Назад", {'cmd': 'marks'}), color=KeyboardButtonColor.NEGATIVE)
    )
    
    logging.info(f'{message.peer_id}: I sent correction_mark_choice_mark')
    await message.answer('Какую оценку хочешь?', keyboard=keyboard)











@bp.on.chat_message(payload={'cmd': 'correction_mark_choice_mark'})
async def chat_correction_mark_choice_mark(message: Message):
    logging.info(f'{message.peer_id}: I get correction_mark_choice_mark')
    # Айди чата:
    chat_id = message.chat_id
    
    lesson = message.text

    db.edit_chat_correction_lesson(chat_id, lesson)
    db.commit()

    #Создаем клавиатуру
    keyboard = (
        Keyboard()
        #Добавить кнопку
        .add(Text('5️⃣', {"cmd": "correction_mark"}))
        .add(Text('4️⃣', {"cmd": "correction_mark"}))
        .add(Text('3️⃣', {"cmd": "correction_mark"}))
        .row()
        .add(Text("Назад", {'cmd': 'correction_mark_choice_lesson'}), color=KeyboardButtonColor.NEGATIVE)
    )

    logging.info(f'{message.peer_id}: I sent correction_mark_choice_mark')
    await message.answer('Какую оценку хочешь?', keyboard=keyboard)
