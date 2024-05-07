import json
from abc import abstractmethod
from fastapi import status


class DatabaseException(Exception):
    def __init__(self, message_code: str | None = None) -> None:
        if not message_code:
            self.message_code = "database_unknown_error"
        else:
            self.status_code = message_code

    @property
    @abstractmethod
    def http_status(self) -> status:
        return status.HTTP_500_INTERNAL_SERVER_ERROR

    def get_response_body(self):
        return json.dumps({"code": self.message_code})
