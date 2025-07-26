from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

TOKEN = '8328542324:AAGYs_5so1RhUE4rXfz4Oc1nHVy6ngy20s8'

dp = Dispatcher()
bot = Bot(token=TOKEN)

class Register(StatesGroup):
    name = State()
    age = State()
    

@dp.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Привет! Как тебя зовут?')
    await state.set_state(Register.name)
    
@dp.message(Register.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Сколько тебе лет?')
    await state.set_state(Register.age)
    
@dp.message(Register.age)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer('Врзраст должен быть числом! Попробуй снова.')
    await state.update_data(age=int(message.text))
    data = await state.get_data()
    await message.answer(f'Ты {data['name']}, тебе {data['age']} лет, Прощай..')
    await state.clear()

async def  main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())