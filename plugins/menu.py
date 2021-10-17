from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
from vkbottle.bot import Blueprint


bp = Blueprint('menu')



#Если написали "Меню" или нажали на соответствующую кнопку
@bp.on.message(text="Меню")
@bp.on.message(payload={'cmd': 'menu'})
async def menu(message: Message):
    #Создаем клавиатуру
    keyboard = (
        Keyboard()
        #Добавить кнопки
        .add(Text('Войти', {'cmd': 'login'}), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text('Дневник', {'cmd': 'keyboard_diary'}), color=KeyboardButtonColor.PRIMARY)
        .add(Text('Расписание', {'cmd': 'keyboard_schedule'}), color=KeyboardButtonColor.PRIMARY)
    )

    #Ответ в чат
    await message.answer('Ты в главном меню.', keyboard=keyboard)