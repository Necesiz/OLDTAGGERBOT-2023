# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏
 
import os

class Config:
    APP_ID = int(os.environ.get("APP_ID", 17568815))
    API_HASH = os.environ.get("API_API_HASHHASH", "177622d39f23e7c3d015f3d6ebaacd31")
    TOKEN = os.environ.get("TOKEN", "5740066159:AAEXp0XqICRHrQdV71YXuzij0PuRdb1CRXU")
