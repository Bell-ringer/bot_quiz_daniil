import os
import random
from datetime import datetime

from aiogram.types import CallbackQuery, ParseMode

from aiogram_dialog import ChatEvent
from aiogram_dialog.widgets.kbd import Button, Select, Cancel, Row
from aiogram_dialog.widgets.text import Format, Jinja

from aiogram.dispatcher.filters.state import StatesGroup, State

from aiogram_dialog import Dialog, DialogManager, Window, StartMode
from aiogram_dialog.manager.protocols import LaunchMode
from aiogram_dialog.widgets.text import Const

from database import Situations, Results
from bot import MyBot
from graph import graph

next_state: State


class test1SG(StatesGroup):
    introduction = State()
    c1s1 = State()
    c1s2 = State()
    c5s4 = State()
    c5s2 = State()
    c5s1 = State()
    c4s4 = State()
    c6s2 = State()
    c7s2 = State()
    c7s3 = State()
    c1s5 = State()
    c1s3 = State()
    c3s1 = State()
    c3s2_1 = State()
    c3s2_2 = State()
    c3s3 = State()
    c2s1 = State()
    c4s3 = State()
    c4s2 = State()
    c2s2 = State()
    c6s3 = State()
    c4s1 = State()
    c6s1 = State()
    c2s4 = State()
    c2s3 = State()
    c6s4 = State()
    c7s4 = State()
    c7s5 = State()
    c5s5 = State()
    c8s3 = State()
    c8s1 = State()
    c8s2 = State()
    c3s4 = State()
    c8s4 = State()
    answer = State()


# функция для получения данных из состояний
async def get_data(dialog_manager: DialogManager, **kwargs):
    return {
        'start_time': dialog_manager.current_context().dialog_data.get("start_time", None),
        'end_time': dialog_manager.current_context().dialog_data.get("end_time", None),
        'answer_buffer': dialog_manager.current_context().dialog_data.get("answer_buffer", ""),
        'answer_variants': dialog_manager.current_context().dialog_data.get("answer_variants", ""),
    }


async def next_question(c: CallbackQuery, button: Button, manager: DialogManager):
    await manager.dialog().switch_to(next_state)


async def get_random_answers(manager: DialogManager, situation: int):
    answer_stuff = await Situations.filter(situation=situation).values_list("text", "answer", "score")
    random.shuffle(answer_stuff)
    manager.current_context().dialog_data["answer_stuff"] = {
        "1": [answer_stuff[0][0], answer_stuff[0][1], answer_stuff[0][2]],
        "2": [answer_stuff[1][0], answer_stuff[1][1], answer_stuff[1][2]],
        "3": [answer_stuff[2][0], answer_stuff[2][1], answer_stuff[2][2]],
        "4": [answer_stuff[3][0], answer_stuff[3][1], answer_stuff[3][2]]
    }

    answer_variants = []
    for key in manager.current_context().dialog_data["answer_stuff"]:
        answer_variants.append(f'{key}. {manager.current_context().dialog_data["answer_stuff"][key][0]}')

    manager.current_context().dialog_data["answer_variants"] = answer_variants


async def start_test(c: CallbackQuery, button: Button, manager: DialogManager):
    manager.current_context().dialog_data["start_time"] = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    manager.current_context().dialog_data["user_id"] = c.from_user.id
    manager.current_context().dialog_data["name"] = c.from_user.first_name

    manager.current_context().dialog_data["try_num"] = await Results.filter(user_id=c.from_user.id).count() + 1

    await get_random_answers(manager, 1)
    await manager.dialog().switch_to(test1SG.c1s1)


async def c1s1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c1s1"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 2)

    global next_state
    next_state = test1SG.c1s2
    await manager.dialog().switch_to(test1SG.answer)


async def c1s2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c1s2"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 3)

    global next_state
    next_state = test1SG.c5s4
    await manager.dialog().switch_to(test1SG.answer)


