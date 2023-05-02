import logging
from aiogram import Bot, Dispatcher, executor, types
# import class
from db import Database
import openai
import os

logging.basicConfig(level=logging.INFO)

bot = Bot(token="5968643447:AAFOrspwnR14AhNAbljn5L1nq5t1Ly0F-1E")
openai.api_key_path = 'key.txt'

dp = Dispatcher(bot)
db = Database("telegram_db")

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Hi!")

@dp.message_handler(commands=['send2all'])
async def send2all(message:types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 642700014:
            # get message text
            text = message.text[10:]
            users = db.get_users()
            for row in users[:1000]:
                try:
                    await bot.send_message(row[0], text)
                    # check active or not and if user get message - set him active
                    if int(row[1])!=1:
                        db.set_active(row[0], 1)
                except:
                    db.set_active(row[0], 0)
            await bot.send_message(message.from_user.id, '!')


@dp.message_handler()
async def openai_response(message:types.Message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    await message.answer(response.choices[0].text)


if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)