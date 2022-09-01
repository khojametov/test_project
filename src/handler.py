from abc import ABC
from src.logger import logger
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
            payload_type = payload.get_type(message)
            if payload_type == TELEGRAM:
                telegram_messages.append(message)
            elif payload_type == WHATSAPP:
                whatsapp.send(message)
            elif payload_type == PUSH:
                push.send(message)
            else:
                logger.error("Unknown message type")
        if telegram_messages:
            telegram.send(telegram_messages)
        return payload
