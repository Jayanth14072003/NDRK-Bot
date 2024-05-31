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

    #BOT_TOKEN = os.environ.get("BOT_TOKEN", "7153525008:AAFTPFIfqlIJiwHJOPzENWnwJQC-32LfR9k") #@video_splitter 
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6922287383:AAEMGiMAcifPH9n1dHF3eOT_jaC7PtGTeFE")
    
    API_ID = int(os.environ.get("API_ID", "3393749"))

    API_HASH = os.environ.get("API_HASH", "a15a5954a1db54952eebd08ea6c68b71")

    OWNER_ID = int(os.environ.get("OWNER_ID", "1061576483"))
    
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1061576483").split())

    AUTH_USERS = list(AUTH_USERS)
    
    AUTH_USERS.append(OWNER_ID)
    
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002060701925"))
    
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002097798772"))

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Jayanna:Jayanna2023@yash.tm1c2bd.mongodb.net/?retryWrites=true&w=majority")

    DATABASE_NAME = os.environ.get("DATABASE_NAME", "NDRKBot")
    
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

    PATH = str(Path(os.path.realpath(__name__)).parent)

    # ~ CONFIG
    config = tuple_()

    # ~ dirPath
    config.dirPath = PATH

    # ~ PATHS
    config.PATHS = tuple_()

    config.PATHS.BINARY_PATH = f"{config.dirPath}/tools"

    # ~ BIN
    config.BIN = tuple_()

    config.BIN.ffmpeg = f"{config.PATHS.BINARY_PATH}/ffmpeg.exe"
    config.BIN.ffprobe = f"{config.PATHS.BINARY_PATH}/ffprobe.exe"
    config.BIN.ffplay = f"{config.PATHS.BINARY_PATH}/ffplay.exe"


# # ~ CDM
# config.CDM = tuple_()
# config.CDM.chrome = deviceconfig.chrome_cdm_1610_l3
# config.CDM.andrl3 = deviceconfig.android_s905x_l3
# config.CDM.andrl3_v2 = deviceconfig.android_phone8162_l3
# # ~ DEVICES
# config.DEVICES = tuple_()
# config.DEVICES.NETFLIX = config.CDM.chrome
# config.DEVICES.APPLETV = config.CDM.andrl3_v2
# config.DEVICES.ITUNES = config.CDM.andrl3_v2
# config.DEVICES.AMAZON = config.CDM.andrl3_v2
# config.DEVICES.DCUNIVERSE = config.CDM.andrl3_v2
# config.DEVICES.DISNEYPLUS = config.CDM.andrl3_v2
# config.DEVICES.STARPLUS = config.CDM.andrl3_v2
# config.DEVICES.HULU = config.CDM.andrl3_v2
# config.DEVICES.STAN = config.CDM.andrl3_v2
# config.DEVICES.SHAHID = config.CDM.andrl3_v2
# config.DEVICES.RAKUTEN = config.CDM.andrl3_v2
# config.DEVICES.GOOGLEPLAY = config.CDM.andrl3_v2
# config.DEVICES.FANDANGONOW = config.CDM.andrl3_v2
# config.DEVICES.HBOMAX = config.CDM.andrl3_v2
# config.DEVICES.OSN = config.CDM.andrl3_v2
# config.DEVICES.PEACOCK = config.CDM.andrl3_v2
# # ~ MUXER
# config.MUXER = tuple_()
# config.MUXER.LANGUAGE_CODE_LIST = f"{config.dirPath}/tools/languages.json"

# config.MUXER.GROUP = config_data["OTHERS"]["GROUP"]
# config.MUXER.DELETE_EPISODE_TITLE = False
# config.MUXER.SCHEME = "P2P"
# config.MUXER.SCHEMES = {
#     "CC": "{t}",
#     "sdr": "{t}.{r}.{s}.WEB-DL.{ac}.x265-{gr}",
#     "hdr": "{t}.{r}.{s}.WEB-DL.{ac}.HDR.{vc}-{gr}",
#     "P2P": "{t}.{r}.{s}.WEB-DL.{ac}.{vc}-{gr}",
#     "psig": "{t}.MULTi.{r}.{s}.WEB-DL.{ac}.{vc}-{gr}",
#     "nsrc": "{t}.{r}.WEB-DL.{ac}.{vc}-{gr}",
#     "SIMPLE": "{t}.{r}.{s}.WEB-DL-{gr}",
# }
# # ~ PATHS
# config.PATHS = tuple_()
# config.PATHS.DL_FOLDER = f"{config.dirPath}"
# config.PATHS.DIR_PATH = f"{config.dirPath}"
# config.PATHS.ITUNES_LOGINS = f"{config.dirPath}/configs/itunes.yml"

