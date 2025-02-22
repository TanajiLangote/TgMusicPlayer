from asyncio import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

from callsmusic import callsmusic, queues

from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    if callsmusic.pause(message.chat.id):
        await message.reply_text(" ⏸ Paused! \n Join @TeleVcplayer")
    else:
        await message.reply_text("Nothing is Playing \n Join @TeleVcplayer")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    if callsmusic.resume(message.chat.id):
        await message.reply_text(" ▶️ Resumed \n Join @TeleVcplayer")
    else:
        await message.reply_text("Nothing is Paused \n Join @TeleVcplayer")


@Client.on_message(command("stop") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_text("Nothing is Playing \n Join @TeleVcplayer")
    else:
        try:
            queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        await callsmusic.stop(message.chat.id)
        await message.reply_text(" Cleared the queue and left the call \n Join @TeleVcplayer")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_text("Nothing is Playing \n Join @TeleVcplayer")
    else:
        queues.task_done(message.chat.id)

        if queues.is_empty(message.chat.id):
            await callsmusic.stop(message.chat.id)
        else:
            await callsmusic.set_stream(
                message.chat.id, queues.get(message.chat.id)["file"]
            )

        await message.reply_text("Skipped \n Join @TeleVcplayer")


@Client.on_message(command("mute") & other_filters)
@errors
@authorized_users_only
async def mute(_, message: Message):
    result = callsmusic.mute(message.chat.id)

    if result == 0:
        await message.reply_text("Ok, Muted  \n please Join @TeleVcplayer ")
    elif result == 1:
        await message.reply_text(" Already muted! \n Please Join @TeleVcplayer")
    elif result == 2:
        await message.reply_text("🎙 Not in voice chat! \n Please Join @TeleVcplayer")


@Client.on_message(command("unmute") & other_filters)
@errors
@authorized_users_only
async def unmute(_, message: Message):
    result = callsmusic.unmute(message.chat.id)

    if result == 0:
        await message.reply_text("ok, Unmuted! \n PLease Join @TeleVcplayer")
    elif result == 1:
        await message.reply_text("Ok, Already unmuted \n Please Join @TeleVcplayer")
    elif result == 2:
        await message.reply_text(" Not in voice chat! \n PLease Join @TeleVcplayer")
