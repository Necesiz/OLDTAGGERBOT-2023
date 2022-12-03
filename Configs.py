# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏

import os

class Config(object):
    API_ID = int(getenv("API_ID", "17568815"))
    API_HASH = getenv("API_HASH", "177622d39f23e7c3d015f3d6ebaacd31")
    TOKEN = getenv("BOT_TOKEN", "None")
