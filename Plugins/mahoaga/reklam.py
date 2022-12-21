import os, logging, asyncio
from Plugins import Maho
from telethon import events, Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from Configs import * 
import time

# Şaun için gerekli Mongodb yaparsan silersin, şimdilik iş yapar. 
ozel_list = [5134595693]
grup_sayi = []
etiketuye = []  

@Maho.on(events.NewMessage())
async def chatid(event):
  global etiketuye
  if event.is_group:
    if event.chat_id in grup_sayi:
      pass
    else:
      grup_sayi.append(event.chat_id)     

     
@Maho.on(events.NewMessage(pattern='^/stats ?(.*)'))
async def son_durum(event):
    global grup_sayi,ozel_list
    sender = await event.get_sender()
    if sender.id not in ozel_list:
      return
    await event.respond(f"**Ümümi Qrup Sayı 🧐**\n\nToplam Qrup: `{len(grup_sayi)}`")


@Maho.on(events.NewMessage(pattern='^/gcast ?(.*)'))
async def gcast(event): 
  global grup_sayi,ozel_list
  sender = await event.get_sender()
  if sender.id not in ozel_list:
    return
  reply = await event.get_reply_message()
  await event.respond(f"Toplam {len(grup_sayi)} Qrublara reklam göndərilir...")
  for x in grup_sayi:
    try:
      await Maho.send_message(x,f"**📣 @AnonyumAz **\n\n{reply.message}")
    except:
      pass
  await event.respond(f"Reklam göndərildi.")

# Reklam ve İstatistik Özellikleri konuldu. Sunucudan restart atıldığı zaman bilgiler geç gelecektir.
