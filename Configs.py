# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 23860620))
    API_HASH = os.environ.get("API_HASH", 347c94d92d0bbcfbc223651b73d71345)
    TOKEN = os.environ.get("TOKEN", 5740066159:AAGjgisqBiEkV1o0IXk7nd-A3hx6cjb1INE)
