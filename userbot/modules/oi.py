from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.yunus(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hallo Perkenalkan Yah Nama Gw Yunus`")
    sleep(3)
    await typew.edit("`Umur 19 tahun`")
    sleep(1)
    await typew.edit("`Asal Dari Padang Salam Kenal Yah:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.tolol(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Lu tolol Goblok`")
    sleep(1)
    await typew.edit("`DASAR AUTISSS`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Jangan Bernafas`")
    sleep(1)
    await typew.edit("`Bunuh Diri Aja`")
# Create by myself @localheart
