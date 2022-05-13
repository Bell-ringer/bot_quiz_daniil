from datetime import datetime

from aiogram.types import CallbackQuery, ParseMode

from aiogram_dialog import ChatEvent
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select, Back, Column, Cancel, Url, SwitchTo, Row
from aiogram_dialog.widgets.text import Format

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message

from aiogram_dialog import Dialog, DialogManager, Window, StartMode
from aiogram_dialog.manager.protocols import LaunchMode
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from bot import MyBot


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


# функция для получения данных из состояний
async def get_data(dialog_manager: DialogManager, **kwargs):
    return {
        'start_time': dialog_manager.current_context().dialog_data.get("start_time", None),
        'end_time': dialog_manager.current_context().dialog_data.get("end_time", None),
        'c1s1': dialog_manager.current_context().dialog_data.get("c1s1", None),
        'c1s2': dialog_manager.current_context().dialog_data.get("c1s2", None),
    }


async def start_test(c: CallbackQuery, button: Button, manager: DialogManager):
    manager.current_context().dialog_data["start_time"] = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    await manager.dialog().switch_to(test1SG.c1s1)


async def c1s1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        await MyBot.bot.send_message(c.from_user.id, "Выбранная тобой задача оказалась воспитательной. "
                                                     "Образовательной же задачей будет «Обучение ведению и броску гандбольного мяча».")
        manager.current_context().dialog_data["c1s1"] = 1
    if item_id == "2":
        await MyBot.bot.send_message(c.from_user.id, "Выбранная тобой задача оказалась оздоровительной. "
                                                     "Образовательной же задачей будет «Обучение ведению и броску гандбольного мяча».")
        manager.current_context().dialog_data["c1s1"] = 2
    if item_id == "3":
        await MyBot.bot.send_message(c.from_user.id,
                                     "Да, это образовательная задача, но она не соответствует третьему занятию по календарному планированию, совершенствовать ещё рано. Лучше подойдёт «Обучение ведению и броску гандбольного мяча».")
        manager.current_context().dialog_data["c1s1"] = 3
    if item_id == "4":
        await MyBot.bot.send_message(c.from_user.id, "Молодец! Эта задача нам подходит!")
        manager.current_context().dialog_data["c1s1"] = 4

    await manager.dialog().switch_to(test1SG.c1s2)


async def c1s2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        await MyBot.bot.send_message(c.from_user.id, "Хм...Пока рано давать эти упражнения. "
                                                     "Они больше подойдут для решения задач по совершенствованию техники ведения и броска мяча. "
                                                     "На этом занятии лучше всего дать упражнения на ведение мяча на месте и бросок мяча в стену с места.")
        manager.current_context().dialog_data["c1s2"] = 1
    if item_id == "2":
        await MyBot.bot.send_message(c.from_user.id, "Хм...Пока рано давать эти упражнения. "
                                                     "Они больше подойдут для решения задач по совершенствованию техники ведения и броска мяча. "
                                                     "На этом занятии лучше всего дать упражнения на ведение мяча на месте и бросок мяча в стену с места.")
        manager.current_context().dialog_data["c1s2"] = 2
    if item_id == "3":
        await MyBot.bot.send_message(c.from_user.id, "Хм...Пока рано давать эти упражнения. "
                                                     "Они больше подойдут для решения задач по совершенствованию техники ведения и броска мяча. "
                                                     "На этом занятии лучше всего дать упражнения на ведение мяча на месте и бросок мяча в стену с места.")
        manager.current_context().dialog_data["c1s2"] = 3
    if item_id == "4":
        await MyBot.bot.send_message(c.from_user.id, "Хм...Пока рано давать эти упражнения. "
                                                     "Они больше подойдут для решения задач по совершенствованию техники ведения и броска мяча. "
                                                     "На этом занятии лучше всего дать упражнения на ведение мяча на месте и бросок мяча в стену с места.")
        manager.current_context().dialog_data["c1s2"] = 4

    await manager.dialog().switch_to(test1SG.c5s4)


async def c5s4_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        await MyBot.bot.send_message(c.from_user.id,
                                     "Ты выбрал электронное методическое пособие, в котором разобрана техника броска гандбольного мяча.")
        manager.current_context().dialog_data["c5s4"] = 1
    if item_id == "2":
        await MyBot.bot.send_message(c.from_user.id,
                                     "Ты выбрал художественный фильм, в котором показана техника броска гандбольного мяча.")
        manager.current_context().dialog_data["c5s4"] = 2
    if item_id == "3":
        await MyBot.bot.send_message(c.from_user.id,
                                     "Ты выбрал приложение «Гандбол 2022», в котором демонстрируется техника броска гандбольного мяча.")
        manager.current_context().dialog_data["c5s4"] = 3
    if item_id == "4":
        await MyBot.bot.send_message(c.from_user.id,
                                     "Ты выбрал видео с официального канала МЭШ на YouTube, в котором разобрана техника броска гандбольного мяча.")
        manager.current_context().dialog_data["c5s4"] = 4

    await manager.dialog().switch_to(test1SG.c5s2)


async def c5s2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c5s2"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c5s2"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c5s2"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c5s2"] = 4

    await manager.dialog().switch_to(test1SG.c5s1)


async def c5s1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c5s1"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c5s1"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c5s1"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c5s1"] = 4

    await MyBot.bot.send_message(c.from_user.id,
                                 "Отлично! С домашним заданием и дополнительными материалами определились. Возвращаемся к плану-конспекту занятия.")

    await manager.dialog().switch_to(test1SG.c4s4)


async def c4s4_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c4s4"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c4s4"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c4s4"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c4s4"] = 4

    await MyBot.bot.send_message(c.from_user.id, "Хм..Хорошо!")

    await manager.dialog().switch_to(test1SG.c6s2)


async def c6s2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c6s2"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c6s2"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c6s2"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c6s2"] = 4

    await MyBot.bot.send_message(c.from_user.id,
                                 "Отлично! С планом-конспектом разобрались, можно приступать к занятию.")

    await manager.dialog().switch_to(test1SG.c7s2)


