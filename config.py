from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "29478734"))
    API_HASH = environ.get("API_HASH", "8bd53e36eceada3329fbe46d9b961d1f")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6881166251:AAEc3bHYmWAGQpM3eipFY8ZGoTJ3M5Ryj64") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://nikzgod:nikzgod@cluster0.lqn4wau.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "ForwardBot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7081827234').split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
