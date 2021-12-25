from pyrogram import Client
from environs import Env
from time import sleep
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

#Create bot
bot = Client("mephit_bot", id, hash)

#Mainloop
with open(f"{gettempdir()}\\botlastpic", "r", encoding='UTF-8') as lastpicfile: #Read last picname from file
    lastpic = lastpicfile.read()
while True:
    picname = get_weather(api_address, api_key, lat, lon)
    if picname != lastpic:  #Check match last and current pictures
        pic(picname)
        with bot:
            photos = bot.get_profile_photos("me")   #Get photos list
            bot.delete_profile_photos([p.file_id for p in photos[3:]])  #Delete old photos
            bot.set_profile_photo(photo=f"{PATH}/data/{picname}.png")    #Add new photo
        lastpic = picname
        with open(f"{gettempdir()}\\botlastpic", "w", encoding='UTF-8') as lastpicfile:   #Save current pic to file
            lastpicfile.write(picname)
    sleep(3600)
    

