from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.requests import get_categories1, get_categories2, get_categories3, get_categories4, get_categories5, get_answers, get_category12, get_category23, get_category34, get_category45, get_category_answer, get_categories2a, get_categories3a, get_categories4a, get_categories5a, get_categories6a



async def categories1():
    all_categories = await get_categories1()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category1_{category.id}"))
    return keyboard.adjust(1).as_markup()


async def categories2(category1_id):
    all_categories = await get_category12(category1_id)
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category2_{category.id}"))
    keyboard.add(InlineKeyboardButton(text='Посмотрите ответы на другие вопросы', callback_data='to_main'))
    return keyboard.adjust(1).as_markup()

async def categories3(category2_id):
    all_categories = await get_category23(category2_id)
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category3_{category.id}"))
    keyboard.add(InlineKeyboardButton(text='Посмотрите ответы на другие вопросы', callback_data='to_main'))
    return keyboard.adjust(1).as_markup()

async def categories4(category3_id):
    all_categories = await get_category34(category3_id)
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category4_{category.id}"))
    keyboard.add(InlineKeyboardButton(text='Посмотрите ответы на другие вопросы', callback_data='to_main'))
    return keyboard.adjust(1).as_markup()

async def categories5(category4_id):
    all_categories = await get_category45(category4_id)
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category5_{category.id}"))
    keyboard.add(InlineKeyboardButton(text='Посмотрите ответы на другие вопросы', callback_data='to_main'))
    return keyboard.adjust(1).as_markup()

async def answrs(category5_id):
    all_answers= await get_category_answer(category5_id)
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Посмотрите ответы на другие вопросы', callback_data='to_main'))
    return keyboard.adjust(1).as_markup()


async def adminp():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Добавить', callback_data='add'))
    keyboard.add(InlineKeyboardButton(text='Удалить❌', callback_data='del'))
    return keyboard.adjust(1).as_markup()

async def addcategory():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Уровень 1', callback_data='l1'))
    keyboard.add(InlineKeyboardButton(text='Уровень 2', callback_data='l2'))
    keyboard.add(InlineKeyboardButton(text='Уровень 3', callback_data='l3'))
    keyboard.add(InlineKeyboardButton(text='Уровень 4', callback_data='l4'))
    keyboard.add(InlineKeyboardButton(text='Уровень 5(Вопросы)', callback_data='l5'))
    keyboard.add(InlineKeyboardButton(text='Уровень 6(Ответы)', callback_data='l6'))
    return keyboard.adjust(2).as_markup()

async def addcategories1():
    all_categories = await get_categories1()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=f'id:{category.id}, название:{category.name}', callback_data=f"category1*{category.id}"))
    return keyboard.adjust(1).as_markup()

async def addcategories2():
    all_categories = await get_categories2a()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=f'id:{category.id}, название:{category.name}', callback_data=f"category2*{category.id}"))
    return keyboard.adjust(1).as_markup()

async def addcategories3():
    all_categories = await get_categories3a()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=f'id:{category.id}, название:{category.name}', callback_data=f"category3*{category.id}"))
    return keyboard.adjust(1).as_markup()

async def addcategories4():
    all_categories = await get_categories4a()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=f'id:{category.id}, название:{category.name}', callback_data=f"category4*{category.id}"))
    return keyboard.adjust(1).as_markup()

async def addcategories5():
    all_categories = await get_categories5a()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=f'id:{category.id}, название:{category.name}', callback_data=f"category5*{category.id}"))
    return keyboard.adjust(1).as_markup()

async def addcategories6():
    all_categories = await get_categories6a()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=f'id:{category.id}, название:{category.name}', callback_data=f"category5*{category.id}"))
    return keyboard.adjust(1).as_markup()


async def delcategory():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Уровень 1', callback_data='dl1'))
    keyboard.add(InlineKeyboardButton(text='Уровень 2', callback_data='dl2'))
    keyboard.add(InlineKeyboardButton(text='Уровень 3', callback_data='dl3'))
    keyboard.add(InlineKeyboardButton(text='Уровень 4', callback_data='dl4'))
    keyboard.add(InlineKeyboardButton(text='Уровень 5(Вопросы)', callback_data='dl5'))
    keyboard.add(InlineKeyboardButton(text='Уровень 6(Ответы)', callback_data='dl6'))
    return keyboard.adjust(2).as_markup()

async def delcategories1():
    all_categories = await get_categories1()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=f'id:{category.id}, название:{category.name}', callback_data=f"category1+*{category.id}"))
    return keyboard.adjust(1).as_markup()

async def delcategories2():
    all_categories = await get_categories2a()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=f'id:{category.id}, название:{category.name}', callback_data=f"category2+*{category.id}"))
    return keyboard.adjust(1).as_markup()

async def delcategories3():
    all_categories = await get_categories3a()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=f'id:{category.id}, название:{category.name}', callback_data=f"category3+*{category.id}"))
    return keyboard.adjust(1).as_markup()

async def delcategories4():
    all_categories = await get_categories4a()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=f'id:{category.id}, название:{category.name}', callback_data=f"category4+*{category.id}"))
    return keyboard.adjust(1).as_markup()

async def delcategories5():
    all_categories = await get_categories5a()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=f'id:{category.id}, название:{category.name}', callback_data=f"category5+*{category.id}"))
    return keyboard.adjust(1).as_markup()

async def delcategories6():
    all_categories = await get_categories6a()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=f'id:{category.id}, название:{category.description}', callback_data=f"category6+*{category.id}"))
    return keyboard.adjust(1).as_markup()