async def c7s2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        await MyBot.bot.send_message(c.from_user.id,
                                     "Что ж... Решение твоё. Ты поступил, как считаешь нужным. Посмотрим, будут ли какие-то последствия в дальнейшем.")
        manager.current_context().dialog_data["c7s2"] = 1
    if item_id == "2":
        await MyBot.bot.send_message(c.from_user.id,
                                     "Что ж... Решение твоё. Ты поступил, как считаешь нужным. Посмотрим, будут ли какие-то последствия в дальнейшем.")
        manager.current_context().dialog_data["c7s2"] = 2
    if item_id == "3":
        await MyBot.bot.send_message(c.from_user.id,
                                     "Что ж... Решение твоё. Ты поступил, как считаешь нужным. Посмотрим, будут ли какие-то последствия в дальнейшем.")
        manager.current_context().dialog_data["c7s2"] = 3
    if item_id == "4":
        await MyBot.bot.send_message(c.from_user.id,
                                     "Интересное решение! Посмотрим, приведёт ли оно тебя к чему-то в дальнейшем.")
        manager.current_context().dialog_data["c7s2"] = 4

    await manager.dialog().switch_to(test1SG.c7s3)


async def c7s3_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        await MyBot.bot.send_message(c.from_user.id,
                                     "Грубовато...\nНо как знаешь. Пора приступать к бегу.")
        manager.current_context().dialog_data["c7s3"] = 1
    if item_id == "2":
        await MyBot.bot.send_message(c.from_user.id,
                                     "Жёстко. Про “играть не умеют” поспорил бы, но зато побежали. Тогда переходим к бегу.")
        manager.current_context().dialog_data["c7s3"] = 2
    if item_id == "3":
        await MyBot.bot.send_message(c.from_user.id,
                                     "Хорошо. Поддеражали интерес к игре и к себе, только времени много на это ушло. Пора переходить к бегу.")
        manager.current_context().dialog_data["c7s3"] = 3
    if item_id == "4":
        await MyBot.bot.send_message(c.from_user.id,
                                     "Отлично! И время сэкономили, и интерес к игре поддержали. Переходим к бегу.")
        manager.current_context().dialog_data["c7s3"] = 4

    await manager.dialog().switch_to(test1SG.c1s5)


async def c1s5_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c1s5"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c1s5"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c1s5"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c1s5"] = 4

    await manager.dialog().switch_to(test1SG.c1s3)


async def c1s3_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c1s3"] = 1
        await MyBot.bot.send_message(c.from_user.id,
                                     "Хм...Странный выбор...Эти признаки говорят о том, что у Гали повышенная утомляемость. Лучше обратить на это внимание и дать Гале команду перейти на шаг и отправиться в конец колонны.")
    if item_id == "2":
        manager.current_context().dialog_data["c1s3"] = 2
        await MyBot.bot.send_message(c.from_user.id,
                                     "Перечисленные признаки говорят о том, что у Гали повышенная утомляемость. После бега необходимо плавно снижать нагрузку, поэтому нельзя сразу сажать Галю на скамью, а лучше перевести её на шаг и отправить в конец колонны.")
    if item_id == "3":
        manager.current_context().dialog_data["c1s3"] = 3
        await MyBot.bot.send_message(c.from_user.id,
                                     "Да, можно действовать и так, если ты хорошо знаешь особенности Гали. Но так как это всего лишь третье занятие, индивидуальные особенности всех занимающихся выделить практически невозможно. Поэтому лучше всего в данной ситуации перевести Галю на шаг и отправить в конец колонны.")
    if item_id == "4":
        manager.current_context().dialog_data["c1s3"] = 4
        await MyBot.bot.send_message(c.from_user.id,
                                     "Хорошо! Перечисленные признаки говорят о том, что у Гали повышенная утомляемость, поэтому это наиболее подходящий выход из данной ситуации.")

    await manager.dialog().switch_to(test1SG.c3s1)


async def c3s1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c3s1"] = 1
        await MyBot.bot.send_message(c.from_user.id, "Хм...Проба Ромберга...Интересный выбор!")
        await manager.dialog().switch_to(test1SG.c3s2_1)
    if item_id == "2":
        manager.current_context().dialog_data["c3s1"] = 2
        await MyBot.bot.send_message(c.from_user.id,
                                     "Этот метод можно использовать, но в данный момент он не является эффективным, так как дети не всегда могут объективно оценить уровень полученной нагрузки. Наиболее объективным методом из предложенных является пульсометрия. Давай проведём её.")
        await manager.dialog().switch_to(test1SG.c3s2_2)
    if item_id == "3":
        manager.current_context().dialog_data["c3s1"] = 3
        await MyBot.bot.send_message(c.from_user.id,
                                     "Этот метод можно использовать, но мы не всегда можем объективно оценить уровень полученной нагрузки по внешнему виду обучающегося, есть риск не заметить признаки утомления у одного или нескольких учеников. Наиболее объективным методом из предложенных является пульсометрия. Давай проведём её.")
        await manager.dialog().switch_to(test1SG.c3s2_2)
    if item_id == "4":
        manager.current_context().dialog_data["c3s1"] = 4
        await MyBot.bot.send_message(c.from_user.id, "Отлично! Пульсометрия действительно эффективный метод!")
        await manager.dialog().switch_to(test1SG.c3s2_2)


async def c3s2_1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c3s2"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c3s2"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c3s2"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c3s2"] = 4

    await MyBot.bot.send_message(c.from_user.id, "Проведя пробу Ромберга ты решил ещё")
    await MyBot.bot.send_message(c.from_user.id,
                                 "Таким образом получили данные, что в среднем у группы значения ЧСС около 120 уд/мин.")
    await manager.dialog().switch_to(test1SG.c3s3)


async def c3s2_2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c3s2"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c3s2"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c3s2"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c3s2"] = 4

    await MyBot.bot.send_message(c.from_user.id,
                                 "Таким образом получили данные, что в среднем у группы значения ЧСС около 120 уд/мин.")
    await manager.dialog().switch_to(test1SG.c3s3)


async def c3s3_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c3s3"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c3s3"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c3s3"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c3s3"] = 4

    await MyBot.bot.send_message(c.from_user.id,
                                 "Хорошо. Учтёшь эти выводы при дальнейшем планировании тренировочного процесса, а сейчас возвращаемся к занятию. У нас впереди комплекс ОРУ.")
    await manager.dialog().switch_to(test1SG.c2s1)


async def c2s1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c2s1"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c2s1"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c2s1"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c2s1"] = 4

    await MyBot.bot.send_message(c.from_user.id,
                                 "Отлично! Ваня провел свою часть комплекса ОРУ. Все ему поаплодировали. И ты продалажаешь проведение комплекса.")
    await manager.dialog().switch_to(test1SG.c4s3)


