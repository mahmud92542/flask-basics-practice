# id is a python keyword, so i use _id
class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password