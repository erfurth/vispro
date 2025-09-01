class Message:
    __slots__ = ("msg_id", "msg_type", "payload")

    def __init__(self, msg_id, msg_type: str, payload: dict) -> None:
        self.msg_id = msg_id
        self.msg_type = msg_type
        self.payload = payload
