from PyroUbot import *

class STR:
    async def PONG(client):
        str_pong = await get_vars(client.me.id, "STRING_PONG")
        string_pong = str_pong if str_pong else " 𝚂𝙿𝙴𝙴𝙳"
        result = f"{string_pong}"
        return result

    async def OWNER(client):
        str_pong = await get_vars(client.me.id, "STRING_OWNER")
        string_pong = str_pong if str_pong else " 𝙿𝙴𝙽𝙶𝙶𝚄𝙽𝙰"
        result = f"{string_pong}"
        return result

    async def UBOT(client):
        str_pong = await get_vars(client.me.id, "STRING_UBOT")
        string_pong = str_pong if str_pong else " 𝚄𝙱𝙾𝚃"
        result = f"{string_pong}"
        return result

    async def DEVS(client):
        str_pong = await get_vars(client.me.id, "STRING_DEVS")
        string_pong = str_pong if str_pong else bot.me.mention
        result = f"{string_pong}"
        return result