async def c5s4_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c5s4"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 4)

    global next_state
    next_state = test1SG.c5s2
    await manager.dialog().switch_to(test1SG.answer)


async def c5s2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c5s2"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 5)

    global next_state
    next_state = test1SG.c5s1
    await manager.dialog().switch_to(next_state)


async def c5s1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c5s1"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 6)

    global next_state
    next_state = test1SG.c4s4
    await manager.dialog().switch_to(test1SG.answer)


async def c4s4_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c4s4"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 7)

    global next_state
    next_state = test1SG.c6s2
    await manager.dialog().switch_to(test1SG.answer)


async def c6s2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c6s2"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 8)

    global next_state
    next_state = test1SG.c7s2
    await manager.dialog().switch_to(test1SG.answer)


async def c7s2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c7s2"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 9)

    global next_state
    next_state = test1SG.c7s3
    await manager.dialog().switch_to(test1SG.answer)


async def c7s3_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c7s3"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 10)

    global next_state
    next_state = test1SG.c1s5
    await manager.dialog().switch_to(test1SG.answer)


async def c1s5_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c1s5"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 11)

    global next_state
    next_state = test1SG.c1s3
    await manager.dialog().switch_to(next_state)


async def c1s3_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c1s3"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 12)

    global next_state
    next_state = test1SG.c3s1
    await manager.dialog().switch_to(test1SG.answer)


async def c3s1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c3s1"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 13)

    global next_state
    next_state = test1SG.c3s2_2
    await manager.dialog().switch_to(test1SG.answer)


async def c3s2_1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c3s2"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 14)

    global next_state
    next_state = test1SG.c3s3
    await manager.dialog().switch_to(test1SG.answer)


async def c3s2_2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c3s2"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 15)

    global next_state
    next_state = test1SG.c3s3
    await manager.dialog().switch_to(test1SG.answer)


async def c3s3_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c3s3"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 16)

    global next_state
    next_state = test1SG.c2s1
    await manager.dialog().switch_to(test1SG.answer)


async def c2s1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c2s1"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 17)

    global next_state
    next_state = test1SG.c4s3
    await manager.dialog().switch_to(test1SG.answer)


async def c4s3_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c4s3"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 18)

    global next_state
    next_state = test1SG.c4s2
    await manager.dialog().switch_to(test1SG.answer)


async def c4s2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c4s2"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 19)

    global next_state
    next_state = test1SG.c2s2
    await manager.dialog().switch_to(test1SG.answer)


async def c2s2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c2s2"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 20)

    global next_state
    next_state = test1SG.c6s3
    await manager.dialog().switch_to(test1SG.answer)


async def c6s3_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c6s3"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 21)

    global next_state
    next_state = test1SG.c4s1
    await manager.dialog().switch_to(test1SG.answer)


async def c4s1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c4s1"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 22)

    global next_state
    next_state = test1SG.c6s1
    await manager.dialog().switch_to(test1SG.answer)


async def c6s1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c6s1"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 23)

    global next_state
    next_state = test1SG.c2s4
    await manager.dialog().switch_to(test1SG.answer)


async def c2s4_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c2s4"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 24)

    global next_state
    next_state = test1SG.c2s3
    await manager.dialog().switch_to(test1SG.answer)


async def c2s3_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c2s3"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 25)

    global next_state
    next_state = test1SG.c6s4
    await manager.dialog().switch_to(test1SG.answer)


async def c6s4_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c6s4"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 26)

    global next_state
    next_state = test1SG.c7s4
    await manager.dialog().switch_to(test1SG.answer)


async def c7s4_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c7s4"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 27)

    global next_state
    next_state = test1SG.c7s5
    await manager.dialog().switch_to(test1SG.answer)


async def c7s5_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c7s5"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 28)

    global next_state
    next_state = test1SG.c5s5
    await manager.dialog().switch_to(test1SG.answer)


