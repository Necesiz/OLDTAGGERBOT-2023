# Botunu aşağıdaki link'e belirt veya configs e BOT_USERNAME şeklinde belirt keyfine göre yeğenim :) 
# Telegram da beni bulmak için @Mahoaga die arat sizlere yardımcı olabilirim. 
# Sadece hobi amaçlı yapılan bir deneme projesidir. 

from Plugins import Maho
from telethon import events, Button
from telethon.tl.types import ChannelParticipantsAdmins

@Maho.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in Maho.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await Maho.send_message(-1001641489645, f"ℹ️ **Start Verən Kullanıcı -** {ad}")
     return await event.reply(f"**Salam\Mənim Görəvim Kullanıcıları Tag Etməkdir.\nƏmirlər üçün Əmirlər butonuna basınız.**", buttons=(
                      [
                       Button.inline("Əmirlər", data="komutlar")
                      ],
                      [
                       Button.url('➕ Qruba Eklə', 'http://t.me/oldtaggerbot?startgroup=a'),
                       Button.url('📣 Kanal', 'https://t.me/oldsupport')
                      ],
                      [
                       Button.url('☯️ Sahibim', 'https://t.me/SS_WOLF')
                      ],
                    ),
                    link_preview=False)


  if event.is_group:
    return await Maho.send_message(event.chat_id, f"**Məni Qrubuna Aldığın Üçün Təşəkkürlər ✨**")

# Başlanğıc Button
@Maho.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in Maho.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"**Salam Mənim adım OLD Tagger\nGörəvim kullanıcılar Tag etmək\nƏmirlər üçün Əmirlər Butonuna Basın.**", buttons=(
                      [
                       Button.inline("Əmirlər", data="komutlar")
                      ],
                      [
                       Button.url('↘️ Qruba Eklə', 'http://t.me/oldtaggerbot?startgroup=a'),
                       Button.url('📣 Kanal', 'https://t.me/oldsupport')
                      ],
                      [
                       Button.url('☯️ Sahibim', 'https://t.me/SS_WOLF')
                      ],
                    ),
                    link_preview=False)

# Maho aga
@Maho.on(events.callbackquery.CallbackQuery(data="komutlar"))
async def handler(event):
    await event.edit(f"**Əmirlərim:\n\n/tag Toplu tag atar..\n/yt Sadəcə yönəticiləri tag etmək üçündür.\n/ttag Tək tək Tag edər.\n/btag Bayraqlar ilə Tag etmək üçündür.\n/stag Sözlər ilə tag edər.\n/itag İsimlər ilə tag etmək üçündür.\n/futbol Futbolcu adları ilə tag edər.\n/etag Emojilər ilə tag edər.\n/cancel - Sonlandırır... \n\n❗ Yalnızca yönəticilər bu əmri isdifadə edə bilər.**", buttons=(
                      [
                      Button.inline("◀️ Geri", data="start")
                      ]
                    ),
                    link_preview=False)
