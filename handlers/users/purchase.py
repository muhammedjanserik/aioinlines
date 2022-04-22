import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard, apples_keyboard, apples_keyboards
from loader import dp, bot

@dp.message_handler(Command("start"))
async def show_items(message: Message):
    await message.answer(text="Выберите психотест",
                         reply_markup=choice)
@dp.callback_query_handler(text_contains="pear")
async def buying_pear(call:CallbackQuery):
    await call.answer(cache_time=60)

    callback_data=call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Психологически возраст",
                              reply_markup=pear_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="Темперамент"))
async def buying_apples(call:CallbackQuery,callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Темперамент",
                              reply_markup=apples_keyboards)

@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_apples(call:CallbackQuery,callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Депрессия",
                              reply_markup=apples_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="apples"))
async def buying_apples(call:CallbackQuery,callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Ай кю",
                              reply_markup=apples_keyboards)


@dp.callback_query_handler(text = "cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("You've cancelled:", show_alert=True)

    await call.message.edit_reply_markup(reply_markup=None)