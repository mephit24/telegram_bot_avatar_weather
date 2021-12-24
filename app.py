from pyrogram import Client
from environs import Env
from time import sleep
from get_weather import get_weather
from pic import pic

#Get config from .env
config = Env()
config.read_env()

id = config.str("ID")
hash = config.str("ID_HASH")

#Create bot
bot = Client("mephit_bot", id, hash)

#Mainloop
while True:
    picname = get_weather()
    pic(picname)
    with bot:
        bot.set_profile_photo(photo=f"./data/{picname}.png")
    sleep(3600)
    

