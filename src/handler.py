from abc import ABC
import logging

from src.messengers import WhatsappMessenger, TelegramMessenger
from src.payload import Payload

MESSENGER = "messenger(telegram|whatsapp)"
TELEGRAM = "messenger(telegram)"
WHATSAPP = "messenger(whatsapp)"
PUSH = "push"


class MessageInterface(ABC):
    pass


class PushNotification(MessageInterface):
    def send(self, message: str) -> None:
        pass


class MessageHandler(MessageInterface):
    def handle(self, payload: Payload) -> Payload:
        messages = payload.get_messages()
        whatsapp = WhatsappMessenger()
        telegram = TelegramMessenger()
        push = PushNotification()
        telegram_messages = []
        for message in messages:
            type = payload.get_type(message)
            if type == TELEGRAM:
                telegram_messages.append(message)
            elif type == WHATSAPP:
                whatsapp.send(message)
            elif type == PUSH:
                push.send(message)
            else:
                logging.log(logging.ERROR, "Unknown message type")
        if telegram_messages:
            telegram.send(telegram_messages)
        return payload
