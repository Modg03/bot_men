import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from keyboards import menu, search_countries

import text

# включаємо логування (модуль logging)
logging.basicConfig(level=logging.INFO)

bot = Bot(token='')
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    if message.chat.type == 'private':
        await message.answer(text.start.format(name=f"<b>{message.from_user.full_name}</b>"), parse_mode='HTML',
                             reply_markup=menu)


@dp.callback_query(F.data == "search")
async def process_search_callback(call: types.CallbackQuery):
    await bot.edit_message_text(text="Оберіть країну:", chat_id=call.message.chat.id,
                                message_id=call.message.message_id, reply_markup=search_countries, parse_mode='HTML')


@dp.callback_query(F.data.startswith("choosen_"))
async def process_choose_country_callback(callback_query: types.CallbackQuery):
    chosen_country = callback_query.data
    chat_id = callback_query.from_user.id
    await bot.send_message(chat_id, text.country_choosen, parse_mode='HTML')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.info("Starting bot")
    asyncio.run(main())