from src.handler import (
    MessageHandler,
    TELEGRAM,
    WHATSAPP,
    PUSH,
    PushNotification,
)
from src.payload import Payload
from src.messengers import WhatsappMessenger, TelegramMessenger


def test_handle(mocker):
    mock_objects = [
        mocker.patch.object(
            TelegramMessenger, "send", return_value="telegram messanger"
        ),
        mocker.patch.object(
            WhatsappMessenger, "send", return_value="whatsapp messanger"
        ),
        mocker.patch.object(
            PushNotification, "send", return_value="push notification"
        ),
    ]
    notification_types = [TELEGRAM, WHATSAPP, PUSH]
    call_counts = [1, 2, 2]

    for mock, call_count, notification_type in zip(
        mock_objects,
        call_counts,
        notification_types,
    ):
        payload = Payload()
        mocker.patch.object(
            payload, "get_messages", return_value=["message1", "message2"]
        )
        mocker.patch.object(
            payload, "get_type", return_value=notification_type
        )
        handler = MessageHandler()
        response = handler.handle(payload)
        assert type(response) == Payload
        assert mock.call_count == call_count
