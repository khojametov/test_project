from typing import Any


class Payload:
    def get_type(self, message: str) -> str:
        """
        Get the type of a message
        return string Following types: "messenger:(telegram|whatsapp)", "push"
        """
        pass

    def get_messages(self) -> list:
        """
        Get messages from payload
        :return: array ["message text N"]
        """
        pass

    def set_processed_request(self, data: dict) -> Any:
        pass

    def get_processed_request(self) -> Any:
        """
        Get information about processing the payload
        :return: array ["request" => "body", "response" => "body"]
        """
        pass
