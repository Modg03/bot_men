from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import text

menu = [
    [InlineKeyboardButton(text=text.search_text, callback_data="search")],
    #[InlineKeyboardButton(text="FAQℹ️", callback_data="help")],
    [InlineKeyboardButton(text=text.bug, url="https://t.me/modg_men")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)

search_countries = [
    [InlineKeyboardButton(text="Німеччина🇩🇪", callback_data="choosen_germany")],
    [InlineKeyboardButton(text="Польща🇵🇱", callback_data="choosen_poland")],
    [InlineKeyboardButton(text="Литва🇱🇹", callback_data="choosen_lithuania")],
    [InlineKeyboardButton(text="Новопоштляндія", callback_data="choosen_pass1")],
    [InlineKeyboardButton(text="Многомодгія", callback_data="choosen_pass2")]
]

search_countries = InlineKeyboardMarkup(inline_keyboard=search_countries)