# config.PATHS.COOKIES_PATH = f"{config.dirPath}/configs/Cookies"
# config.PATHS.PRESETS_FOLDER = f"{config.dirPath}/configs/Presets"
# config.PATHS.LOGGING_FOLDER = f"{config.dirPath}/configs/Logging"
# config.PATHS.KEYS_PATH = f"{config.dirPath}/configs/KEYS"
# config.PATHS.TOKENS_PATH = f"{config.dirPath}/configs/Tokens"
# config.PATHS.JSON_PATH = f"{config.dirPath}/json"
# config.PATHS.LOGA_PATH = f"{config.dirPath}/tools/aria2c/aria2c"
# # ~ SETTINGS
# config.SETTINGS = tuple_()
# config.SETTINGS.enable_aria2c_logging = False
# config.SETTINGS.enable_menu_selection = True
# config.SETTINGS.enable_aria2c_moded_progress_bar = False
# config.SETTINGS.external_txt_key = f"{config.PATHS.KEYS_PATH}/external.txt"
# config.SETTINGS.skip_video_demux = [
#     "HBOMAX",
#     "APPLETV",
#     "GOOGLEPLAY",
#     "DCUNIVERSE",
#     "ITUNES"
# ]

# # ~ VPN
# config.VPN = tuple_()
# config.VPN.proxies = None
# config.VPN.nordvpn = tuple_()
# config.VPN.nordvpn.port = config_data["VPN"]["nordvpn"]["port"]
# config.VPN.nordvpn.email = config_data["VPN"]["nordvpn"]["email"]
# config.VPN.nordvpn.passwd = config_data["VPN"]["nordvpn"]["passwd"]
# config.VPN.nordvpn.http = "https://{email}:{passwd}@{ip}:{port}"
# config.VPN.private = tuple_()
# config.VPN.private.port = config_data["VPN"]["private"]["port"]
# config.VPN.private.email = config_data["VPN"]["nordvpn"]["email"]
# config.VPN.private.passwd = config_data["VPN"]["nordvpn"]["passwd"]
# config.VPN.private.http = "http://{email}:{passwd}@{ip}:{port}"
# config.VPN.torguard = tuple_()
# config.VPN.torguard.port = config_data["VPN"]["torguard"]["port"]
# config.VPN.torguard.email = config_data["VPN"]["nordvpn"]["email"]
# config.VPN.torguard.passwd = config_data["VPN"]["nordvpn"]["passwd"]
# config.VPN.torguard.http = "http://{email}:{passwd}@{ip}:{port}"
# # ~ BIN
# config.BIN = tuple_()
# if platform.system() == "Linux":
#     config.BIN.mp4decrypt = "mp4decrypt"
#     config.BIN.mp4dump = "mp4dump"
#     config.BIN.pandsdecryptor = "mp4decrypt"
#     config.BIN.shaka_packager = f"{config.PATHS.BINARY_PATH}/decryptor/packager-linux"
#     config.BIN.mp4box = "mp4box"
#     config.BIN.ffmpeg = "ffmpeg"
#     config.BIN.ffprobe = "ffprobe"
#     config.BIN.ffplay = "ffplay"
#     config.BIN.MediaInfo = "mediainfo"
#     config.BIN.mkvmerge = "mkvmerge"
#     config.BIN.youtube = f"{config.PATHS.BINARY_PATH}/youtube-dl/youtube_dl/__main__.py"
#     config.BIN.aria2c = "aria2c"
#     config.BIN.SubtitleEdit = "mono SubtitleEdit"
#     config.BIN.SubtitleEdit = "mono SubtitleEdit"
#     config.BIN.SaldDL = f"SaldDL"
# else:
#     config.BIN.mp4decrypt = f"{config.PATHS.BINARY_PATH}/bento4/mp4decrypt.exe"
#     config.BIN.mp4demuxer = f"{config.PATHS.BINARY_PATH}/mp4box/mp4demuxer.exe"
#     config.BIN.mp4dump = f"{config.PATHS.BINARY_PATH}/bento4/mp4dump.exe"
#     config.BIN.pandsdecryptor = f"{config.PATHS.BINARY_PATH}/decryptor/pandsdecryptor.exe"
#     config.BIN.shaka_packager = f"{config.PATHS.BINARY_PATH}/decryptor/packager-win.exe"
#     config.BIN.mp4box = f"{config.PATHS.BINARY_PATH}/mp4box/mp4box.exe"
#     config.BIN.ffmpeg = f"{config.PATHS.BINARY_PATH}/ffmpeg/ffmpeg.exe"
#     config.BIN.ffprobe = f"{config.PATHS.BINARY_PATH}/ffmpeg/ffprobe.exe"
#     config.BIN.ffplay = f"{config.PATHS.BINARY_PATH}/ffmpeg/ffplay.exe"
#     config.BIN.MediaInfo = f"{config.PATHS.BINARY_PATH}/MediaInfo/MediaInfo.exe"
#     config.BIN.mkvmerge = f"{config.PATHS.BINARY_PATH}/mkvtoolnix/mkvmerge.exe"
#     config.BIN.youtube = f"{config.PATHS.BINARY_PATH}/youtube-dl/youtube-dl.exe"
#     config.BIN.aria2c = f"{config.PATHS.BINARY_PATH}/aria2c/aria2c.exe"
#     config.BIN.SubtitleEdit = f"{config.PATHS.BINARY_PATH}/SubtitleEdit/SubtitleEdit.exe"
#     config.BIN.CCExtractor = f"{config.PATHS.BINARY_PATH}/ccextractor/ccextractorwin.exe"
#     config.BIN.SaldDL = f"{config.PATHS.BINARY_PATH}/SaldDL.exe"
# # ~ SERVICES
# config.SERVICES = tuple_()
# # ╔═══════════════════
# # ║
# # ║  NETFLIX    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.NETFLIX = tuple_()
# config.SERVICES.NETFLIX.NAME = "NETFLIX"
# config.SERVICES.NETFLIX.TAG = "NF"
# config.SERVICES.NETFLIX.cookies_file = f"{config.PATHS.COOKIES_PATH}/cookies_nf.txt"
# config.SERVICES.NETFLIX.keys_file = f"{config.PATHS.KEYS_PATH}/netflix.keys"
# config.SERVICES.NETFLIX.token_file = f"{config.PATHS.TOKENS_PATH}/netflix_token.json"
# config.SERVICES.NETFLIX.email = config_data["CREDENTIALS"]["NETFLIX"]["email"]
# config.SERVICES.NETFLIX.password = config_data["CREDENTIALS"]["NETFLIX"]["password"]
# config.SERVICES.NETFLIX.profiles = f"{config.PATHS.BINARY_PATH}/profiles.json"
# config.SERVICES.NETFLIX.esn = "NFCDIE-03-{}".format(utils().random_hex(30))
# config.SERVICES.NETFLIX.esn_manifest = "NFCDIE-03-{}".format(utils().random_hex(30))
# config.SERVICES.NETFLIX.androidesn = "NFCDIE-03-{}".format(utils().random_hex(30))
# ESN = config_data["OTHERS"]["ESN"]
# #config.SERVICES.NETFLIX.esn = "NFCDCH-02-GRTTKNT2LAER6P2RWAMTNKJR9HG6XV"
# #config.SERVICES.NETFLIX.esn_manifest = "NFANDROID2-PRV-SHIELDANDROIDTV-NVIDISHIELD=ANDROID=TV-5485-D4D24ABA523EF168874D77EEF136881FFEEEE72B0F594230D4FA05C24C8F756A"
# #config.SERVICES.NETFLIX.androidesn = f"NFANDROID1-PRV-P-GOOGLEPIXEL=4=XL-{ESN}-BF80614C967DFD2D1CCDAAD69BCFD7063B037E6951CDF172C3D77792104CE05F"
# config.SERVICES.NETFLIX.metada_language = "en"
# config.SERVICES.NETFLIX.manifest_language = ["en-US"]

