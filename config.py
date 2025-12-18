from os import environ 

class Config:
    API_ID = environ.get("API_ID", "34033563")
    API_HASH = environ.get("API_HASH", "10aab5a0e4450412a23bf060a2fe347a")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8353707438:AAFAItU0wUhKuBdIB0XQNTTiiwSAfWj7RgY") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Hanzlys:raihanmahdi24@cluster0.f8quvz7.mongodb.net/?appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "hanzlydb")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1157010249').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
