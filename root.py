from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from aiogram_dialog import Dialog, DialogManager, Window, StartMode
from aiogram_dialog.manager.protocols import LaunchMode
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from bot import MyBot
from test1 import test1SG
from config import ADMIN_ID
from database import admin_load


async def load_handler(m: Message, dialog_manager: DialogManager):
    await admin_load()

    MyBot.bot.send_document(ADMIN_ID, open("results.xlsx", 'rb'))


async def start(m: Message, dialog_manager: DialogManager):
    if m.from_user.id == ADMIN_ID:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        item = KeyboardButton('Выгрузить результаты .xls 📊')
        markup.add(item)
        await MyBot.bot.send_message(m.from_user.id, f'Привет, <b>{m.from_user.first_name}</b>\n'
                                                     f'Это бот с тестами для преподавателей', parse_mode="HTML",
                                     reply_markup=markup)
        await dialog_manager.start(mainSG.choose_test, mode=StartMode.RESET_STACK)
    else:
        await MyBot.bot.send_message(m.from_user.id, f'Привет, <b>{m.from_user.first_name}</b>\n'
                                                     f'Это бот с тестами для преподавателей', parse_mode="HTML")
        await dialog_manager.start(mainSG.choose_test, mode=StartMode.RESET_STACK)


MyBot.register_handler(method=start, commands=["start"])
MyBot.register_handler(method=load_handler, text=['Выгрузить результаты .xls 📊'])


class mainSG(StatesGroup):
    choose_test = State()


main_menu = Dialog(
    Window(
        Const("Выбери, какой тест ты желаешь пройти!"),
        Start(Const("Ведение и бросок мяча"), id="po", state=test1SG.introduction),
        # Start(Const("Тест 2"), id="po", state=test2SG.post),
        # Start(Const("Тест 3"), id="po", state=test3SG.post),
        state=mainSG.choose_test
    ),
    launch_mode=LaunchMode.ROOT
)

MyBot.register_dialogs(main_menu)
