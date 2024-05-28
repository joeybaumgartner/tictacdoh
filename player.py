import json

class Player:

    def __init__(self, name: str, token: str, mark: str):
        self.name = name
        self.token = token
        self.mark = mark

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)