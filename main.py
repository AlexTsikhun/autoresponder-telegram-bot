import logging
from aiogram import Bot, Dispatcher, executor, types
from db import Database
import openai
import os
import time
from dotenv import load_dotenv, find_dotenv

logging.basicConfig(level=logging.INFO)

# Find .evn file
load_dotenv(find_dotenv())
bot = Bot(os.getenv("TOKEN"))
openai.api_key = os.getenv("OPENAI_TOKEN")

dp = Dispatcher(bot)
db = Database("telegram_db")


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if message.chat.type == "private":
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "✉️🤖Hi! I'm a bot that replies to messages and sends out mailing!")


@dp.message_handler(commands=["send2all"])
async def send2all(message: types.Message):
    if message.chat.type == "private":
        if message.from_user.id == 642700014:
            # Get message text
            text = message.text[10:]
            users = db.get_users()
            # Send to 1000 users (include admin)
            for row in users[:1000]:
                try:
                    await bot.send_message(row[0], text)
                    # Check active or not and if user get message - set him active
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                    # Avoid spam
                    # Bot able send to 30 messages per sec, for this case .sleep(0.033)
                    time.sleep(0.2)
                except:
                    db.set_active(row[0], 0)
            await bot.send_message(message.from_user.id, "!")


@dp.message_handler()
async def openai_response(message: types.Message):
    # For avoid openai.error.APIConnectionError - can add try/except or restart bot
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"],
    )
    await message.answer(response.choices[0].text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
