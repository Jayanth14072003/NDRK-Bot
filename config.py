#Code by KA18 the @legend580 💛❤️

import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging
from pathlib import Path
from os.path import dirname, join

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class tuple_(object):
    def __init__(self):
        return

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6922287383:AAFG3cqfQu5uXq7PjKYRSKTOhIGeGLNeT9Y")  #Original one
    # BOT_TOKEN = os.environ.get("BOT_TOKEN", "6100891233:AAEPZ22I2sI3IPVWDcsAC1X3Ydf1XqM6qvA") #testing bot 1 (ghfjg)
    # BOT_TOKEN = os.environ.get("BOT_TOKEN", "5872747581:AAHVN_3OP9uffBCKdesYZXFigzVuRYWLYOY") #testing bot 2 (url_v3)
    # BOT_TOKEN = os.environ.get("BOT_TOKEN", "5409934939:AAGXdsEVszrNGUQWhlrlcRO9WxAaCDsL9P8") #testing bot 3 (notify)
    
    API_ID = int(os.environ.get("API_ID", "3393749"))

    API_HASH = os.environ.get("API_HASH", "a15a5954a1db54952eebd08ea6c68b71")

    OWNER_ID = int(os.environ.get("OWNER_ID", "1061576483"))
    
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1061576483").split())

    AUTH_USERS = list(AUTH_USERS)
    
    AUTH_USERS.append(OWNER_ID)
    
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002246939657"))
    
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002097798772"))

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Jaya:Jaya@cluster0.4ot2upm.mongodb.net/?retryWrites=true&w=majority")  #Jaya@2003 becomes Jaya%402003 becouse of escape according to RFC 3986

    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Splitter-Bot")
    
    LOGGER = logging
    
    #Port
    PORT = os.environ.get("PORT", "8080")

    START_TEXT = """<b>🤗 Hello {}
    ɪ ᴀᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏ ꜱᴘʟɪᴛᴛᴇʀ ʙᴏᴛ. ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ᴠɪᴅᴇᴏ/ꜰɪʟᴇ ᴛᴏ ꜱᴘʟɪᴛ ɪɴᴛᴏ ᴇQᴜᴀʟ ᴘᴀʀᴛꜱ. ᴜꜱᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ.</b>"""
    
    NOT_AUTH = """<b>🤗 Hello {}
    ʏᴏᴜʀ ɴᴏᴛ ᴀɴ ᴀᴜᴛʜᴏʀɪꜱᴇᴅ ᴜꜱᴇʀ. ʏᴏᴜ ɴᴇᴇᴅ ʙᴜʏ ᴀ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ ꜰʀᴏᴍ [Kannadiga 💛❤️](https://t.me/legend580) ᴛᴏ ʙᴇᴄᴏᴍᴇ ᴀɴ ᴀᴜᴛʜᴏʀɪꜱᴇᴅ ᴜꜱᴇʀ.</b>"""

    PROGRESS_BAR = """<b>\n
    ╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
    ┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
    ┣⪼ ⏳️ Dᴏɴᴇ : {0}%
    ┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
    ┣⪼ ⏰️ Eᴛᴀ: {4}
    ╰━━━━━━━━━━━━━━━➣ </b>"""

    WAIT_MSG = """"<b>Processing ...</b>"""
    
    TEXT = "sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴛᴏ sᴇᴛ."

    REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""

    HELP_TEXT = """
    <b>𒊹︎︎︎ How To Split File Or Video</b>
    
     ➪ Send Your File Or Video For Download.
     
     ➪ Then Reply Command /sp With Split Size To Your File Or Video.
     
     ➪ Example: Reply <code>/sp 5</code> To Any File Or Video. Here The Given Video Is Splitted Into 5 Parts And Upload.

<b>𒊹︎︎︎ How to set thumbnail</b>
    
     ➪ Send Your Thumbnail Photo To Add Your Permanent Thumbnail Photo.

<b>𒊹︎︎︎ How To Deleting Thumbnail</b>
    
     ➪ Send /delthumb To Delete Your Thumbnail.

<b>𒊹︎︎︎ How To Show Thumbnail</b>
    
     ➪ Send /showthumb To View Custom Thumbnail 
 
     """
    
    ABOUT_TEXT = """
    **📛 My Name** : [𝐕𝐢𝐝𝐞𝐨 𝐒𝐩𝐥𝐢𝐭𝐭𝐞𝐫🚀](http://t.me/media_splitter_bot)
    
**❤️ Version** : VSB-V02🔥

**🤖 Source** : Not Available ❌

**🧿 Language** : [Python 3](https://www.python.org/)

**📢 Framework** : [Pyrogram](https://docs.pyrogram.org/)

**👨‍💻 Developer** : [ಕನ್ನಡಿಗ 💛❤️](https://t.me/legend580) """
    
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙️ Settings ⚙️', callback_data='OpenSettings')
        ],[
        InlineKeyboardButton('Help 🫂', callback_data='help'),
        InlineKeyboardButton('🧑‍🎓 About🧑‍🎓', callback_data='about')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Back', callback_data='home'),
        InlineKeyboardButton('🧑‍🎓 About 🧑‍🎓', callback_data='about')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Back', callback_data='home'),
        InlineKeyboardButton('Help 🫂', callback_data='help')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    AUTH_ADD_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👁️Confirm', callback_data='addauthuser'),
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    AUTH_DELETE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👁️Confirm', callback_data='deleteauthuser'),
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
