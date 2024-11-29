from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon import LEXICON
from data.requests import add_category1, add_category2, add_category3, add_category4, add_category5, add_answer, delete_category1, delete_answer, delete_category2, delete_category3, delete_category4, delete_category5
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
import keyboards.keyboards as kb
import data.requests as rq
from dotenv import load_dotenv
import os


router = Router()
load_dotenv()

class FSMFillForm(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодействия с пользователем
    cat1 = State()        # Состояние ожидания ввода имени
    cat2 = State()         # Состояние ожидания ввода возраста
    cat3 = State()      # Состояние ожидания выбора пола
    cat4 = State()     # Состояние ожидания загрузки фото
    cat5 = State()   # Состояние ожидания выбора образования
    cat6 = State()
    dcat1 = State()        # Состояние ожидания ввода имени
    dcat2 = State()         # Состояние ожидания ввода возраста
    dcat3 = State()      # Состояние ожидания выбора пола
    dcat4 = State()     # Состояние ожидания загрузки фото
    dcat5 = State()   # Состояние ожидания выбора образования
    dcat6 = State()
# Этот хэндлер будет срабатывать на команду "/start"
@router.message(CommandStart())
async def process_start_command(message: Message):
    print("Обрабатываем команду /start")
    await message.answer(LEXICON[message.text], reply_markup=await kb.categories1())
    if str(message.from_user.id) == os.getenv('ADMIN_IDS'):
        print("Пользователь авторизован как администратор")
        await message.answer('Вы авторизовались как администратор!', reply_markup=await kb.adminp())


@router.callback_query(F.data.startswith('category1_'))
async def category(callback: CallbackQuery):
    await callback.message.answer('Выберите тему вопроса',
                                  reply_markup=await kb.categories2(callback.data.split('_')[1]))

@router.callback_query(F.data.startswith('category2_'))
async def category(callback: CallbackQuery):

    await callback.message.answer('Выберите тему вопроса',
                                  reply_markup=await kb.categories3(callback.data.split('_')[1]))

@router.callback_query(F.data.startswith('category3_'))
async def category(callback: CallbackQuery):

    await callback.message.answer('Выберите тему вопроса',
                                  reply_markup=await kb.categories4(callback.data.split('_')[1]))

@router.callback_query(F.data.startswith('category4_'))
async def category(callback: CallbackQuery):
    await callback.message.answer('Выберите вопрос',
                                  reply_markup=await kb.categories5(callback.data.split('_')[1]))

@router.callback_query(F.data.startswith('category5_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_category_answer(callback.data.split('_')[1])
    await callback.message.answer(f'Ответ: {item_data.description}',
                                  reply_markup=await kb.answrs(callback.data.split('_')[1]))



@router.callback_query(F.data.startswith('to_main'))
async def answr(callback: CallbackQuery):
    await callback.message.answer('Выберите тему вопроса',
                                  reply_markup=await kb.categories1())

@router.callback_query(F.data.startswith('add'))
async def addcat(callback: CallbackQuery):
    await callback.message.answer('Выберите уровень раздела',
                                  reply_markup=await kb.addcategory())

@router.callback_query(F.data.startswith('l1'))
async def namecat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Введите название раздела')
    await state.set_state(FSMFillForm.cat1)

@router.message(FSMFillForm.cat1)
async def nam(message: Message, state: FSMContext):
    name = message.text
    await add_category1(name)
    await state.clear()
    await message.answer('Раздел добавлен!')

@router.callback_query(F.data.startswith('l2'))
async def namecat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Выберите раздел, в котором хотите добавить подраздел.\nНапишите в формате "id раздела","название нового подраздела" без пробела.\nНапример: "1,подраздел 1"',
                                  reply_markup=await kb.addcategories1())
    await state.set_state(FSMFillForm.cat2)


@router.message(FSMFillForm.cat2)
async def nam(message: Message, state: FSMContext):
    name = message.text.split(',',1)[1]
    category = message.text.split(',')[0]
    await add_category2(category, name)
    await state.clear()
    await message.answer('Раздел добавлен!')

@router.callback_query(F.data.startswith('l3'))
async def namecat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Выберите раздел, в котором хотите добавить подраздел.\nНапишите в формате "id раздела","название нового подраздела" без пробела.\nНапример: "1,подраздел 1"',
                                  reply_markup=await kb.addcategories2())
    await state.set_state(FSMFillForm.cat3)


@router.message(FSMFillForm.cat3)
async def nam(message: Message, state: FSMContext):
    name = message.text.split(',',1)[1]
    category = message.text.split(',')[0]
    await add_category3(category, name)
    await state.clear()
    await message.answer('Раздел добавлен!')

@router.callback_query(F.data.startswith('l4'))
async def namecat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Выберите раздел, в котором хотите добавить подраздел.\nНапишите в формате "id раздела","название нового подраздела" без пробела.\nНапример: "1,подраздел 1"',
                                  reply_markup=await kb.addcategories3())
    await state.set_state(FSMFillForm.cat4)


