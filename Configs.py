# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 17568815))
    API_HASH = os.environ.get("API_HASH", 177622d39f23e7c3d015f3d6ebaacd31)
    TOKEN = os.environ.get("TOKEN", 5740066159:AAFFvQW5B6f2mZ7XIdB4ar86LWdp7qkQogc)
