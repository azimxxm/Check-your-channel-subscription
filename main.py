import logging
from aiogram import Bot, Dispatcher, executor, types
import config
import button as btn

print("Bot ishga tushdi.....")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


def chek_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if message.chat.type == 'private':
        if chek_sub_channel(await bot.get_chat_member(chat_id=config.channel_id, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, "Kerakli tugamni tanlang!", reply_markup=btn.create_test)
        else:
            await bot.send_message(message.from_user.id, config.NOTSUB_MESSAGE, reply_markup=btn.follow_btn)


@dp.callback_query_handler(text="subchenneldane")
async def subchenneldane(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if chek_sub_channel(await bot.get_chat_member(chat_id=config.channel_id, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, "Kerakli tugamni tanlang!", reply_markup=btn.create_test)
    else:
        await bot.send_message(message.from_user.id,  config.NOTSUB_MESSAGE, reply_markup=btn.follow_btn)


@dp.callback_query_handler(text="create_test")
async def subchenneldane(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Yaratmoqchi bo'lgan testingsiz yo'nalishini kiriting")


@dp.callback_query_handler(text="check_test")
async def subchenneldane(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Test Tekshirishni bosdingiz")


@dp.callback_query_handler(text="about_us")
async def subchenneldane(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "O'zingiz haqida ma'lumot olasiz!")

# # 💵 Service charge bilish bosilganida ishlidigan fungsiyalar
# @dp.message_handler(lambda message: message.text == "💵 Service charge")
# async def text(message: types.Message):
#     title = "<b> Calculate Your Rug Yourself How To Make The Square Meter Shown! </b>"
#     xisoblash_info = "<i>Add width to length. And multiply by 2</i>"
#     caption = f"{title} \n\n {xisoblash_info} "
#     await bot.send_photo(message.from_user.id, config.xisoblash_id, caption, parse_mode=types.ParseMode.HTML, reply_markup=btn.language_btn)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)