# # ╔═══════════════════
# # ║
# # ║  APPLETV    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.APPLETV = tuple_()
# config.SERVICES.APPLETV.NAME = "APPLETV"
# config.SERVICES.APPLETV.TAG = "APTV"
# config.SERVICES.APPLETV.cookies_file = f"{config.PATHS.COOKIES_PATH}/cookies_apple.txt"
# config.SERVICES.APPLETV.keys_file = f"{config.PATHS.KEYS_PATH}/apple.keys"
# config.SERVICES.APPLETV.token_file = f"{config.PATHS.TOKENS_PATH}/appletv.json"
# config.SERVICES.APPLETV.email = "Latinomhd@gmail.com"
# config.SERVICES.APPLETV.password = "9122Teamoalvarex"
# # ╔═══════════════════
# # ║
# # ║  ITUNES    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# # itunes_logins_raw = config_data["CREDENTIALS"]["ITUNES"]["logins"]
# # itunes_logins = dict()
# # for key, value in itunes_logins_raw.items():
# #     if value.get("cookies"):
# #         itunes_logins["key"] = {
# #             "cookies": value["cookies"].format(path=config.PATHS.COOKIES_PATH),
# #             "email": value["email"],
# #             "password": value["password"],
# #         }
# config.SERVICES.ITUNES = tuple_()
# config.SERVICES.ITUNES.NAME = "ITUNES"
# config.SERVICES.ITUNES.TAG = "ITUN"
# config.SERVICES.ITUNES.cookies_file = f"{config.PATHS.COOKIES_PATH}/cookies_itunes.txt"
# config.SERVICES.ITUNES.keys_file = f"{config.PATHS.KEYS_PATH}/itunes.keys"
# config.SERVICES.ITUNES.token_file = f"{config.PATHS.TOKENS_PATH}/itunes.json"
# config.SERVICES.ITUNES.email = None # config_data["CREDENTIALS"]["ITUNES"]["email"]
# config.SERVICES.ITUNES.password = None # config_data["CREDENTIALS"]["ITUNES"]["password"]
# config.SERVICES.ITUNES.logins = None
# # ╔═══════════════════
# # ║
# # ║  ITUNES    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.PARAMOUNT = tuple_()
# config.SERVICES.PARAMOUNT.NAME = "PARAMOUNT"
# config.SERVICES.PARAMOUNT.TAG = "PMTP"
# config.SERVICES.PARAMOUNT.cookies_file = f"{config.PATHS.COOKIES_PATH}/cookies_paramount.txt"
# config.SERVICES.PARAMOUNT.keys_file = f"{config.PATHS.KEYS_PATH}/paramount.keys"
# config.SERVICES.PARAMOUNT.token_file = f"{config.PATHS.TOKENS_PATH}/paramount.json"
# config.SERVICES.PARAMOUNT.email = None
# config.SERVICES.PARAMOUNT.password = None

