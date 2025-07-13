from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import OWNER_ID, bot, ubot, get_expired_date


class MSG:     
    def EXP_MSG_UBOT(X):
        return f"""
<blockquote><b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ɪᴅ:</b> <code>{X.me.id}</code>
<b>╰ ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴛᴇʟᴀʜ ʜᴀʙɪs</b></blockquote>
"""

    def START(message):
        return f"""
<b>𝙷𝚎𝚢 𝙱𝚛𝚘𝚘.. 👋🏻  <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a></b>❕
<blockquote><b>👑 {bot.me.mention} 𝚊𝚍𝚊𝚕𝚊𝚑 𝚋𝚘𝚝 𝚖𝚞𝚕𝚝𝚒 𝚌𝚕𝚒𝚎𝚗𝚝 𝚢𝚊𝚗𝚐 𝚍𝚊𝚙𝚊𝚝 𝚖𝚎𝚖𝚋𝚞𝚊𝚝 𝚊𝚔𝚝𝚒v𝚒𝚝𝚊𝚜 𝚊𝚗𝚍𝚊 𝚖𝚎𝚗𝚓𝚊𝚍𝚒 𝚕𝚎𝚋𝚒𝚑 𝚖𝚞𝚍𝚊𝚑 𝚍𝚊𝚗 𝚙𝚛𝚊𝚔𝚝𝚒𝚜.</b>

<b>✨ 𝚃𝚎𝚛𝚒𝚖𝚊 𝚔𝚊𝚜𝚒𝚑 𝚝𝚎𝚕𝚊𝚑 𝚋𝚎𝚛𝚐𝚊𝚋𝚞𝚗𝚐 𝚍𝚊𝚗 𝚖𝚎𝚗𝚐𝚐𝚞𝚗𝚊𝚔𝚊𝚗 𝚕𝚊𝚢𝚊𝚗𝚊𝚗 𝚞𝚜𝚎𝚛𝚋𝚘𝚝 𝚒𝚗𝚒. 𝙺𝚊𝚖𝚒 𝚑𝚊𝚍𝚒𝚛 𝚞𝚗𝚝𝚞𝚔 𝚖𝚎𝚖𝚞𝚍𝚊𝚑𝚔𝚊𝚗 𝚊𝚔𝚝𝚒𝚟𝚒𝚝𝚊𝚜 𝙰𝚗𝚍𝚊 𝚍𝚎𝚗𝚐𝚊𝚗 𝚏𝚒𝚝𝚞𝚛-𝚏𝚒𝚝𝚞𝚛 𝚘𝚝𝚘𝚖𝚊𝚝𝚒𝚜𝚊𝚜𝚒 𝚢𝚊𝚗𝚐 𝚌𝚊𝚗𝚐𝚐𝚒𝚑 𝚍𝚊𝚗 𝚖𝚞𝚍𝚊𝚑 𝚍𝚒𝚐𝚞𝚗𝚊𝚔𝚊𝚗. 𝙹𝚒𝚔𝚊 𝙰𝚗𝚍𝚊 𝚖𝚎𝚖𝚎𝚛𝚕𝚞𝚔𝚊𝚗 𝚋𝚊𝚗𝚝𝚞𝚊𝚗 𝚊𝚝𝚊𝚞 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚜𝚒 𝚕𝚎𝚋𝚒𝚑 𝚕𝚊𝚗𝚓𝚞𝚝, 𝚓𝚊𝚗𝚐𝚊𝚗 𝚛𝚊𝚐𝚞 𝚞𝚗𝚝𝚞𝚔 𝚖𝚎𝚗𝚐𝚑𝚞𝚋𝚞𝚗𝚐𝚒 𝚊𝚍𝚖𝚒𝚗 𝚊𝚝𝚊𝚞 𝚖𝚎𝚖𝚋𝚊𝚌𝚊 𝚍𝚘𝚔𝚞𝚖𝚎𝚗𝚝𝚊𝚜𝚒 𝚢𝚊𝚗𝚐 𝚝𝚎𝚛𝚜𝚎𝚍𝚒𝚊.</b>
<b>💭 𝚂𝚎𝚕𝚊𝚖𝚊𝚝 𝚋𝚎𝚛𝚊𝚔𝚝𝚒𝚟𝚒𝚝𝚊𝚜 𝚍𝚊𝚗 𝚜𝚎𝚖𝚘𝚐𝚊 𝚙𝚎𝚗𝚐𝚊𝚕𝚊𝚖𝚊𝚗 𝙰𝚗𝚍𝚊 𝚖𝚎𝚗𝚢𝚎𝚗𝚊𝚗𝚐𝚔𝚊𝚗‼️</b></blockquote>
<b>📎𝚂𝚊𝚕𝚊𝚖 𝙷𝚊𝚗𝚐𝚊𝚝,</b>
<b>@YanzzZzv1 🤖</b>"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote><b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>⎆ ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
 <b>├ 𝚍𝚊𝚗𝚊​ </𝚋>
 <b>├────• </b>
 <b>├────• A/N penggg</b>
 <b>├ 𝚀𝚛𝚒𝚜 </b>
 <b>├────• https://files.catbox.moe/afcvid.jpg</b>
 ᴜɴᴛᴜᴋ ᴍᴇᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ʟᴀɪɴɴʏᴀ ʙɪꜱᴀ ʟᴀɴɢꜱᴜɴɢ ʜᴜʙ ᴏᴡɴᴇʀ, ᴀᴅᴍɪɴ ᴅᴀɴ sᴇʟᴇʀ.

<b>⌭ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b></blockquote>
"""

    async def UBOT(count):
        return f"""
<blockquote><b>⌬ ᴜsᴇʀʙᴏᴛ ᴋᴇ</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ╰ ɪᴅ:</b> <code>{ubot._ubot[int(count)].me.id}</code></blockquote>
"""

    def POLICY():
        return """
ʙᴜᴀᴛ ʏᴀɴɢ ɴᴀɴʏᴀ ᴘᴇɴɢɢᴜɴᴀᴀɴ ᴜsᴇʀʙᴏᴛ ʏᴀɴɢ ᴀᴍᴀɴ ʙᴜᴀᴛ ᴅɪ ᴘᴀsᴀɴɢ ᴅɪ ᴀᴋᴜɴ ɪᴅ ᴀᴡᴀʟᴀɴ ʙᴇʀᴀᴘᴀ ʏᴀ??
ɢɪɴɪ ᴜɴᴛᴜᴋ ᴘᴇɴɢɢᴜɴᴀ ᴜsᴇʀʙᴏᴛ ɪᴛᴜ ᴊᴀɴɢᴀɴ ᴘᴇɴɢɢᴜɴᴀ ɪᴅ ᴀᴡᴀʟᴀɴ 𝟼-𝟽 ᴋᴀʀɴᴀ sᴀɴɢᴀᴛ ʀᴀᴡᴀɴ ᴊɪᴋᴀ ᴅɪ ᴘᴀsᴀɴɢ ᴜsᴇʀʙᴏᴛ.
ᴜɴᴛᴜᴋ ᴘᴇᴍᴀᴋᴀɪᴀɴ ᴜsᴇʀʙᴏᴛ ʙɪᴀsᴀ ᴅɪ ᴘᴀᴋᴀɪ ᴅɪ ᴀᴋᴜɴ ʟᴀᴍᴀ ᴀᴛᴀᴜ ʙɪᴀsᴀ ɪᴅ ᴀᴡᴀʟᴀɴ 𝟷-𝟻,
sᴇᴍᴜᴀ ᴘᴇɴɢɢᴜɴᴀ ᴅᴀʀɪ ɪᴅ ᴛᴇʀsᴇʙᴜᴛ sᴜᴅᴀʜ ᴛᴇʀʙɪʟᴀɴɢ ᴀᴍᴀɴ ᴛᴀᴘɪ sᴇᴍᴜᴀ ᴛᴇʀɢᴀɴᴛᴜɴɢ ᴘᴇᴍᴀᴋᴀɪᴀɴ ᴋᴀʟɪᴀɴ.
"""