@router.message(FSMFillForm.cat4)
async def nam(message: Message, state: FSMContext):
    name = message.text.split(',',1)[1]
    category = message.text.split(',')[0]
    await add_category4(category, name)
    await state.clear()
    await message.answer('Раздел добавлен!')

@router.callback_query(F.data.startswith('l5'))
async def namecat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Выберите раздел, в котором хотите добавить вопрос.\nНапишите в формате "id раздела","вопрос" без пробела.\nНапример: "1,вопрос 1"',
                                  reply_markup=await kb.addcategories4())
    await state.set_state(FSMFillForm.cat5)


@router.message(FSMFillForm.cat5)
async def nam(message: Message, state: FSMContext):
    name = message.text.split(',',1)[1]
    category = message.text.split(',')[0]
    await add_category5(category, name)
    await state.clear()
    await message.answer('Вопрос добавлен!')

@router.callback_query(F.data.startswith('l6'))
async def namecat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Выберите вопрос, на который хотите добавить ответ.\nНапишите в формате "id вопроса","текст ответа" без пробела.\nНапример: "1,ответ 1"',
                                  reply_markup=await kb.addcategories5())
    await state.set_state(FSMFillForm.cat6)


@router.message(FSMFillForm.cat6)
async def nam(message: Message, state: FSMContext):
    text = message.text.split(',',1)[1]
    category = message.text.split(',')[0]
    await add_answer(category, text)
    await state.clear()
    await message.answer('Ответ добавлен!')



@router.callback_query(F.data.startswith('del'))
async def addcat(callback: CallbackQuery):
    await callback.message.answer('Выберите раздел',
                                  reply_markup=await kb.delcategory())




@router.callback_query(F.data.startswith('dl1'))
async def namecat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Напишите id раздела, который хотите удалить',
                                  reply_markup=await kb.delcategories1())
    await state.set_state(FSMFillForm.dcat1)


@router.message(FSMFillForm.dcat1)
async def nam(message: Message, state: FSMContext):
    name = message.text
    await delete_category1(name)
    await state.clear()
    await message.answer('Раздел удален!')



@router.callback_query(F.data.startswith('dl2'))
async def namecat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Напишите id подраздела, который хотите удалить',
                                  reply_markup=await kb.delcategories2())
    await state.set_state(FSMFillForm.dcat2)

@router.message(FSMFillForm.dcat2)
async def nam(message: Message, state: FSMContext):
    name = message.text
    await delete_category2(name)
    await state.clear()
    await message.answer('Подраздел удален!')

@router.callback_query(F.data.startswith('dl3'))
async def namecat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Напишите id подраздела, который хотите удалить',
                                  reply_markup=await kb.delcategories3())
    await state.set_state(FSMFillForm.dcat3)



@router.message(FSMFillForm.dcat3)
async def nam(message: Message, state: FSMContext):
    name = message.text
    await delete_category3(name)
    await state.clear()
    await message.answer('Подраздел удален!')

@router.callback_query(F.data.startswith('dl4'))
async def namecat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Напишите id подраздела, который хотите удалить',
                                  reply_markup=await kb.delcategories4())
    await state.set_state(FSMFillForm.dcat4)


@router.message(FSMFillForm.dcat4)
async def nam(message: Message, state: FSMContext):
    name = message.text
    await delete_category4(name)
    await state.clear()
    await message.answer('Подраздел удален!')

@router.callback_query(F.data.startswith('dl5'))
async def namecat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Напишите id вопроса, который хотите удалить',
                                  reply_markup=await kb.delcategories5())
    await state.set_state(FSMFillForm.dcat5)


@router.message(FSMFillForm.dcat5)
async def nam(message: Message, state: FSMContext):
    name = message.text
    await delete_category5(name)
    await state.clear()
    await message.answer('Вопрос удален!')

@router.callback_query(F.data.startswith('dl6'))
async def namecat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Напишите id ответа, который хотите удалить',
                                  reply_markup=await kb.delcategories6())
    await state.set_state(FSMFillForm.dcat6)


@router.message(FSMFillForm.dcat6)
async def nam(message: Message, state: FSMContext):
    name = message.text
    await delete_answer(name)
    await state.clear()
    await message.answer('Ответ удален!')