async def c4s3_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c4s3"] = 1
        await MyBot.bot.send_message(c.from_user.id,
                                     "Все смогли выполнить, а кто-то даже легко коснулся ладонями и сказал, что это слишком просто.")
    if item_id == "2":
        manager.current_context().dialog_data["c4s3"] = 2
        await MyBot.bot.send_message(c.from_user.id,
                                     "Почти все смогли выполнить, а кто-то даже легко коснулся ладонями и сказал, что это слишком просто.")
    if item_id == "3":
        manager.current_context().dialog_data["c4s3"] = 3
        await MyBot.bot.send_message(c.from_user.id,
                                     "Большинство смогли выполнить, а кто-то даже легко коснулся ладонями и сказал, что это слишком просто.")
    if item_id == "4":
        manager.current_context().dialog_data["c4s3"] = 4
        await MyBot.bot.send_message(c.from_user.id,
                                     "Почти всем далось непросто, а некоторые смогли только пальцами коснуться пола и сказали, что это слишком сложно. Но всем понравилось.")

    await manager.dialog().switch_to(test1SG.c4s2)


async def c4s2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c4s2"] = 1
        await MyBot.bot.send_message(c.from_user.id,
                                     "Федя и Марина сделали по 4 раза и больше не смогли. Для них это много. Надо их взбодрить.")
    if item_id == "2":
        manager.current_context().dialog_data["c4s2"] = 2
        await MyBot.bot.send_message(c.from_user.id,
                                     "Оля и Дима сделали по 12 раз, остальные в среднем по 8, а Егор только 4 раза. Надо учесть это в подготовке к следующему занятию. А сейчас пора переходить к основной части занятия.")
    if item_id == "3":
        manager.current_context().dialog_data["c4s2"] = 3
        await MyBot.bot.send_message(c.from_user.id,
                                     "Вика и Егор выполнили 7 раз, Марина и Федя по 6 - прогресс “на лицо”. Остальные сделали по 10 раз. А Костя и Максим закончили первыми и долго ждали остальных. Надо учесть это в следующий раз. А сейчас пора переходить к основной части занятия.")
    if item_id == "4":
        manager.current_context().dialog_data["c4s2"] = 4
        await MyBot.bot.send_message(c.from_user.id,
                                     "Все справились с заданем.  Можно переходить к основной части занятия.")

    await manager.dialog().switch_to(test1SG.c2s2)


async def c2s2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c2s2"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c2s2"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c2s2"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c2s2"] = 4

    await MyBot.bot.send_message(c.from_user.id,
                                 "Хорошо. Теперь точно можно приступать к основной части занятия. Тем более, что далее по плану ведение гандбольного мяча.")
    await manager.dialog().switch_to(test1SG.c6s3)


async def c6s3_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c6s3"] = 1
        await MyBot.bot.send_message(c.from_user.id,
                                     "Долго, конечно, но зато они уже в одной шеренге. Можно начинать объяснение.")
    if item_id == "2":
        manager.current_context().dialog_data["c6s3"] = 2
        await MyBot.bot.send_message(c.from_user.id,
                                     "Хм... Интересно.\nТеперь их нужно построить в одну шеренгу на расстоянии друг от друга. И начать объяснение")
    if item_id == "3":
        manager.current_context().dialog_data["c6s3"] = 3
        await MyBot.bot.send_message(c.from_user.id,
                                     "Хорошо!\nТеперь их нужно построить в одну шеренгу на расстоянии друг от друга. И начать объяснение.")
    if item_id == "4":
        manager.current_context().dialog_data["c6s3"] = 4
        await MyBot.bot.send_message(c.from_user.id,
                                     "Ловко!\nТеперь их нужно остановить и построить в одну шеренгу на расстоянии друг от друга. И начать объяснение.")

    await manager.dialog().switch_to(test1SG.c4s1)


async def c4s1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c4s1"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c4s1"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c4s1"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c4s1"] = 4

    await MyBot.bot.send_message(c.from_user.id,
                                 "Креативный подход. Переходим к броску гандбольного мяча.")
    await manager.dialog().switch_to(test1SG.c6s1)


async def c6s1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c6s1"] = 1
        await MyBot.bot.send_message(c.from_user.id,
                                     "Маловато инструкций, но тем не менее у занимающихся получилось очень даже неплохо.\nНо тут ...")
    if item_id == "2":
        manager.current_context().dialog_data["c6s1"] = 2
        await MyBot.bot.send_message(c.from_user.id,
                                     "Маловато инструкций, но тем не менее у занимающихся получилось очень даже неплохо.\nНо тут ...")
    if item_id == "3":
        manager.current_context().dialog_data["c6s1"] = 3
        await MyBot.bot.send_message(c.from_user.id,
                                     "Очень качественно.\nПочти у всех хорошо получилось выполнить данное упражнение.\nИ тут...")
    if item_id == "4":
        manager.current_context().dialog_data["c6s1"] = 4
        await MyBot.bot.send_message(c.from_user.id,
                                     "Очень качественно.\nПочти у всех хорошо получилось выполнить данное упражнение.\nИ тут...")

    await manager.dialog().switch_to(test1SG.c2s4)


async def c2s4_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c2s4"] = 1
        await MyBot.bot.send_message(c.from_user.id,
                                     "Сильно.\nНо хоть за что-то уж точно можно было бы похвалить. Ладно продолжаем. Пора играть в гандбол.")
    if item_id == "2":
        manager.current_context().dialog_data["c2s4"] = 2
        await MyBot.bot.send_message(c.from_user.id,
                                     "Хорошо.\nС Настей вопрос решили. Пора играть в гандбол.")
    if item_id == "3":
        manager.current_context().dialog_data["c2s4"] = 3
        await MyBot.bot.send_message(c.from_user.id,
                                     "Хорошо.\nС Настей вопрос решили. Пора играть в гандбол.")
    if item_id == "4":
        manager.current_context().dialog_data["c2s4"] = 4
        await MyBot.bot.send_message(c.from_user.id,
                                     "Хорошо.\nС Настей вопрос решили. Пора играть в гандбол.")

    await manager.dialog().switch_to(test1SG.c2s3)


async def c2s3_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c2s3"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c2s3"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c2s3"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c2s3"] = 4

    await MyBot.bot.send_message(c.from_user.id,
                                 "Так и договорились.\nНачали играть. У детей появился спортивный азарт, идёт хорошая атака и тут ты замечаешь...")
    await manager.dialog().switch_to(test1SG.c6s4)


