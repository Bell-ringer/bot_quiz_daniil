from aiogram.types import CallbackQuery, ParseMode

from aiogram_dialog import ChatEvent
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select, Back, Column, Cancel, Url, SwitchTo
from aiogram_dialog.widgets.text import Format

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message

from aiogram_dialog import Dialog, DialogManager, Window, StartMode
from aiogram_dialog.manager.protocols import LaunchMode
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from bot import MyBot
from test1 import test1SG


async def start(m: Message, dialog_manager: DialogManager):
    await MyBot.bot.send_message(m.from_user.id, f'Привет, <b>{m.from_user.first_name}</b>\n'
                                                 f'Это бот с тестами для преподавателей', parse_mode="HTML")
    await dialog_manager.start(mainSG.choose_test, mode=StartMode.RESET_STACK)

MyBot.register_handler(method=start, commands=["start"])


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
