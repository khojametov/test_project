from src.logger import logger


class TelegramMessenger:
    def send(self, message: str) -> str:
        logger.info(f"Telegram Message: {message}")
        pass


class WhatsappMessenger:
    def send(self, message: str) -> str:
        logger.info(f"Whatsapp Message: {message}")
        pass