async def c6s4_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c6s4"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c6s4"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c6s4"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c6s4"] = 4

    await MyBot.bot.send_message(c.from_user.id,
                                 "На этом занятие подходит к концу. Завершили игру. Построились. Подвели итоги занятия. И попрощались.\nНо это ещё не всё!")
    await manager.dialog().switch_to(test1SG.c7s4)


async def c7s4_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c7s4"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c7s4"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c7s4"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c7s4"] = 4

    await manager.dialog().switch_to(test1SG.c7s5)


async def c7s5_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c7s5"] = 1
        await MyBot.bot.send_message(c.from_user.id,
                                     "Хм...Уверенная позиция.\nИнтересно насколько долго получится сотрудничать с администрацией и родителями этого образовательного учреждения.  Но беседа закончилась. Надо возвращаться к себе в кабинет.")
    if item_id == "2":
        manager.current_context().dialog_data["c7s5"] = 2
        await MyBot.bot.send_message(c.from_user.id,
                                     "Интересное решение.\nОднако затратное. Может быть и сработает. Но беседа закончилась. Надо возвращаться к себе в кабинет.")
    if item_id == "3":
        manager.current_context().dialog_data["c7s5"] = 3
        await MyBot.bot.send_message(c.from_user.id,
                                     "Хорошо.\nЕсли администрация всё правильно поняла, то может быть получиться убедить маму Саши. А беседа закончилась. Надо возвращаться к себе в кабинет.")
    if item_id == "4":
        manager.current_context().dialog_data["c7s5"] = 4
        await MyBot.bot.send_message(c.from_user.id,
                                     "Отлично!\nВместе с администрацией всё- таки больше шансов убедить маму Саши.  Беседа закончилась. Надо возвращаться к себе в кабинет.")

    await manager.dialog().switch_to(test1SG.c5s5)


async def c5s5_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c5s5"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c5s5"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c5s5"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c5s5"] = 4

    await MyBot.bot.send_message(c.from_user.id,
                                     "Хорошо.\nТы уже почти пришел в свой кабинет и тут...")
    await manager.dialog().switch_to(test1SG.c8s3)


async def c8s3_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c8s3"] = 1
        await MyBot.bot.send_message(c.from_user.id,
                                     "Нет.\nВсё-таки требования к температуре в спортивном зале прописаны в СанПиН.\nКстати о занятии...")
    if item_id == "2":
        manager.current_context().dialog_data["c8s3"] = 2
        await MyBot.bot.send_message(c.from_user.id,
                                     "Нет.\nВсё-таки требования к температуре в спортивном зале прописаны в СанПиН.\nКстати о занятии...")
    if item_id == "3":
        manager.current_context().dialog_data["c8s3"] = 3
        await MyBot.bot.send_message(c.from_user.id,
                                     "Нет.\nВсё-таки требования к температуре в спортивном зале прописаны в СанПиН.\nКстати о занятии...")
    if item_id == "4":
        manager.current_context().dialog_data["c8s3"] = 4
        await MyBot.bot.send_message(c.from_user.id,
                                     "Да.\nИменно в этом документе прописаны требования к температуре в спортивном зале.\nКстати о занятии...")
    await manager.dialog().switch_to(test1SG.c8s1)


async def c8s1_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c8s1"] = 1
        await MyBot.bot.send_message(c.from_user.id,
                                     "???Нет.\nВсё-таки требования к температуре в спортивном зале прописаны в СанПиН.\nКстати о занятии...")
    if item_id == "2":
        manager.current_context().dialog_data["c8s1"] = 2
        await MyBot.bot.send_message(c.from_user.id,
                                     "???Нет.\nВсё-таки требования к температуре в спортивном зале прописаны в СанПиН.\nКстати о занятии...")
    if item_id == "3":
        manager.current_context().dialog_data["c8s1"] = 3
        await MyBot.bot.send_message(c.from_user.id,
                                     "???Нет.\nВсё-таки требования к температуре в спортивном зале прописаны в СанПиН.\nКстати о занятии...")
    if item_id == "4":
        manager.current_context().dialog_data["c8s1"] = 4
        await MyBot.bot.send_message(c.from_user.id,
                                     "???Да.\nИменно в этом документе прописаны требования к температуре в спортивном зале.\nКстати о занятии...")
    await manager.dialog().switch_to(test1SG.c8s2)


async def c8s2_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c8s2"] = 1
        await MyBot.bot.send_message(c.from_user.id,
                                     "Почти.\nНа самом деле на этапе начальной подготовки не требуется проводить отборочные соревнования.")
    if item_id == "2":
        manager.current_context().dialog_data["c8s2"] = 2
        await MyBot.bot.send_message(c.from_user.id,
                                     "Почти.\nНа самом деле на этапе начальной подготовки не требуется проводить отборочные соревнования.")
    if item_id == "3":
        manager.current_context().dialog_data["c8s2"] = 3
        await MyBot.bot.send_message(c.from_user.id,
                                     "Почти.\nНа самом деле на этапе начальной подготовки не требуется проводить отборочные соревнования.")
    if item_id == "4":
        manager.current_context().dialog_data["c8s2"] = 4
        await MyBot.bot.send_message(c.from_user.id,
                                     "Верно.\nНа этапе начальной подготовки не требуется проводить отборочные соревнования.")
    await manager.dialog().switch_to(test1SG.c3s4)


async def c3s4_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c3s4"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c3s4"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c3s4"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c3s4"] = 4

    await MyBot.bot.send_message(c.from_user.id,
                                 "Хорошо.\nС домашним заданием определились, занятие провели, выводы сделали. Можно отправляться домой.")
    await manager.dialog().switch_to(test1SG.c8s4)


