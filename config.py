from os import environ 

class Config:
    API_ID = environ.get("API_ID", "76767988")
    API_HASH = environ.get("API_HASH", "b734dchjyvhgmjbhjygbe836594706")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7923214678:AAHm-njC8_XcDQQZ27keyEI0TWI1AnUXcBA") 
    BOT_SESSION = environ.get("BOT_SESSION", "Hope") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://forwww1:jugvjih@cluster0.fuhwp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "name")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5446367898').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
