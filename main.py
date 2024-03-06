import telebot
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from telebot.apihelper import ApiTelegramException

app = FastAPI()


class TelegramMessage(BaseModel):
    bottoken: str
    chatid: str
    message: str


@app.post("/send/")
def send_message(data: TelegramMessage):
    bot = telebot.TeleBot(data.bottoken)
    try:
        bot.send_message(data.chatid, data.message, parse_mode="Markdown")
        return {"status": "Message sent successfully"}
    except ApiTelegramException as error:
        raise HTTPException(status_code=500, detail=f"Telegram API error: {error}")
