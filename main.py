import smtplib
import time
import config
import os
import pyrogram 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, CallbackQuery, InlineQuery, InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

print ("\033[1;31m_________    __        __        ____        ________    __                                             \033[1;m")
print ("\033[1;34m|########|  |##\      /##|      /####\      |########|  |##|              By @RishbroProMax                 \033[1;m")
print ("\033[1;34m|##|____    |###\ __ /###|     /##/\##\        |##|     |##|              Made with code             \033[1;m")
print ("\033[1;34m|########|  |##| |##| |##|    /########\       |##|     |##|         ____   __       ____   __  ___     \033[1;m")
print ("\033[1;31m|##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__|    \033[1;m")
print ("\033[1;31m|########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \    \033[1;m")

START = "I m Alive 💙"

API_ID = '140XXX90'

API_HASH = 'a46f7b439d0axxxxxxc450f754e9'

BOT_TOKEN = '5867842414:xxxxxxxzRaWhWh6jnt_67NgVBat4J59XYU'

app = Client(

      "RishBro"

      api_id=API_ID,

      api_hash=API_HASH,

      bot_token=BOT_TOKEN,

)

files = open('email.txt', 'r')
bomb_emails = files.readlines()


email = config.email
password = config.password
message = input("Enter Message:")
message_relode = int(input("How many message you want to send:"))

ers")]]))

@app.on_message(filters.command("start"))

async def start(bot, message):

  await message.reply_photo("https://telegra.ph/file/c4ea3761bb73bab726334.jpg",caption=START,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="</> ємσ вσт ∂єνσℓσρєʀѕ", url="t.me/EmoBotDevolopers")]]))

num = 0
for bomb_email in bomb_emails:
    for x in range(0, message_relode):
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        num += 1
        print("Message sent to {}[{}]".format(bomb_email, num))
    time.sleep(1)

mail.close()
files.close()

print("Done")
