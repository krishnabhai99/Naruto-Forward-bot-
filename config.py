from os import environ 

class Config:
    API_ID = environ.get("API_ID", "14050586")
    API_HASH = environ.get("API_HASH", "42a60d9c657b106370c79bb0a8ac560c")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7923214678:AAHm-njC8_XcDQQZ27keyEI0TWI1AnUXcBA") 
    BOT_SESSION = environ.get("BOT_SESSION", "Hope") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Krishna")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5446367898').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
