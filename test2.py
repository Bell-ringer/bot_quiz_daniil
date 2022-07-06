import random
from datetime import datetime

from aiogram.types import CallbackQuery, ParseMode

from aiogram_dialog import ChatEvent
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select, Back, Column, Cancel, Url, SwitchTo, Row
from aiogram_dialog.widgets.text import Format, Jinja

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message

from aiogram_dialog import Dialog, DialogManager, Window, StartMode
from aiogram_dialog.manager.protocols import LaunchMode
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from bot import MyBot
from database import Situations2, Results


class test2SG(StatesGroup):
    introduction = State()
    question = State()
    finish = State()


async def get_data(dialog_manager: DialogManager, **kwargs):
    return {
        'start_time': dialog_manager.current_context().dialog_data.get("start_time", None),
        'end_time': dialog_manager.current_context().dialog_data.get("end_time", None),
        "question": dialog_manager.current_context().dialog_data.get("question", ""),
        'answer_variants': dialog_manager.current_context().dialog_data.get("answer_variants", ""),
        "not_last": dialog_manager.current_context().dialog_data.get("not_last", ""),
        "last": dialog_manager.current_context().dialog_data.get("last", ""),
        "next_button_text": dialog_manager.current_context().dialog_data.get("next_button_text", ""),
    }


async def get_random_answers(manager: DialogManager, situation: str):
    answer_stuff = await Situations2.filter(situation=situation).values_list("text", "score", "next_situation", "comp")
    random.shuffle(answer_stuff)
    manager.current_context().dialog_data["answer_stuff"] = {
        "1": [answer_stuff[0][0], answer_stuff[0][1], answer_stuff[0][2], answer_stuff[0][3]],
        "2": [answer_stuff[1][0], answer_stuff[1][1], answer_stuff[1][2], answer_stuff[1][3]],
        "3": [answer_stuff[2][0], answer_stuff[2][1], answer_stuff[2][2], answer_stuff[2][3]],
        "4": [answer_stuff[3][0], answer_stuff[3][1], answer_stuff[3][2], answer_stuff[3][3]]
    }

    answer_variants = []
    for key in manager.current_context().dialog_data["answer_stuff"]:
        answer_variants.append(f'{key}. {manager.current_context().dialog_data["answer_stuff"][key][0]}')

    return answer_variants


async def get_question(manager: DialogManager, situation: str):
    question = (await Situations2.filter(situation=situation).values_list("question", flat=True))[0]
    manager.current_context().dialog_data["question"] = question

    manager.current_context().dialog_data["answer_variants"] = await get_random_answers(manager, situation)


async def start_test(c: CallbackQuery, button: Button, manager: DialogManager):
    manager.current_context().dialog_data["start_time"] = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    manager.current_context().dialog_data["user_id"] = c.from_user.id
    manager.current_context().dialog_data["name"] = c.from_user.first_name
    manager.current_context().dialog_data["not_last"] = True
    manager.current_context().dialog_data["last"] = False
    manager.current_context().dialog_data["try_num"] = await Results.filter(user_id=c.from_user.id).count() + 1
    manager.current_context().dialog_data["current_question_num"] = "1"
    manager.current_context().dialog_data["c1"] = 0
    manager.current_context().dialog_data["c2"] = 0
    manager.current_context().dialog_data["c3"] = 0
    manager.current_context().dialog_data["c4"] = 0
    manager.current_context().dialog_data["c5"] = 0
    manager.current_context().dialog_data["c6"] = 0
    manager.current_context().dialog_data["c7"] = 0
    manager.current_context().dialog_data["c8"] = 0

    await get_question(manager, manager.current_context().dialog_data["current_question_num"])
    await manager.dialog().switch_to(test2SG.question)


async def answer_handler(c: CallbackQuery, button: Button, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["current_question_num"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    manager.current_context().dialog_data[manager.current_context().dialog_data["answer_stuff"][item_id][3]] += \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]

    await get_question(manager, manager.current_context().dialog_data["current_question_num"])


test2 = Dialog(
    Window(
        Format("Твоя задача провести урок физической культуры"
               " для <i>5 класса</i> общеобразовательной школы.\n"
               "По списку в классе <b>29</b> человек.\n"
               "<b>Тема урока: Акробатические упражнения</b>"),
        Button(Const("Начать тест!"), id="start_test", on_click=start_test),
        Cancel(Const("⏪ Назад")),
        parse_mode=ParseMode.HTML,
        state=test2SG.introduction
    ),
    Window(
        Format("{question}"),
        Jinja("{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="question",
            on_click=answer_handler,
        )),
        getter=get_data,
        state=test2SG.question
    )
)

MyBot.register_dialogs(test2)
