from pyrogram import Client
from pytgcalls import PyTgCalls
from startup import call
from startup.queue import clear_queue
from pytgcalls.types import MediaStream
from startup import API_ID, API_HASH, SESSION_STRING
from startup.logging import LOGGER

audio_file = "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
api_id: int = API_ID
api_hash: str = API_HASH
session_string: str = SESSION_STRING

Bot = Client(
    name="Bot", api_id=api_id, api_hash=api_hash, session_string=session_string
)

User = PyTgCalls(Bot)



# MUSICBOT CORE


# audio playback
async def playAudio(chat_id, audio_file=audio_file):
    try:
        await call.play(
            chat_id,
            MediaStream(
                audio_file,
                video_flags=MediaStream.Flags.IGNORE,
            ),
        )
        return True, None
    except Exception as e:
        return False, f"Error:- <code>{e}</code>"

# pause 

async def pause(chat_id):
    try:
        await call.pause(
            chat_id,
        )
        return "Stream Paused"
    except Exception as e:
        return f"Error:- <code>{e}</code>"

# resume 

async def resume(chat_id):
    try:
        await call.resume(
            chat_id,
        )
        return "Stream Resumed"
    except Exception as e:
        return f"Error:- <code>{e}</code>"

# mute 

async def mute(chat_id):
    try:
        await call.mute(
            chat_id,
        )
        return "Stream Muted"
    except Exception as e:
        return f"Error:- <code>{e}</code>"

# unmute 

async def unmute(chat_id):
    try:
        await call.unmute(
            chat_id,
        )
        return "Stream Unmuted"
    except Exception as e:
        return f"Error:- <code>{e}</code>"


# end song 

async def stop(chat_id):
    try:
        clear_queue(chat_id)
        await call.leave_call(
            chat_id,
        )
        return "Stream Ended"
    except Exception as e:
        return f"Error:- <code>{e}</code>"
