



@Bot.on_message((filters.document | filters.video | filters.audio) & filters.private)
async def convert_link(bot, message):
    username = (await bot.get_me()).username
    file_type = message.media
    file_id, ref = unpack_new_file_id((getattr(message, file_type.value)).file_id)
    string = 'file_'
    string += file_id
    outstr = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
    user_id = message.from_user.id
    share_link = f"https://t.me/{username}?start={outstr}"
    await message.reply(f"<b>⭕ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟɪɴᴋ:\n\n🔗 ᴏʀɪɢɪɴᴀʟ ʟɪɴᴋ :- {share_link}</b>")
    return
