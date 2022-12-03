import os, logging, asyncio
from Plugins import Maho
from telethon import events, Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from Configs import *
from asyncio import sleep 
import time, random

# Gerekli silmeyiniz. 
anlik_calisan = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}

@Maho.on(events.NewMessage(pattern="^/yt ?(.*)"))
async def mentionalladmin(event):
  global anlik_calisan 
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu əmir sadəcə qrup vəya kanallarda edə bilərsiz.")
  
  admins = []
  async for admin in Maho.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmiri sadəcə yönəticlər isdifadə edə bilər.**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Köhmə Mesajlar Üçün Kullanıcılardan Bəhs edənmərəm! (qruba əlavə etmədən öncə göndərilən mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Tag'a Başlamaq üçün səbəb yazın... ✋\n\n(Məsələn: /yt Salam!)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Tag prosesi başladı.**")
        
    async for usr in Maho.iter_participants(event.chat_id,filter=ChannelParticipantsAdmins):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}),"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await Maho.send_message(event.chat_id, f"📢 ~ **{msg}**\n\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"{sender.first_name}"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**✅ Tag prosesi başarıyla dayandırıldı.**\n\n**Tag edilən Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}")
           await sleep(10)
           await a.delete()

  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in Maho.iter_participants(event.chat_id,filter=ChannelParticipantsAdmins):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}),"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await Maho.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"{sender.first_name}"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**✅ Tag prosesi başarıyla dayandırıldı.**\n\n**Tag edilən Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}")
           await sleep(10)
           await a.delete()
