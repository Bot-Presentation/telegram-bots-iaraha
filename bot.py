gister_member(usimport asyncio
import random
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import Message, ChatMemberUpdated

TOKEN = "8593766854:AAFIrN_UjFw44N_1Ns8Nic6Q7CB6HBC2JCU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

recorded_users = set()

@dp.message(F.chat.type.in_({"group", "supergroup"}))
async def record_user(message: Message):
    if message.from_user and not message.from_user.is_bot:
        recorded_users.add(f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name)
    
    if "ping" in message.text.lower() or "пинг" in message.text.lower():
        if recorded_users:
            random_user = random.choice(list(recorded_users))
            await message.reply(f"Понг! 🏓\nВыбираю жертву: {random_user}")
        else:
            await message.reply("Понг! Но я пока никого не запомнил...")
@dp.chat_member()
async def on_user_join(event: ChatMemberUpdated):
    if event.new_chat_member.user and not event.new_chat_member.user.is_bot:
        user = event.new_chat_member.user
        name = f"@{user.username}" if user.username else user.first_name
        recorded_users.add(name)

async def main():
    print("Бот запущен и готов к труду!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен.")
