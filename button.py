from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 

create_test = InlineKeyboardMarkup(row_width=2)
iteam1 = InlineKeyboardButton(text="Test yaratish", callback_data= "create_test")
iteam2 = InlineKeyboardButton(text="Testni tekshirish", callback_data= "check_test")
iteam3 = InlineKeyboardButton(text="Men haqimda", callback_data= "about_us")
create_test.add(iteam1, iteam2, iteam3) 



follow_btn = InlineKeyboardMarkup(row_width=1)
folow = InlineKeyboardButton(text="➕ A'zo bo'lish ➕", url="https://t.me/joinchat/V7MV6Dv7atgwYmQy", callback_data="follow")
check = InlineKeyboardButton(text="✅ Tekshirish ✅", callback_data="subchenneldane")
follow_btn.add(folow, check)