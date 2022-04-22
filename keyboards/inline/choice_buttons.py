from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_JIHC, URL_APPLE, URL_JIHCqwe, URL_APPLEqwe
from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Возраст", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Депрессия", callback_data="buy:apple:5")
choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Темперамент", callback_data="buy:Темперамент:5")
choice.insert(buy_apples)

buy_appless = InlineKeyboardButton(text="IQ", callback_data="buy:apples:5")
choice.insert(buy_appless)

cancel_button = InlineKeyboardButton(text="Болды", callback_data="cancel")
choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Өту", url=URL_JIHC)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Өту", url=URL_APPLE)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Өту", url=URL_JIHCqwe)
    ]
])
apples_keyboards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Өту", url=URL_APPLEqwe)
    ]
])