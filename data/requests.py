from data.models import async_session
from data.models import Category1, Category2, Category3, Category4, Category5, Answer
from sqlalchemy import select

async def get_categories1():
    async with async_session() as session:
        return await session.scalars(select(Category1))

async def get_category12(category1_id):
    async with async_session() as session:
        return await session.scalars(select(Category2).where(Category2.category == category1_id))

async def get_categories2(category2_id):
    async with async_session() as session:
        return await session.scalars(select(Category2).where(Category2.id == category2_id))

async def get_category23(category2_id):
    async with async_session() as session:
        return await session.scalars(select(Category3).where(Category3.category == category2_id))

async def get_categories3(category3_id):
    async with async_session() as session:
        return await session.scalars(select(Category3).where(Category3.id == category3_id))

async def get_category34(category3_id):
    async with async_session() as session:
        return await session.scalars(select(Category4).where(Category4.category == category3_id))

async def get_categories4(category4_id):
    async with async_session() as session:
        return await session.scalars(select(Category4).where(Category4.id == category4_id))

async def get_category45(category4_id):
    async with async_session() as session:
        return await session.scalars(select(Category5).where(Category5.category == category4_id))

async def get_categories5(category5_id):
    async with async_session() as session:
        return await session.scalars(select(Category5).where(Category5.id == category5_id))

async def get_category_answer(category5_id):
    async with async_session() as session:
        return await session.scalar(select(Answer).where(Answer.category == category5_id))

async def get_answers(answr_id):
    async with async_session() as session:
        return await session.scalar(select(Answer).where(Answer.id == answr_id))




async def get_categories2a():
    async with async_session() as session:
        return await session.scalars(select(Category2))

async def get_categories3a():
    async with async_session() as session:
        return await session.scalars(select(Category3))

async def get_categories4a():
    async with async_session() as session:
        return await session.scalars(select(Category4))

async def get_categories5a():
    async with async_session() as session:
        return await session.scalars(select(Category5))

async def get_categories6a():
    async with async_session() as session:
        return await session.scalars(select(Answer))

# Добавление новой категории в Category1
async def add_category1(name: str):
    async with async_session() as session:
        category = Category1(name=name)
        session.add(category)
        await session.commit()  # Сохраняем изменения
        return category  # Можно вернуть добавленную категорию

# Добавление новой категории в Category2
async def add_category2(category1_id: int, name: str):
    async with async_session() as session:
        category2 = Category2(category=category1_id, name=name)
        session.add(category2)
        await session.commit()
        return category2

# Добавление новой категории в Category3
async def add_category3(category2_id: int, name: str):
    async with async_session() as session:
        category3 = Category3(category=category2_id, name=name)
        session.add(category3)
        await session.commit()
        return category3

# Добавление новой категории в Category4
async def add_category4(category3_id: int, name: str):
    async with async_session() as session:
        category4 = Category4(category=category3_id, name=name)
        session.add(category4)
        await session.commit()
        return category4

# Добавление новой категории в Category5
async def add_category5(category4_id: int, name: str):
    async with async_session() as session:
        category5 = Category5(category=category4_id, name=name)
        session.add(category5)
        await session.commit()
        return category5

# Добавление нового ответа в таблицу Answer
async def add_answer(category5_id: int, text: str):
    async with async_session() as session:
        answer = Answer(category=category5_id, description=text)
        session.add(answer)
        await session.commit()
        return answer



# Функция для удаления категории из таблицы Category1 по ID
async def delete_category1(category_id: int):
    async with async_session() as session:
        category = await session.get(Category1, category_id)  # Получаем категорию по ID
        if category:
            await session.delete(category)  # Удаляем категорию
            await session.commit()

# Функция для удаления категории из таблицы Category2 по ID
async def delete_category2(category_id: int):
    async with async_session() as session:
        category = await session.get(Category2, category_id)
        if category:
            await session.delete(category)
            await session.commit()

# Функция для удаления категории из таблицы Category3 по ID
async def delete_category3(category_id: int):
    async with async_session() as session:
        category = await session.get(Category3, category_id)
        if category:
            await session.delete(category)
            await session.commit()

# Функция для удаления категории из таблицы Category4 по ID
async def delete_category4(category_id: int):
    async with async_session() as session:
        category = await session.get(Category4, category_id)
        if category:
            await session.delete(category)
            await session.commit()

# Функция для удаления категории из таблицы Category5 по ID
async def delete_category5(category_id: int):
    async with async_session() as session:
        category = await session.get(Category5, category_id)
        if category:
            await session.delete(category)
            await session.commit()

# Функция для удаления ответа из таблицы Answer по ID
async def delete_answer(answer_id: int):
    async with async_session() as session:
        answer = await session.get(Answer, answer_id)  # Получаем ответ по ID
        if answer:
            await session.delete(answer)  # Удаляем ответ
            await session.commit()
