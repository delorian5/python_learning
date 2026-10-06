import asyncio
import random
import sqlite3
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import CallbackQuery
from datetime import datetime
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
TOKEN = ""

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        messages INTEGER DEFAULT 0
    )
""")
conn.commit()
bot = Bot(token=TOKEN)
dp = Dispatcher()

def register_user(user_id, username, first_name):
    cursor.execute("""
        INSERT OR IGNORE INTO users (user_id, username, first_name)
        VALUES (?, ?, ?)
    """, (user_id, username, first_name))
    conn.commit()
def add_message(user_id):
    cursor.execute("""
        UPDATE users SET messages = messages + 1
        WHERE user_id = ?
    """, (user_id,))
    conn.commit()
def get_stats(user_id):
    cursor.execute("SELECT messages FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else 0

class GameStates(StatesGroup):
    playing = State()

@dp.callback_query(lambda c: c.data == "btn_time")
async def time_callback(callback: CallbackQuery):
    now = datetime.now()
    await callback.message.answer(f"Сейчас: {now.strftime('%H:%M:%S')}")
    await callback.answer()
@dp.callback_query(lambda c: c.data == "btn_date")
async def date_callback(callback: CallbackQuery):
    today = datetime.now()
    await callback.message.answer(f"Сегодня: {today.strftime('%d.%m.%Y')}")
    await callback.answer()
@dp.callback_query(lambda c: c.data == "btn_random")
async def random_callback(callback: CallbackQuery):
    number = random.randint(1, 100)
    await callback.message.answer(f"Случайное число: {number}")
    await callback.answer()
@dp.callback_query(lambda c: c.data == "btn_game")
async def game_callback(callback: CallbackQuery, state: FSMContext):
    secret = random.randint(1, 100)
    await state.update_data(secret=secret, attempts=0)
    await state.set_state(GameStates.playing)
    await callback.message.answer("Я загадал число от 1 до 100. Угадай!\n/stop - Выйти.")
    await callback.answer()
@dp.message(Command("start"))
async def start_handler(message: Message):
    user = message.from_user
    register_user(user.id, user.username, user.first_name)
    await message.answer(f"Привет, {user.first_name}! Я бот.")
@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("Я простой бот.\nКоманды: /start /help /random /date /time /menu /game /stats")
@dp.message(Command("stats"))
async def stats_handler(message: Message):
    user_id = message.from_user.id
    count = get_stats(user_id)
    await message.answer(f"Ты написал мне {count} сообщений.")
@dp.message(Command("time"))
async def time_handler(message: Message):
    now = datetime.now()
    await message.answer(f"Сейчас: {now.strftime('%H:%M:%S')}")
@dp.message(Command("date"))
async def date_handler(message: Message):
    today = datetime.now()
    await message.answer(f"Сегодня: {today.strftime('%d.%m.%Y')}")
@dp.message(Command("random"))
async def random_handler(message: Message):
    number = random.randint(1, 100)
    await message.answer(f"Случайное число: {number}")
@dp.message(Command("game"))
async def game_handler(message: Message, state: FSMContext):
    secret = random.randint(1, 100)
    await state.update_data(secret=secret, attempts=0)
    await state.set_state(GameStates.playing)
    await message.answer("Я загадал число от 1 до 100. Угадай!\n/stop - Выйти.")
@dp.message(GameStates.playing)
async def game_guess(message: Message, state: FSMContext):
    if message.text == "/stop":
        await state.clear()
        await message.answer("Игра окончена.")
        return
    try:
        guess = int(message.text)
    except ValueError:
        await message.answer("Это не число!")
        return
    data = await state.get_data()
    secret = data["secret"]
    attempts = data["attempts"] + 1
    if guess < secret:
        await state.update_data(attempts=attempts)
        await message.answer("Больше.")
    elif guess > secret:
        await state.update_data(attempts=attempts)
        await message.answer("Меньше.")
    else:
        await state.clear()
        await message.answer(f"Ты угадал! Число попыток: {attempts}")
@dp.message(Command("menu"))
async def menu_handler(message: Message):
    button_time = InlineKeyboardButton(text="🕐 Время", callback_data="btn_time")
    button_random = InlineKeyboardButton(text="🎲 Случайное", callback_data="btn_random")
    button_date = InlineKeyboardButton(text="📅 Дата", callback_data="btn_date")
    button_game = InlineKeyboardButton(text="🎮 Игра", callback_data="btn_game")
    keyboard =  InlineKeyboardMarkup(inline_keyboard=[[button_time, button_date],[button_random, button_game]])
    await message.answer("Выбери:", reply_markup=keyboard)
@dp.message(lambda message: message.text and message.text.lower() == "привет")
async def hello_handler(message: Message):
    await message.answer(f"Привет {message.from_user.first_name}!")
@dp.message()
async def echo_handler(message: Message):
    add_message(message.from_user.id)
    await message.answer(f"Ты сказал: {message.text}")
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())