# # ╔═══════════════════
# # ║
# # ║  DISNEYPLUS    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.DISNEYPLUS = tuple_()
# config.SERVICES.DISNEYPLUS.NAME = "DISNEYPLUS"
# config.SERVICES.DISNEYPLUS.TAG = "DSNP"
# config.SERVICES.DISNEYPLUS.token_file = f"{config.PATHS.TOKENS_PATH}/disney.json"
# config.SERVICES.DISNEYPLUS.keys_file = f"{config.PATHS.KEYS_PATH}/disneyplus.keys"
# config.SERVICES.DISNEYPLUS.email = config_data["CREDENTIALS"]["DISNEYPLUS"]["email"]
# config.SERVICES.DISNEYPLUS.password = config_data["CREDENTIALS"]["DISNEYPLUS"]["password"]
# # ╔═══════════════════
# # ║
# # ║  STARPLUS    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.STARPLUS = tuple_()
# config.SERVICES.STARPLUS.NAME = "STARPLUS"
# config.SERVICES.STARPLUS.TAG = "DSNP"
# config.SERVICES.STARPLUS.token_file = f"{config.PATHS.TOKENS_PATH}/starplus.json"
# config.SERVICES.STARPLUS.keys_file = f"{config.PATHS.KEYS_PATH}/starplus.keys"
# config.SERVICES.STARPLUS.email = config_data["CREDENTIALS"]["STARPLUS"]["email"]
# config.SERVICES.STARPLUS.password = config_data["CREDENTIALS"]["STARPLUS"]["password"]
# # ╔═══════════════════
# # ║
# # ║  AMAZON    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.AMAZON = tuple_()
# config.SERVICES.AMAZON.NAME = "AMAZON"
# config.SERVICES.AMAZON.TAG = "AMZN"
# config.SERVICES.AMAZON.keys_file = f"{config.PATHS.KEYS_PATH}/amazon.keys"
# config.SERVICES.AMAZON.cookies_file = config.PATHS.COOKIES_PATH + "/cookies_{region}.txt"
# config.SERVICES.AMAZON.token_file = config.PATHS.TOKENS_PATH + "/{region}.json"
# # ╔═══════════════════
# # ║
# # ║  GOOGLEPLAY    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.GOOGLEPLAY = tuple_()
# config.SERVICES.GOOGLEPLAY.NAME = "GOOGLEPLAY"
# config.SERVICES.GOOGLEPLAY.TAG = "GP"
# config.SERVICES.GOOGLEPLAY.keys_file = f"{config.PATHS.KEYS_PATH}/googleplay.keys"
# config.SERVICES.GOOGLEPLAY.cookies_file = f"{config.PATHS.COOKIES_PATH}/cookies_googleplay.txt"
# config.SERVICES.GOOGLEPLAY.cookies_file_headers = f"{config.PATHS.COOKIES_PATH}/cookies_googleplay_headers.txt"
# # ╔═══════════════════
# # ║
# # ║  HULU    -> [SETTINGS]
# # ║
# # ╚═══════════════════=
# config.SERVICES.HULU = tuple_()
# config.SERVICES.HULU.NAME = "HULU"
# config.SERVICES.HULU.TAG = "HULU"
# config.SERVICES.HULU.keys_file = f"{config.PATHS.KEYS_PATH}/hulu.keys"
# config.SERVICES.HULU.cookies_file = f"{config.PATHS.COOKIES_PATH}/cookies_hulu.txt"
# # ╔═══════════════════
# # ║
# # ║  DCUNIVERSE    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.DCUNIVERSE = tuple_()
# config.SERVICES.DCUNIVERSE.NAME = "DCUNIVERSE"
# config.SERVICES.DCUNIVERSE.TAG = "DCU"
# config.SERVICES.DCUNIVERSE.keys_file = f"{config.PATHS.KEYS_PATH}/dcu.keys"
# config.SERVICES.DCUNIVERSE.token_file = f"{config.PATHS.TOKENS_PATH}/dcuniverse.json"
# config.SERVICES.DCUNIVERSE.email = "email"
# config.SERVICES.DCUNIVERSE.password = "password"
# config.SERVICES.DCUNIVERSE.device_key = "DA59dtVXYLxajktV"
# # ╔═══════════════════
# # ║
# # ║  STAN    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.STAN = tuple_()
# config.SERVICES.STAN.NAME = "STAN"
# config.SERVICES.STAN.TAG = "STAN"
# config.SERVICES.STAN.keys_file = f"{config.PATHS.KEYS_PATH}/stan.keys"
# config.SERVICES.STAN.token_file = f"{config.PATHS.TOKENS_PATH}/stan.json"
# config.SERVICES.STAN.email = config_data["CREDENTIALS"]["STAN"]["email"]
# config.SERVICES.STAN.password = config_data["CREDENTIALS"]["STAN"]["password"]
# # ╔═══════════════════
# # ║
# # ║  HBOMAX    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.HBOMAX = tuple_()
# config.SERVICES.HBOMAX.NAME = "HBOMAX"
# config.SERVICES.HBOMAX.TAG = "HMAX"
# config.SERVICES.HBOMAX.keys_file = f"{config.PATHS.KEYS_PATH}/hbomax.keys"
# config.SERVICES.HBOMAX.token_file = f"{config.PATHS.TOKENS_PATH}/hbomax.json"
# config.SERVICES.HBOMAX.email = config_data["CREDENTIALS"]["HBOMAX"]["email"]
# config.SERVICES.HBOMAX.password = config_data["CREDENTIALS"]["HBOMAX"]["password"]
# config.SERVICES.HBOMAX.id_language = "es" # ["en", "es"]
# # ╔═══════════════════
# # ║
# # ║  PEACOCK    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.PEACOCK = tuple_()
# config.SERVICES.PEACOCK.NAME = "PEACOCK"
# config.SERVICES.PEACOCK.TAG = "PCOK"
# config.SERVICES.PEACOCK.keys_file = f"{config.PATHS.KEYS_PATH}/peacock.keys"
# config.SERVICES.PEACOCK.token_file = f"{config.PATHS.TOKENS_PATH}/peacock.json"
# config.SERVICES.PEACOCK.email = config_data["CREDENTIALS"]["PEACOCK"]["email"]
# config.SERVICES.PEACOCK.password = config_data["CREDENTIALS"]["PEACOCK"]["password"]
# config.SERVICES.PEACOCK.cookies_file = f"{config.PATHS.COOKIES_PATH}/cookies_peacock.txt"
# # ╔═══════════════════
# # ║
# # ║  SHAHID    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.SHAHID = tuple_()
# config.SERVICES.SHAHID.NAME = "SHAHID"
# config.SERVICES.SHAHID.TAG = "SHID"
# config.SERVICES.SHAHID.keys_file = f"{config.PATHS.KEYS_PATH}/shahid.keys"
# config.SERVICES.SHAHID.token_file = f"{config.PATHS.TOKENS_PATH}/shahid.json"
# # ╔═══════════════════
# # ║
# # ║  OSN    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.OSN = tuple_()
# config.SERVICES.OSN.NAME = "OSN"
# config.SERVICES.OSN.TAG = "OSN"
# config.SERVICES.OSN.keys_file = f"{config.PATHS.KEYS_PATH}/osn.keys"
# config.SERVICES.OSN.token_file = f"{config.PATHS.TOKENS_PATH}/osn.json"
# config.SERVICES.OSN.cookies_file = f"{config.PATHS.COOKIES_PATH}/cookies_osn.txt"
# config.SERVICES.OSN.proxies = {
#     "http": "http://abdalhmohmd8@gmail.com:123456@ae-dub.pvdata.host:8080",
#     "https": "http://abdalhmohmd8@gmail.com:123456@ae-dub.pvdata.host:8080",
# }
# # ╔═══════════════════
# # ║
# # ║  RAKUTEN    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.RAKUTEN = tuple_()
# config.SERVICES.RAKUTEN.NAME = "RAKUTEN"
# config.SERVICES.RAKUTEN.TAG = "RKTN"
# config.SERVICES.RAKUTEN.email = config_data["CREDENTIALS"]["RAKUTEN"]["email"]
# config.SERVICES.RAKUTEN.password = config_data["CREDENTIALS"]["RAKUTEN"]["password"]
# config.SERVICES.RAKUTEN.cookies_file = f"{config.PATHS.COOKIES_PATH}/cookies_rakuten.txt"
# config.SERVICES.RAKUTEN.keys_file = f"{config.PATHS.KEYS_PATH}/rakuten.keys"
# config.SERVICES.RAKUTEN.token_file = f"{config.PATHS.TOKENS_PATH}/rakuten.json"
# # ╔═══════════════════
# # ║
# # ║  FANDANGONOW    -> [SETTINGS]
# # ║
# # ╚═══════════════════
# config.SERVICES.FANDANGONOW = tuple_()
# config.SERVICES.FANDANGONOW.NAME = "FANDANGONOW"
# config.SERVICES.FANDANGONOW.TAG = "FNOW"
# config.SERVICES.FANDANGONOW.cookies_file = f"{config.PATHS.COOKIES_PATH}/cookies_fandangonow.txt"
# config.SERVICES.FANDANGONOW.keys_file = f"{config.PATHS.KEYS_PATH}/fandangonow.keys"

# utils().create_dirs_files(
#     DIRS=[config.PATHS.COOKIES_PATH, config.PATHS.TOKENS_PATH, config.PATHS.LOGA_PATH, config.PATHS.PRESETS_FOLDER, config.PATHS.LOGGING_FOLDER], FILES=[],
# )

# PRESETS_FOLDER = config.PATHS.PRESETS_FOLDER
# LOG_FILE = os.path.join(config.PATHS.LOGGING_FOLDER, "{}.log".format(strftime("%Y-%m-%d %H,%M,%S", gmtime())))


# class wvripper_config:
#     def config(self):
#         return config
