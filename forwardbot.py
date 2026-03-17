from pyrogram import Client, filters

api_id = 39990072
api_hash = "5f33c6473a52439af7fee27f46585410"

source_channel = "https://t.me/GAMES_HORIZON_CLUBS"

app = Client("my_userbot", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(source_channel))
def forward_to_saved(client, message):
    message.forward("me")  # "me" = Saved Messages

app.run()