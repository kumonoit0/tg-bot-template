#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minimal aiogram 3.x Telegram bot template: menu, echo, errors."""
import asyncio
import logging
import os
import sys

try:
    from aiogram import Bot, Dispatcher, F
    from aiogram.filters import CommandStart
    from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
except ImportError:
    print("Нужно: pip install -r requirements.txt")
    sys.exit(1)

TOKEN = os.environ.get("BOT_TOKEN", "")
MENU = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Привет"), KeyboardButton(text="Помощь")]],
    resize_keyboard=True,
)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(m: Message):
    await m.answer("Привет! Я шаблон бота. Жми кнопки.", reply_markup=MENU)


@dp.message(F.text == "Помощь")
async def help_cmd(m: Message):
    await m.answer("Команды: /start. Остальное - эхо.")


@dp.message()
async def echo(m: Message):
    try:
        await m.answer(f"Эхо: {m.text}")
    except Exception as e:
        logging.exception("send failed: %s", e)


async def main():
    if not TOKEN:
        print("Укажи токен: BOT_TOKEN=123:ABC python bot.py")
        sys.exit(1)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(Bot(TOKEN))


if __name__ == "__main__":
    asyncio.run(main())
