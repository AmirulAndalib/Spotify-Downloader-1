from pyrogram.errors import UserNotParticipant, PeerIdInvalid, UserIsBlocked, ChatWriteForbidden
from pyrogram import enums, filters, StopPropagation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.users_chats_db import db
from utils import Translate 
from bot import Mbot, LOG_GROUP as BUG
from requests import post 
import traceback 
def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"


async def Fsub(message, Mbot, user_id):
      try:
          if user_id  == 5268375124:
             return 
          get_prem = await db.get_prem(user_id)
          if get_prem:
             return 
          get_user = await db.get_user(user_id)
          if get_user and not get_user.get("language_code"):
             try:
                 tg_user = await Mbot.get_users(user_id)
                 if hasattr(tg_user, "language_code"):
                    lang_code = tg_user.language_code
                 else:
                     lang_code = "en"
                 await db.update_user(user_id,lang_code)
             except Exception:
                 pass 
          else:
              lang_code = get_user.get("language_code")
          try:
              get_member = await Mbot.get_chat_member(chat_id=-1001797516752,user_id=user_id)
          except UserNotParticipant:
              await message.reply(
    "Sᴏʀʀʏ Sɪʀ/ Mᴀᴅᴀᴍ 🥲\n\n"
    "    Iɴ ᴏʀᴅᴇʀ ᴛᴏ ᴜsᴇ ᴍᴇ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ @Mᴀsᴛᴇʀᴅᴇᴠss\n\n"
    "Nᴏᴛᴇ:\n"
    "    Iғ ʏᴏᴜ ᴇɴᴄᴏᴜɴᴛᴇʀ ᴀɴʏ ɪssᴜᴇs, ʏᴏᴜ ᴄᴀɴ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ ᴛᴏ sᴋɪᴘ ᴊᴏɪɴɪɴɢ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ.\n\n"
    "Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ!\n"
    "Jᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴇss ᴛʜᴇ ʀᴇғʀᴇsʜ ʙᴜᴛᴛᴏɴ.",
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Why?", url="https://t.me/MasterDevss/386"),
         InlineKeyboardButton("Join Channel 📣", url="https://t.me/+Pc8XEMwZlZ9jMjc9")],
        [InlineKeyboardButton("Refresh 🔄", callback_data="refresh"),
         InlineKeyboardButton("🌐 Translate", url=Translate.FSUB.format(lang_code))]
    ])
              )
              raise StopPropagation
          except PeerIdInvalid:
              try:
                  await Mbot.send_chat_action(chat_id=user_id,action=enums.ChatAction.TYPING)
                  get_member = await Mbot.get_chat_member(chat_id=-1001797516752,user_id=user_id)
              except PeerIdInvalid:
                  pass
              except UserIsBlocked:
                  pass
              except UserNotParticipant:
                  await message.reply(
    "Sᴏʀʀʏ Sɪʀ/ Mᴀᴅᴀᴍ 🥲\n\n"
    "    Iɴ ᴏʀᴅᴇʀ ᴛᴏ ᴜsᴇ ᴍᴇ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ @Mᴀsᴛᴇʀᴅᴇᴠss\n\n"
    "Nᴏᴛᴇ:\n"
    "    Iғ ʏᴏᴜ ᴇɴᴄᴏᴜɴᴛᴇʀ ᴀɴʏ ɪssᴜᴇs, ʏᴏᴜ ᴄᴀɴ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ ᴛᴏ sᴋɪᴘ ᴊᴏɪɴɪɴɢ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ.\n\n"
    "Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ!\n"
    "Jᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴇss ᴛʜᴇ ʀᴇғʀᴇsʜ ʙᴜᴛᴛᴏɴ.",
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Why?", url="https://t.me/MasterDevss/386"),
         InlineKeyboardButton("Join Channel 📣", url="https://t.me/+Pc8XEMwZlZ9jMjc9")],
        [InlineKeyboardButton("Refresh 🔄", callback_data="refresh"),
         InlineKeyboardButton("🌐 Translate", url=Translate.FSUB.format(lang_code))]
    ])
                  )
                  raise StopPropagation
      except (StopPropagation, ChatWriteForbidden):
          raise StopPropagation
      except Exception as e:
          await Mbot.send_message(BUG, f"#Fsub module Exception Raised {e}\n {paste(traceback.format_exc())}")
          await message.reply('503: Sorry, We Are Unable To Procced It 🤕❣️')     
      for var in list(locals()):
        if var != '__name__' and var != '__doc__':
            del locals()[var]
