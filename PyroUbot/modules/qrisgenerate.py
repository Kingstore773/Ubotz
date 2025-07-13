from pyrogram.types import Message
from pyrogram.enums import ChatAction
from pyrogram import filters
from binascii import crc_hqx
from io import BytesIO
import segno

from PyroUbot import PY

__MODULE__ = "QRIS Generator"
__HELP__ = """
<b>✦ QRIS Generator</b>

<code>.qris [nominal]</code> - Membuat QRIS nominal tertentu.
"""

# ✅ QR Static dasar (tanpa CRC di akhir)
BASE_QRIS_STATIC = (
    "00020101021126670016COM.NOBUBANK.WWW01189360050300000879140214451151569912580303UMI51440014ID.CO.QRIS.WWW0215ID20232632982180303UMI5204481253033605802ID5919KINGSTORE OK11627246009TANGERANG61051511162070703A016304CAA7"
)

OWNER_ID = [7850668888]  # ID pemilik, sesuaikan

def build_qris_dinamis(base_qris: str, amount: int) -> str:
    nominal = f"{amount:.2f}"  # Format 5000 => '5000.00' ✅ TANPA dibagi
    tag_54 = f"54{len(nominal):02d}{nominal}"
    if "6304" in base_qris:
        base_qris = base_qris.split("6304")[0]
    payload = f"{base_qris}{tag_54}6304"
    crc = f"{crc_hqx(payload.encode(), 0xFFFF):04X}"
    return f"{payload}{crc}"

def generate_qr_image(payload: str) -> BytesIO:
    qr = segno.make(payload)
    buf = BytesIO()
    qr.save(buf, kind="png", scale=6)
    buf.name = "qris_dinamis.png"
    buf.seek(0)
    return buf

@PY.UBOT("qris")
@PY.TOP_CMD
async def qris_dinamis_handler(client, message: Message):
    if message.from_user.id not in OWNER_ID:
        return await message.reply("❌ Hanya Owner yang dapat menggunakan perintah ini!")

    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        return await message.reply("⚠️ Masukkan nominal, contoh:\n<code>.qris 15000</code>")

    amount = int(args[1])
    await message.reply("⏳ Membuat QRIS Dinamis...")

    try:
        payload = build_qris_dinamis(BASE_QRIS_STATIC, amount)
        qr_image = generate_qr_image(payload)

        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)

        # Pisah caption dan pesan utama
        await message.reply_photo(
            photo=qr_image,
            caption="✅ QRIS Dinamis"
        )
        await message.reply_text(f"💵 Nominal: Rp {amount:,}")

        await asyncio.sleep(1)
        try:
            await message.delete()
        except:
            pass

    except Exception as e:
        return await message.reply(f"❌ Gagal membuat QRIS:\n<code>{e}</code>")