async def c8s4_handler(c: ChatEvent, select: Select, manager: DialogManager, item_id: str):
    if item_id == "1":
        manager.current_context().dialog_data["c8s4"] = 1
    if item_id == "2":
        manager.current_context().dialog_data["c8s4"] = 2
    if item_id == "3":
        manager.current_context().dialog_data["c8s4"] = 3
    if item_id == "4":
        manager.current_context().dialog_data["c8s4"] = 4

    manager.current_context().dialog_data["end_time"] = datetime.now().strftime("%d-%m-%y %H:%M:%S")

    await MyBot.bot.send_message(c.from_user.id,
                                 'Поздравляю!\nНа этом внеурочное занятие завершено. Спасибо за твои решения!\n'
                                 'Желаю тебе достичь всех амбициозных целей! Удачи тебе!\n'
                                 f'Время начала теста:\n{manager.current_context().dialog_data["start_time"]}\n'
                                 f'Время окончания теста:\n{manager.current_context().dialog_data["end_time"]}\n'
                                 'Твои результаты:\n'
                                 f'№1 : {manager.current_context().dialog_data["c1s1"]}\n'
                                 f'№2 : {manager.current_context().dialog_data["c1s2"]}\n'
                                 f'№3 : {manager.current_context().dialog_data["c5s4"]}\n'
                                 f'№4 : {manager.current_context().dialog_data["c5s2"]}\n'
                                 f'№5 : {manager.current_context().dialog_data["c5s1"]}\n'
                                 f'№6 : {manager.current_context().dialog_data["c4s4"]}\n'
                                 f'№7 : {manager.current_context().dialog_data["c6s2"]}\n'
                                 f'№8 : {manager.current_context().dialog_data["c7s2"]}\n'
                                 f'№9 : {manager.current_context().dialog_data["c7s3"]}\n'
                                 f'№10 : {manager.current_context().dialog_data["c1s5"]}\n'
                                 f'№11 : {manager.current_context().dialog_data["c1s3"]}\n'
                                 f'№12 : {manager.current_context().dialog_data["c3s1"]}\n'
                                 f'№13 : {manager.current_context().dialog_data["c3s2"]}\n'
                                 f'№14 : {manager.current_context().dialog_data["c3s3"]}\n'
                                 f'№15 : {manager.current_context().dialog_data["c2s1"]}\n'
                                 f'№16 : {manager.current_context().dialog_data["c4s3"]}\n'
                                 f'№17 : {manager.current_context().dialog_data["c4s2"]}\n'
                                 f'№18 : {manager.current_context().dialog_data["c2s2"]}\n'
                                 f'№19 : {manager.current_context().dialog_data["c6s3"]}\n'
                                 f'№20 : {manager.current_context().dialog_data["c4s1"]}\n'
                                 f'№21 : {manager.current_context().dialog_data["c6s1"]}\n'
                                 f'№22 : {manager.current_context().dialog_data["c2s4"]}\n'
                                 f'№23 : {manager.current_context().dialog_data["c2s3"]}\n'
                                 f'№24 : {manager.current_context().dialog_data["c6s4"]}\n'
                                 f'№25 : {manager.current_context().dialog_data["c7s4"]}\n'
                                 f'№26 : {manager.current_context().dialog_data["c7s5"]}\n'
                                 f'№27:  {manager.current_context().dialog_data["c5s5"]}\n'
                                 f'№28 : {manager.current_context().dialog_data["c8s3"]}\n'
                                 f'№29 : {manager.current_context().dialog_data["c8s1"]}\n'
                                 f'№30 : {manager.current_context().dialog_data["c8s2"]}\n'
                                 f'№31 : {manager.current_context().dialog_data["c3s4"]}\n'
                                 f'№32 : {manager.current_context().dialog_data["c8s4"]}\n'
                                 )
    await manager.done()

