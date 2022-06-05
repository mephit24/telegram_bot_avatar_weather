from pyrogram import Client
from environs import Env
from time import sleep
import os
from tempfile import gettempdir
from get_weather import get_weather
from pic import pic, PATH

#Get config from .env
config = Env()
config.read_env()

id = config.str("ID")
hash = config.str("ID_HASH")

api_address = config.str("YA_ADDRESS")
api_key = config.str("YA_API_KEY")

lat = config.str("lat")
lon = config.str("lon")

DELAY = config.int("DELAY")

#Create data directory
if not os.path.exists(f"{PATH}/data"):
    os.mkdir(f"{PATH}/data")

#Delay of change avatar
def countdown(delay):
    while delay >= 0:
        sleep(1)
        delay -= 1
        print(f"Update photo in: {delay:04d} sec", end='\r')
        
#Telegram handler
bot = Client("mephit_bot", id, hash)
        
#Mainloop
tempfile = f"{gettempdir()}/botlastpic"
if not os.path.exists(tempfile):
    f = open(tempfile, "x")
    f.close()
with open(tempfile, "r", encoding='UTF-8') as lastpicfile: #Read last picname from file
    lastpic = lastpicfile.read()
while True:
    try:
        picname = get_weather(api_address, api_key, lat, lon)
    except:
        print("Weather API not access!")
        picname = lastpic
    if picname != lastpic:  #Check match last and current pictures
        pic(picname)
        with bot:
            photos = bot.get_chat_photos("me")   #Get avatars list
            bot.delete_profile_photos([p.file_id for p in list(photos)[3:]])  #Delete old avatars
            bot.set_profile_photo(photo=f"{PATH}/data/{picname}.png")    #Add new avatar
        lastpic = picname
        with open(tempfile, "w", encoding='UTF-8') as lastpicfile:   #Save current pic to file
            lastpicfile.write(picname)
    countdown(DELAY)
