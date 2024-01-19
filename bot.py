import asyncio
import logging
import sqlite3

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

subject = None

from keyboards import menu, search_countries, add_item

import text

# включаємо логування (модуль logging)
logging.basicConfig(level=logging.INFO)

bot = Bot(token='6351249583:AAE8Fsdbe37byM_pDEtsnSHN_LYYFPqDjYQ')
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    if message.chat.type == 'private':
        # Отримати ім'я користувача
        user_name = message.from_user.full_name

        # Відправити вітальне повідомлення
        await message.answer(text.start, parse_mode='HTML', reply_markup=menu)



@dp.callback_query(F.data == "search")
async def process_search_callback(call: types.CallbackQuery):
    await bot.edit_message_text(text="Оберіть країну:", chat_id=call.message.chat.id,
                                message_id=call.message.message_id, reply_markup=search_countries, parse_mode='HTML')


@dp.callback_query(F.data.startswith("choosen_"))
async def process_choose_country_callback(callback_query: types.CallbackQuery):
    global chosen_country
    chosen_country = callback_query.data.replace("choosen_", "")
    chat_id = callback_query.from_user.id
    await bot.send_message(chat_id, text.country_choosen, parse_mode='HTML')

@dp.message(F.text)
async def handle_subject_input(message: types.Message):
    global subject
    subject = message.text.lower()
    chat_id = message.chat.id

    connection = sqlite3.connect(f"databases/{chosen_country}.db")
    cursor = connection.cursor()

    # Виконання запиту
    cursor.execute("SELECT name, text FROM subjects WHERE name = ?", (subject,))
    result = cursor.fetchone()

    # Закриття з'єднання з базою даних
    connection.close()

    if result is not None:
        # Текст з сусідньої рядки
        next_subject = result[0]
        next_text = result[1]
        print(f"{next_subject}, {next_text}")
        await bot.send_message(chat_id, text=(f"Результат: {next_text}"), reply_markup=add_item, parse_mode='HTML')
    else:
        await bot.send_message(chat_id, text.not_found, reply_markup=add_item, parse_mode='HTML')

@dp.callback_query(F.data == "exit_menu")
async def process_exit_menu(callback_query: types.CallbackQuery):
    await command_start_handler(callback_query.message)  # Виклик функції

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.info("Starting bot")
    asyncio.run(main())