test1 = Dialog(
    Window(
        Format("Твоя задача провести внеурочное занятие по гандболу\n"
               "<i>для обучающихся 10-11 лет</i>, "
               "этап начальной подготовки. В календарном планировании это занятие No3.\n"
               "<b>Тема «Ведение и бросок мяча»</b>. По списку в группе 20 человек."),
        Button(Const("Начать тест!"), id="start_test", on_click=start_test),
        Cancel(Const("⏪ Назад")),
        parse_mode=ParseMode.HTML,
        state=test1SG.introduction
    ),
    Window(
        Format("<b>Ситуация №1\n</b>Перед тем как пойдут запланированные 45 минут занятия,"
               "необходимо составить план- конспект предстоящего занятия."
               "Начнём с педагогических задач."
               "Какую из этих задач ты поставишь, как образовательную?\n"
               "<b>1. Способствовать воспитанию чувства ответственности и работы в команде\n"
               "2. Способствовать развитию координационных способностей\n"
               "3. Совершенствование ведения и броска гандбольного мяча\n"
               "4. Обучение ведению и броску гандбольного мяча</b>"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c1s1
    ),
    Window(
        Format("<b>Ситуация №2\n</b>"
               "Какие упражнения ты выберешь для выполнения этой задачи в основной части занятия?\n"
               "<b>"
               "1. Ведение мяча с закрытыми глазами\n"
               "   Бросок мяча в прыжке\n\n"
               "2. Ведение с двумя мячами\n"
               "   Бросок с обманным движением\n\n"
               "3. Ведение мяча в беге\n"
               "   Бросок меча во время движения\n\n"
               "4. Ведение мяча на месте\n"
               "   Бросок мяча в стену с места\n\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c1s2
    ),
    Window(
        Format("<b>Ситуация №3\n</b>"
               "Ты изучил цифровые материалы по обучению броска мяча в гандболе"
               " и решил отправить один из них детям в качестве дополнительного материала.\n"
               "<b>Какую ссылку отправишь?</b>\n"
               "<b>"
               "1. Ссылка на электронное методическое пособие\n"
               "2. Ссылка на художественный фильм\n"
               "3. Ссылка на приложение «Гандбол 2022»\n"
               "4. Ссылка на видео с официального канала МЭШ на YouTube\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c5s4
    ),
    Window(
        Format("<b>Ситуация №4\n</b>"
               "<b>Какой показатель скажет тебе о том, что видео достоверно?</b>\n"
               "<b>"
               "1. Ссылка на научные источники\n"
               "2. Тренерский стаж автора\n"
               "3. Спортивная квалификация автора\n"
               "4. Грамотно подобранная терминология\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c5s2
    ),
    Window(
        Format("<b>Ситуация №5\n</b>"
               "Ты решил дать детям в конце тренировки домашнее задание посмотреть подобранные материалы.\n"
               "<b>Каким образом ты донесёшь эту информацию?</b>\n"
               "<b>"
               "1. Вышлешь одному ученику ссылку и попросишь разослать её остальным\n"
               "2. Вышлешь материалы в родительский чат и скажешь показать его детям\n"
               "3. Скажешь название и попросишь учеников найти и изучить материалы его дома\n"
               "4. После тренировки скажешь ученикам подойти к тебе с телефонами и отсканировать QR-код со ссылкой на материалы\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c5s1
    ),
    Window(
        Format("<b>Ситуация №6\n</b>"
               "В план-конспект нужно добавить подвижную игру.\n"
               "<b>Какая из перечисленных больше подходит для детей этого возраста?</b>\n"
               "<b>"
               "1. «Ногой и головой через ворота»:\n"
               "2 команды перебрасывают мяч через ворота, которые установлены по середине зала."
               " Первая подача ногой, а дальше отбивают головой через ворота. Кто не перебросил – выбывает.\n\n"
               "2. «Тяжелые вышибалы»: "
               "2 команды. Одна команда всем составом встаёт в середину зала."
               " Другая распределяется по двум линиям атаки."
               " Задача выбить всех игроков первой команды тяжелым мячом, который весит 3 кг.\n"
               "3. «Рывок за мячом»:"
               " 2 шеренги по коротким сторонам зала. Рассчитываются по порядку."
               " Тренер кладёт мяч на середину зала, называет номера и по свистку 2 игрока бегут к мячу."
               " Побеждает тот, кто коснётся мяча первым.\n"
               "4. «По наземной мишени»: все строятся в одну шеренгу, каждый с мячом в руках."
               " Необходимо попасть в обруч, который лежит перед воротами. "
               "Бросил, подобрал мяч, вернулся в шеренгу, бросил..."
               " Кто первым попадёт 3 раза?\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c4s4
    ),
    Window(
        Format("<b>Ситуация №7\n</b>"
               "<b>Тогда в какой форме ты произведёшь сбор данных о том, насколько твои ученики ознакомлены с техникой безопасности на занятии?</b>\n"
               "<b>"
               "1. Рассказ непосредственно перед началом игры в гандбол\n"
               "2. Задание на внимание в конце занятия\n"
               "3. Беседа в начале урока\n"
               "4. Игра на внимание в начале урока\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c6s2
    ),
    Window(
        Format("<b>Ситуация №8\n</b>"
               "Итак, на занятие пришло 18 учеников. Все построились в одну шеренгу. Все в спортивной форме. Но тут ты замечаешь, что Петя стоит в грязной уличной обуви."
               "<b>Что будешь делать?</b>\n"
               "<b>"
               "1. Наорёшь на Петю и выгонишь с занятия\n"
               "2. Спросишь у Пети где «сменка» и заставишь заниматься босиком\n"
               "3. Отправишь Петю мыть обувь, а потом подключишь его к работе\n"
               "4. Посадишь Петю на скамью всё занятие наблюдать со стороны\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c7s2
    ),
    Window(
        Format("<b>Ситуация №9\n</b>"
               "С Петей разобрались. Но пока решали вопрос с Петей, остальные стали обсуждать вчерашний матч сборной нашей страны с принципиальным соперником."
               "<b>Что скажешь?</b>\n"
               "<b>"
               "1. «Тишина! Петя, из-за тебя время тратим, так ещё и остальные болтать начинают! Кого выгнать?»\n"
               "2. «Нечего там обсуждать! Играть не умеют всё равно! Беспомощные! Бегом по залу! Молча!»\n"
               "3. Присоединишься к обсуждению. Обсудите игру. Расскажешь истории из своей жизни. Потом продолжишь занятие.\n"
               "4. Присоединишься к обсуждению. Отметишь, что игра была интересной и предложишь продолжить занятие.\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c7s3
    ),
    Window(
        Format("<b>Ситуация №10\n</b>"
               "Бег\nПора переходить на беговые упражнения!\n"
               "<b>Сколько времени ты отведёшь на упражнения в беге?</b>\n"
               "<b>"
               "1. 3 минуты\n"
               "2. 5 минут\n"
               "3. 7 минут\n"
               "4. 10 минут\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c1s5
    ),
    Window(
        Format("<b>Ситуация №11\n</b>"
               "Бег\nНа последних минутах бега ты замечаешь, что у Гали красные щёки, повышенная потливость, тяжёлое дыхание и нарушенная координация движений.\n"
               "<b>Что будешь делать?</b>\n"
               "<b>"
               "1. Продолжишь без дополнительных команд\n"
               "2. Посадишь Галю на скамью\n"
               "3. Скажешь Гале перейти на лёгкий бег\n"
               "4. Скажешь Гале перейти на шаг и отправиться в конец колонны\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c1s3
    ),
    Window(
        Format("<b>Ситуация №12\n</b>"
               "Диагностика\n Отлично! Беговые упражнения завершили. Теперь нужно оценить уровень полученной нагрузки.\n"
               "<b>Какой из перечисленных методов диагностики поможет это сделать?</b>\n"
               "<b>"
               "1. Проба Ромберга\n"
               "2. Вопрос: «Устали или нет ещё?»\n"
               "3. Внешняя оценка степени утомляемости\n"
               "4. Пульсометрия\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c3s1
    ),
    Window(
        Format("<b>Ситуация №13\n</b>"
               "Диагностика\n"
               "<b> Как организуешь проведение пульсометрии?</b>\n"
               "<b>"
               "1. В форме подвижной игры\n"
               "2. В построении в одну шеренгу\n"
               "3. В парах\n"
               "4. В построении уступами\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c3s2_1
    ),
    Window(
        Format("<b>Ситуация №13\n</b>"
               "Диагностика\n"
               "<b> Как организуешь проведение пульсометрии?</b>\n"
               "<b>"
               "1. Замерить каждому лично\n"
               "2. Объединить в группы\n"
               "3. Объединить в пары\n"
               "4. Каждый измеряет себе сам\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c3s2_2
    ),
    Window(
        Format("<b>Ситуация №14\n</b>"
               "Диагностика\n"
               "<b>Какие выводы сделаешь для себя?</b>\n"
               "<b>"
               "1. Нагрузка слишком большая. Подобраны сложные упражнения и темп работы очень высокий. В следующий раз повторю, они уже привыкли будет лучше.\n"
               "2. Нагрузка выше оптимальной. Упражнения простые, но темп слишком высокий. В следующий раз проведу эти же упражнения в спокойном темпе.\n"
               "3. Нагрузка недостаточная. Упражнения подобраны хорошо, но темп оказался низким. В следующий раз увеличу темп.\n"
               "4. Нагрузка оптимальная. Хорошо подобраны упражнения и темп работы. В следующий раз нужно повторить.\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c3s3
    ),
    Window(
        Format("<b>Ситуация №15\n</b>"
               "ОРУ\n"
               "Ты захотел поручить Ване провести 3 упражнения из комплекса ОРУ в подготовительной части занятия."
               "<b>Когда ты предупредишь его о своём поручении?</b>\n"
               "<b>"
               "1. В процессе проведения комплекса ОРУ\n"
               "2. Перед началом комплекса ОРУ\n"
               "3. В начале тренировки\n"
               "4. На прошлой тренировке\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c2s1
    ),
    Window(
        Format("<b>Ситуация №16\n</b>"
               "Следующее упражнение на растяжку – из основной стойки сделать наклон и ..."
               "<b>Какое из действий выберешь с учётом возраста занимающихся?</b>\n"
               "<b>"
               "1. Коснуться кроссовок\n"
               "2. Коснуться пола кончиками пальцев\n"
               "3. Коснуться пола кулачками\n"
               "4. Коснуться пола ладонями\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c4s3
    ),
    Window(
        Format("<b>Ситуация №17\n</b>"
               "Впереди заключительное упражнение в комплексе ОРУ «Упор присев – упор лёжа (прыжком)» по плану- конспекту запланировано 10 повторений. Но ты помнишь, что Костя, Дима, Максим и Оля в прошлый раз легко сделали больше 13 повторений, а Федя, Егор, Вика и Марина с трудом выполнили 5 повторений.\n"
               "<b>Какую дозировку задашь?</b>\n"
               "<b>"
               "1. «Всем сделать 10 повторений. Начали!»\n"
               "2. «Даю вам 15 секунд. Кто сделает больше всех?! Начали!»\n"
               "3. «Всем сделать 10 повторений. Федя, Егор, Вика и Марина, Вам хотя бы 7 раз. Начали!»\n"
               "4. «Всем сделать 10 повторений. Костя, Дима, Максим и Оля, Вам 15. Федя, Егор, Вика и Марина, Вам 7. Начали!»\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c4s2
    ),
    Window(
        Format("<b>Ситуация №18\n</b>"
               "<b>В какой форме проведешь упражнение перед основной частью занятия?</b>\n"
               "<b>"
               "1. Проведение упражнения без эмоционального фона. «Выполняем подскоки под счёт 1-4»\n"
               "2. Проведение упражнения с высоким эмоциональным фоном «Прыжки на месте и выкрикнуть своё имя»\n"
               "3. Проведение подвижной игры без сюжета «Пробежать через линию»\n"
               "4. Проведение подвижной сюжетно-ролевой игры «Два Мороза»\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c2s2
    ),
    Window(
        Format("<b>Ситуация №19\n</b>"
               "Для выполнения ведения гандбольного мяча тебе необходимо раздать ученикам гандбольные мячи.\n"
               "<b>Каким наиболее эффективным способом ты это сделаешь?</b>\n"
               "<b>"
               "1. Построишь в шеренгу и будешь лично раздавать каждому по мячу\n"
               "2. Распределишь всех ребят по рабочим местам и раздашь каждому по мячу\n"
               "3. В начале урока выберешь 2–3 дежурных, которые всем раздадут мячи\n"
               "4. В процессе движения, когда они будут проходить мимо тебя, раздашь им мячи\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c6s3
    ),
    Window(
        Format("<b>Ситуация №20\n</b>"
               "<b>Какую из этих фраз произнесешь для объяснения как вести мяч?</b>\n"
               "<b>"
               "1. Выгуливаем нашего Колобка по тропинке\n"
               "2. Ведём мяч по прямой\n"
               "3. Ведём Колобка по прямой\n"
               "4. Ведём мяч по тропинке\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c4s1
    ),
    Window(
        Format("<b>Ситуация №21\n</b>"
               "<b>Какие рекомендации для выполнения броска мяча в стену ты дашь детям?</b>\n"
               "<b>"
               "1. Расстояние на которые необходимо отойти от партнёра и от мишени и укажешь куда точно нужно бросать мяч\n"
               "2. Укажешь расстояние до мишени и между партнёром, четко обозначишь мишень и запретишь бросать куда-либо ещё\n"
               "3. Укажешь расстояние до мишени и между партнёрами, четко обозначишь мишень и запретишь направлять мяч куда-либо ещё, дашь команду работать по свистку тренера\n"
               "4. Перед началом выполнения упражнения проведешь опрос о технике безопасности и дополнишь их ответы своими рекомендациями к выполнению упражнения на основе предыдущих занятий\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c6s1
    ),
    Window(
        Format("<b>Ситуация №22\n</b>"
               "К тебе снова подходит Настя и просит дать оценку её действиям при выполнении упражнения (уже, наверное, раз пятый за сегодня)."
               "<b>Каким образом ты повысишь её интерес к занятию?</b>\n"
               "<b>"
               "1. Не хвалить, сказать, что она может лучше\n"
               "2. Похвалить, не акцентируя внимания на недочётах\n"
               "3. Укажешь расстояние до мишени и между партнёрами, четко обозначишь мишень и запретишь направлять мяч куда-либо ещё, дашь команду работать по свистку тренера\n"
               "4. ???\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c2s4
    ),
    Window(
        Format("<b>Ситуация №23\n</b>"
               "Перед игрой нужно объединиться в команды.\nУченики разделились на 4 команды. 2 команды девочек, 2 – мальчиков. Первая команда девочек надевает зелёные жилетки, вторая команда мальчиков надевает – желтые. Девочки начинают просить поменяться жилетками с мальчиками, так как жёлтые им нравятся больше. А мальчики не хотят меняться.\n"
               "<b>Начинаются крики и ругань. Что будешь делать?</b>\n"
               "<b>"
               "1. Сказать, что это моё решение, и оно неизменно\n"
               "2. Попросить мальчиков быть джентельменами и уступить девочкам\n"
               "3. Выделить двух капитанов и пускай они решат на «Камень. Ножницы. Бумага»\n"
               "4. Сказать, что сегодня так, а в следующий раз девочки наденут жёлтые жилетки\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c2s3
    ),
    Window(
        Format("<b>Ситуация №24\n</b>"
               "Замечаешь, что вратарь атакующей команды висит на перекладине от ворот. Ты останавливаешь игру и обращаешься к вратарю.\n"
               "<b>Твои действия?</b>\n"
               "<b>"
               "1. Скажешь слезть и заставишь его делать 10 отжиманий\n"
               "2. Скажешь слезть и сделаешь его полевым игроком\n"
               "3. Скажешь слезть и посадишь его на скамейку\n"
               "4. Скажешь слезть и проведешь с ним беседу\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c6s4
    ),
    Window(
        Format("<b>Ситуация №25\n</b>"
               "После занятия к тебе подошла мама Саши. Она утверждает, что её ребенок сильно устаёт.\nИ спрашивает, зачем ты даёшь такую нагрузку на занятиях в таком возрасте?\n"
               "<b>Что ты сделаешь?</b>\n"
               "<b>"
               "1. Скажешь ей: «Если Вас что- то не устраивает, то обращайтесь к администрации.»\n"
               "2. Скажешь ей: «Усталость – это нормально, ребёнок должен уставать. Я знаю это лучше Вас. Всё-таки не первый день с детьми работаю.»\n"
               "3. Пригласишь её на следующее занятие, чтобы она понаблюдала, как проходит занятие и чем дети занимаются.\n"
               "4. Скажешь, что этот вопрос уже задавали, поэтому придешь на родительское собрание и расскажешь всем, как влияют физические упражнения на организм ребёнка.\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c7s4
    ),
    Window(
        Format("<b>Ситуация №26\n</b>"
               "Через полчаса тебя вызывает завуч на беседу. Мама Саши написала на тебя жалобу на имя директора. Из жалобы следует, что она не согласна с тем, что ребёнок может уставать после занятия.\n"
               "<b>Как будешь выходить из этой ситуации?</b>\n"
               "<b>"
               "1. ???\n"
               "2. Скажешь: «Вот вам тортик. Решите, пожалуйста, эту проблему без моего участия.»\n"
               "3. Обоснуешь администрации правильность своих действий, чтобы они сами объяснили это родителю.\n"
               "4. Объяснишь администрации правильность своих действий. И вместе с представителем администрации встретишься с родителем.\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c7s5
    ),
    Window(
        Format("<b>Ситуация №27\n</b>"
               "После беседы с завучем у тебя появилась идея получить обратную связь от родителей по итогам первых трёх занятий. Ты знаешь, что один из самых удобных способов реализации этой идеи – разослать опрос в Google Формы. \n"
               "<b>Какой алгоритм действий выберешь?</b>\n"
               "<b>"
               "1. Напишешь название опроса -> Объяснишь для чего он нужен и сколько времени займёт -> Попросишь указать группу и возраст детей -> Составишь 5 вопросов -> Внесёшь вопросы в Google Формы -> Отправишь ссылку на опрос в мессенджере каждому родителю лично -> Соберешь статистику и сделаешь выводы\n"
               "2. Напишешь название опроса -> Объяснишь для чего он нужен и сколько времени займёт -> Попросишь указать группу и возраст детей -> Потребуешь указать личные данные -> Составишь 7 вопросов -> Внесёшь вопросы в Google Формы -> Отправишь ссылку на опрос в общую группу в мессенджере -> Соберешь статистику и сделаешь выводы\n"
               "3. Напишешь название опроса -> Попросишь указать группу и возраст детей -> Потребуешь указать личные данные -> Составишь 5 вопросов -> Внесёшь вопросы в Google Формы -> Отправишь ссылку на опрос в общую группу в мессенджере -> Соберешь статистику\n"
               "4. Напишешь название опроса -> Попросишь указать группу и возраст детей -> Потребуешь указать личные данные -> Составишь 15 вопросов -> Внесёшь вопросы в Google Формы -> Отправишь ссылку на опрос по почте каждому родителю лично -> Соберешь статистику\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c5s5
    ),
    Window(
        Format("<b>Ситуация №28\n</b>"
               "Входя в зал тебе на глаза попался градусник, который показывает, что температура воздуха в зале сейчас 17 градусов. У тебя возникло сомнение: «Не слишком ли холодно?».\n"
               "<b>Какой документ подскажет тебе, какой должна быть температура в спортивном зале?</b>\n"
               "<b>"
               "1. Федеральный закон «Об образовании в Российской Федерации» от 29.12.2012 No273-ФЗ\n"
               "2. Федеральный закон «О физической культуре и спорте в Российской Федерации» от 04.12.2007 No329-ФЗ\n"
               '3. Приказ Минспорта России от 30.06.2021 No485 «Об утверждении федерального стандарта спортивной подготовки по виду спорта "гандбол"»\n'
               "4. СанПиН 2.4.2.2821-10 «Санитарно-эпидемиологические требования к условиям и организации обучения в общеобразовательных учреждениях»\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c8s3
    ),
    Window(
        Format("<b>Ситуация №29\n</b>"
               "Подводя итоги занятия, ты понимаешь, что занимающиеся уже хорошо освоили бросок, хотя на разучивание по планированию отводилось два занятия.\n"
               "<b>В какой документ внесешь изменения в первую очередь?</b>\n"
               "<b>"
               "1. Учебная программа\n"
               "2. План подготовки к соревнованиям\n"
               '3. План-график годичного цикла\n'
               "4. План-конспект следующего тренировочного занятия\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c8s1
    ),
    Window(
        Format("<b>Ситуация №30\n</b>"
               "Раз уж начали вносить изменения в документы планирования, то необходимо определиться, какое минимальное количество отборочных игр надо провести в этом году в соответствии со стандартом спортивной подготовки по гандболу?\n"
               "<b>"
               "1. 3\n"
               "2. 2\n"
               '3. 1\n'
               "4. 0\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c8s2
    ),
    Window(
        Format("<b>Ситуация №31\n</b>"
               "Прежде чем с радостью отправиться домой, осталось решить какое домашнее задание дашь после следующего занятия?\n"
               "<b>"
               "1. Установить приложение «Калькулятор калорий» — отчитаться на следующем занятии\n"
               "2. Установить приложение «Шагомер» — присылать скриншоты тебе в мессенджер\n"
               '3. Отправлять каждый вечер тебе Гугл форму\n'
               "4. Использовать приложение «Личный дневник» (Режим дня: часы сна, часы приёмов пищи, часы занятий физической активностью)\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c3s4
    ),
    Window(
        Format("<b>Ситуация №32\n</b>"
               "Вот уже вечером, сидя дома, ты узнаешь, что где-то произошёл пожар. И задумываешься: «А что я буду делать при срабатывании пожарной сигнализации на занятии?».\n"
               "<b>В каком документе прописан порядок действий при возникновении пожара?\n</b>"
               "<b>"
               "1. Декларация пожарной безопасности образовательной организации\n"
               "2. Устав образовательной организации\n"
               '3. Приказ МЧС Р «Об утверждении норм пожарной безопасности»\n'
               "4. План действий администрации и работников образовательной организации в случае пожара\n"
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
        parse_mode=ParseMode.HTML,
        state=test1SG.c8s4
    ),
    launch_mode=LaunchMode.SINGLE_TOP
)

MyBot.register_dialogs(test1)