async def c5s5_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c5s5"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 29)

    global next_state
    next_state = test1SG.c8s3
    await manager.dialog().switch_to(test1SG.answer)


async def c8s3_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c8s3"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 30)

    global next_state
    next_state = test1SG.c8s1
    await manager.dialog().switch_to(test1SG.answer)


async def c8s1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c8s1"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 31)

    global next_state
    next_state = test1SG.c8s2
    await manager.dialog().switch_to(test1SG.answer)


async def c8s2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c8s2"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 32)

    global next_state
    next_state = test1SG.c3s4
    await manager.dialog().switch_to(test1SG.answer)


async def c3s4_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["answer_buffer"] = \
        manager.current_context().dialog_data["answer_stuff"][item_id][1]
    manager.current_context().dialog_data["c3s4"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    await get_random_answers(manager, 33)

    global next_state
    next_state = test1SG.c8s4
    await manager.dialog().switch_to(test1SG.answer)


async def c8s4_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    manager.current_context().dialog_data["c8s4"] = manager.current_context().dialog_data["answer_stuff"][item_id][2]

    manager.current_context().dialog_data["end_time"] = datetime.now().strftime("%d-%m-%y %H:%M:%S")

    c1 = ((manager.current_context().dialog_data["c1s1"] + manager.current_context().dialog_data["c1s2"] +
           manager.current_context().dialog_data["c1s3"] + manager.current_context().dialog_data["c1s5"]) / 16 * 100)
    c2 = ((manager.current_context().dialog_data["c2s1"] + manager.current_context().dialog_data["c2s2"] +
           manager.current_context().dialog_data["c2s3"] + manager.current_context().dialog_data["c2s4"]) / 16 * 100)
    c3 = ((manager.current_context().dialog_data["c3s1"] + manager.current_context().dialog_data["c3s2"] +
           manager.current_context().dialog_data["c3s3"] + manager.current_context().dialog_data["c3s4"]) / 16 * 100)
    c4 = ((manager.current_context().dialog_data["c4s1"] + manager.current_context().dialog_data["c4s2"] +
           manager.current_context().dialog_data["c4s3"] + manager.current_context().dialog_data["c4s4"]) / 16 * 100)
    c5 = ((manager.current_context().dialog_data["c5s1"] + manager.current_context().dialog_data["c5s2"] +
           manager.current_context().dialog_data["c5s4"] + manager.current_context().dialog_data["c5s5"]) / 16 * 100)
    c6 = ((manager.current_context().dialog_data["c6s1"] + manager.current_context().dialog_data["c6s2"] +
           manager.current_context().dialog_data["c6s3"] + manager.current_context().dialog_data["c6s4"]) / 16 * 100)
    c7 = ((manager.current_context().dialog_data["c7s2"] + manager.current_context().dialog_data["c7s3"] +
           manager.current_context().dialog_data["c7s4"] + manager.current_context().dialog_data["c7s5"]) / 16 * 100)
    c8 = ((manager.current_context().dialog_data["c8s1"] + manager.current_context().dialog_data["c8s2"] +
           manager.current_context().dialog_data["c8s3"] + manager.current_context().dialog_data["c8s4"]) / 16 * 100)

    await graph(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, user_id=c.from_user.id)

    await MyBot.bot.send_photo(c.from_user.id,
                               open("results_" + str(c.from_user.id) + ".png", "rb"),
                               caption='Поздравляю!\nНа этом внеурочное занятие завершено. Спасибо за твои решения!\n'
                                       'Желаю тебе достичь всех амбициозных целей! Удачи тебе!\n'
                                       f'Время начала теста:\n{manager.current_context().dialog_data["start_time"]}\n'
                                       f'Время окончания теста:\n{manager.current_context().dialog_data["end_time"]}\n'
                                       'Твои результаты:\n'
                                       f'Компетенция №1: {c1}%\n'
                                       f'Компетенция №2: {c2}%\n'
                                       f'Компетенция №3: {c3}%\n'
                                       f'Компетенция №4: {c4}%\n'
                                       f'Компетенция №5: {c5}%\n'
                                       f'Компетенция №6: {c6}%\n'
                                       f'Компетенция №7: {c7}%\n'
                                       f'Компетенция №8: {c8}%\n'
                               )

    await Results.create(user_id=manager.current_context().dialog_data["user_id"],
                         try_num=manager.current_context().dialog_data["try_num"],
                         name=manager.current_context().dialog_data["name"],
                         start_time=manager.current_context().dialog_data["start_time"],
                         end_time=manager.current_context().dialog_data["end_time"],
                         c1=c1,
                         c2=c2,
                         c3=c3,
                         c4=c4,
                         c5=c5,
                         c6=c6,
                         c7=c7,
                         c8=c8)

    os.remove("results_" + str(c.from_user.id) + ".png")

    await manager.done()


test1 = Dialog(
    Window(
        Format("{answer_buffer}"),
        Button(Const("Следующий вопрос ⏩"), id="next_question", on_click=next_question),
        getter=get_data,
        state=test1SG.answer
    ),
    Window(
        Format("Твоя задача провести внеурочное занятие по гандболу\n"
               "<i>для обучающихся 10-11 лет</i>, "
               "этап начальной подготовки. В календарном планировании это занятие No3.\n"
               "<b>Тема «Ведение и бросок мяча»</b>. По списку в группе 20 человек."),
        Button(Const("Начать тест!"), id="start_test", on_click=start_test),
        parse_mode=ParseMode.HTML,
        state=test1SG.introduction
    ),
    Window(
        Jinja("Перед тем как пойдут запланированные 45 минут занятия,"
              "необходимо составить план- конспект предстоящего занятия."
              "Начнём с педагогических задач."
              "Какую из этих задач ты поставишь, как образовательную?\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c1s1",
            on_click=c1s1_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c1s1
    ),
    Window(
        Jinja("Какие упражнения ты выберешь для выполнения этой задачи в основной части занятия?\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c1s2",
            on_click=c1s2_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c1s2
    ),
    Window(
        Jinja("Ты изучил цифровые материалы по обучению броска мяча в гандболе"
              " и решил отправить один из них детям в качестве дополнительного материала.\n"
              "<b>Какую ссылку отправишь?</b>\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c1s1",
            on_click=c5s4_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c5s4
    ),
    Window(
        Jinja("<b>Какой показатель скажет тебе о том, что видео достоверно?</b>\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c1s1",
            on_click=c5s2_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c5s2
    ),
    Window(
        Jinja("Ты решил дать детям в конце тренировки домашнее задание посмотреть подобранные материалы.\n"
              "<b>Каким образом ты донесёшь эту информацию?</b>\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c1s1",
            on_click=c5s1_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c5s1
    ),
    Window(
        Jinja("В план-конспект нужно добавить подвижную игру.\n"
              "<b>Какая из перечисленных больше подходит для детей этого возраста?</b>\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c4s4",
            on_click=c4s4_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c4s4
    ),
    Window(
        Jinja(
            "<b>Тогда в какой форме ты произведёшь сбор данных о том, насколько твои ученики ознакомлены с техникой безопасности на занятии?</b>\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c6s2",
            on_click=c6s2_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c6s2
    ),
    Window(
        Jinja(
            "Итак, на занятие пришло 18 учеников. Все построились в одну шеренгу. Все в спортивной форме. Но тут ты замечаешь, что Петя стоит в грязной уличной обуви."
            "<b>Что будешь делать?</b>\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c7s2",
            on_click=c7s2_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c7s2
    ),
    Window(
        Jinja(
            "С Петей разобрались. Но пока решали вопрос с Петей, остальные стали обсуждать вчерашний матч сборной нашей страны с принципиальным соперником."
            "<b>Что скажешь?</b>\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c7s3",
            on_click=c7s3_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c7s3
    ),
    Window(
        Jinja("Бег\nПора переходить на беговые упражнения!\n"
              "<b>Сколько времени ты отведёшь на упражнения в беге?</b>\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c1s5",
            on_click=c1s5_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c1s5
    ),
    Window(
        Jinja(
            "Бег\nНа последних минутах бега ты замечаешь, что у Гали красные щёки, повышенная потливость, тяжёлое дыхание и нарушенная координация движений.\n"
            "<b>Что будешь делать?</b>\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c1s3",
            on_click=c1s3_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c1s3
    ),
    Window(
        Jinja(
            "Диагностика\n Отлично! Беговые упражнения завершили. Теперь нужно оценить уровень полученной нагрузки.\n"
            "<b>Какой из перечисленных методов диагностики поможет это сделать?</b>\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c3s1",
            on_click=c3s1_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c3s1
    ),
    Window(
        Jinja("Диагностика\n"
              "<b> Как организуешь проведение пульсометрии?</b>\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c3s2_1",
            on_click=c3s2_1_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c3s2_1
    ),
    Window(
        Jinja("Диагностика\n"
              "<b> Как организуешь проведение пульсометрии?</b>\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c3s2_2",
            on_click=c3s2_2_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c3s2_2
    ),
    Window(
        Jinja("Диагностика\n"
              "<b>Какие выводы сделаешь для себя?</b>\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c3s3",
            on_click=c3s3_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c3s3
    ),
    Window(
        Jinja("ОРУ\n"
              "Ты захотел поручить Ване провести 3 упражнения из комплекса ОРУ в подготовительной части занятия."
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c2s1",
            on_click=c2s1_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c2s1
    ),
    Window(
        Jinja("Следующее упражнение на растяжку – из основной стойки сделать наклон и ..."
              "<b>Какое из действий выберешь с учётом возраста занимающихся?</b>\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c4s3",
            on_click=c4s3_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c4s3
    ),
    Window(
        Jinja(
            "Впереди заключительное упражнение в комплексе ОРУ «Упор присев – упор лёжа (прыжком)» по плану- конспекту запланировано 10 повторений. Но ты помнишь, что Костя, Дима, Максим и Оля в прошлый раз легко сделали больше 13 повторений, а Федя, Егор, Вика и Марина с трудом выполнили 5 повторений.\n"
            "<b>Какую дозировку задашь?</b>\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c4s2",
            on_click=c4s2_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c4s2
    ),
    Window(
        Jinja("<b>В какой форме проведешь упражнение перед основной частью занятия?</b>\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c2s2",
            on_click=c2s2_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c2s2
    ),
    Window(
        Jinja("Для выполнения ведения гандбольного мяча тебе необходимо раздать ученикам гандбольные мячи.\n"
              "<b>Каким наиболее эффективным способом ты это сделаешь?</b>\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c6s3",
            on_click=c6s3_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c6s3
    ),
    Window(
        Jinja("<b>Какую из этих фраз произнесешь для объяснения как вести мяч?</b>\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c4s1",
            on_click=c4s1_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c4s1
    ),
    Window(
        Jinja("<b>Какие рекомендации для выполнения броска мяча в стену ты дашь детям?</b>\n"
              "<b>"
              "{% for answer in answer_variants %}"
              "{{answer}}\n"
              "{% endfor %}"
              "</b>"
              ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c6s1",
            on_click=c6s1_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c6s1
    ),
    Window(
        Jinja(
            "К тебе снова подходит Настя и просит дать оценку её действиям при выполнении упражнения (уже, наверное, раз пятый за сегодня)."
            "<b>Каким образом ты повысишь её интерес к занятию?</b>\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c2s4",
            on_click=c2s4_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c2s4
    ),
    Window(
        Jinja(
            "Перед игрой нужно объединиться в команды.\nУченики разделились на 4 команды. 2 команды девочек, 2 – мальчиков. Первая команда девочек надевает зелёные жилетки, вторая команда мальчиков надевает – желтые. Девочки начинают просить поменяться жилетками с мальчиками, так как жёлтые им нравятся больше. А мальчики не хотят меняться.\n"
            "<b>Начинаются крики и ругань. Что будешь делать?</b>\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c2s3",
            on_click=c2s3_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c2s3
    ),
    Window(
        Jinja(
            "Замечаешь, что вратарь атакующей команды висит на перекладине от ворот. Ты останавливаешь игру и обращаешься к вратарю.\n"
            "<b>Твои действия?</b>\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c6s4",
            on_click=c6s4_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c6s4
    ),
    Window(
        Jinja(
            "После занятия к тебе подошла мама Саши. Она утверждает, что её ребенок сильно устаёт.\nИ спрашивает, зачем ты даёшь такую нагрузку на занятиях в таком возрасте?\n"
            "<b>Что ты сделаешь?</b>\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c7s4",
            on_click=c7s4_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c7s4
    ),
    Window(
        Jinja(
            "Через полчаса тебя вызывает завуч на беседу. Мама Саши написала на тебя жалобу на имя директора. Из жалобы следует, что она не согласна с тем, что ребёнок может уставать после занятия.\n"
            "<b>Как будешь выходить из этой ситуации?</b>\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c7s5",
            on_click=c7s5_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c7s5
    ),
    Window(
        Jinja(
            "После беседы с завучем у тебя появилась идея получить обратную связь от родителей по итогам первых трёх занятий. Ты знаешь, что один из самых удобных способов реализации этой идеи – разослать опрос в Google Формы. \n"
            "<b>Какой алгоритм действий выберешь?</b>\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c5s5",
            on_click=c5s5_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c5s5
    ),
    Window(
        Jinja(
            "Входя в зал тебе на глаза попался градусник, который показывает, что температура воздуха в зале сейчас 17 градусов. У тебя возникло сомнение: «Не слишком ли холодно?».\n"
            "<b>Какой документ подскажет тебе, какой должна быть температура в спортивном зале?</b>\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c8s3",
            on_click=c8s3_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c8s3
    ),
    Window(
        Jinja(
            "Подводя итоги занятия, ты понимаешь, что занимающиеся уже хорошо освоили бросок, хотя на разучивание по планированию отводилось два занятия.\n"
            "<b>В какой документ внесешь изменения в первую очередь?</b>\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c8s1",
            on_click=c8s1_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c8s1
    ),
    Window(
        Jinja(
            "Раз уж начали вносить изменения в документы планирования, то необходимо определиться, какое минимальное количество отборочных игр надо провести в этом году в соответствии со стандартом спортивной подготовки по гандболу?\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c8s2",
            on_click=c8s2_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c8s2
    ),
    Window(
        Jinja(
            "Прежде чем с радостью отправиться домой, осталось решить какое домашнее задание дашь после следующего занятия?\n"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c3s4",
            on_click=c3s4_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c3s4
    ),
    Window(
        Jinja(
            "Вот уже вечером, сидя дома, ты узнаешь, что где-то произошёл пожар. И задумываешься: «А что я буду делать при срабатывании пожарной сигнализации на занятии?».\n"
            "<b>В каком документе прописан порядок действий при возникновении пожара?\n</b>"
            "<b>"
            "{% for answer in answer_variants %}"
            "{{answer}}\n"
            "{% endfor %}"
            "</b>"
        ),
        Row(Select(
            Format("{item}"),
            items=["1",
                   "2",
                   "3",
                   "4"],
            item_id_getter=lambda x: x,
            id="c8s4",
            on_click=c8s4_handler,
        )),
        getter=get_data,
        parse_mode=ParseMode.HTML,
        state=test1SG.c8s4
    ),
    launch_mode=LaunchMode.SINGLE_TOP
)

MyBot.register_dialogs(test1)
