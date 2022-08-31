from src.payload import Payload
from src.handler import TELEGRAM, WHATSAPP, PUSH


def test_get_type(mocker):
    mocker.patch.object(Payload, "get_type", return_value=TELEGRAM)
    payload = Payload()
    message_type = payload.get_type("message")
    assert type(message_type) == str
    assert message_type == TELEGRAM

    mocker.patch.object(Payload, "get_type", return_value=WHATSAPP)
    payload = Payload()
    assert payload.get_type("message") == WHATSAPP

    mocker.patch.object(Payload, "get_type", return_value=PUSH)
    payload = Payload()
    assert payload.get_type("message") == PUSH


def test_get_messages(mocker):
    message_text_1 = "message text 1"
    message_text_2 = "message text 2"
    mocker.patch.object(
        Payload, "get_messages", return_value=[message_text_1, message_text_2]
    )
    payload = Payload()
    messages = payload.get_messages()
    assert type(messages) == list
    assert messages == [message_text_1, message_text_2]


def test_set_processed_request(mocker):
    mock = mocker.patch.object(Payload, "set_processed_request")
    payload = Payload()
    payload.set_processed_request({"test": "test"})
    assert mock.call_count == 1


def test_get_processed_request(mocker):
    request_body = "request body"
    response_body = "response body"
    mocker.patch.object(
        Payload,
        "get_processed_request",
        return_value={"request": request_body, "response": response_body},
    )
    payload = Payload()
    processed_request = payload.get_processed_request()
    assert type(processed_request) == dict
    assert processed_request["request"] == request_body
    assert processed_request["response"] == response_body
