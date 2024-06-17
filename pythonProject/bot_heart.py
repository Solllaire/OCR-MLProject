import decypher
import asyncio
import logging
import sys
import os
from Source import *
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

TOKEN = bot_token

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(F.photo, Command('readImage'))
async def photo_handler(message: Message) -> None:
    photo_data = message.photo[-1].file_id
    await message.bot.download(photo_data, destination=file_name)
    decypher.OCR_method(path=file_name)
    with open(textfile, "r") as text_file:
        pictureText = text_file.read()
    with open(resultfile, 'r') as myFile:
        answerText = myFile.readline()
        answerText = answerText.split(" ")
    os.remove(textfile)
    os.remove(resultfile)
    await message.answer("Language: "+answerText[0]+"\nText:"+pictureText)
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
