from src.messengers import TelegramMessenger, WhatsappMessenger


def test_telegram_messenger(mocker):
    return_value = "This is telegram send method mock"
    mocker.patch.object(TelegramMessenger, "send", return_value=return_value)
    telegram = TelegramMessenger()
    assert telegram.send("test") == return_value


def test_whatsapp_messenger(mocker):
    return_value = "This is whatsapp send method mock"
    mocker.patch.object(WhatsappMessenger, "send", return_value=return_value)
    whatsapp = WhatsappMessenger()
    assert whatsapp.send("test") == return_value
