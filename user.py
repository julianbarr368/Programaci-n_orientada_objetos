from account import Account

class User(Account):
    email = str
    password = str

    def __init__(self, id, name, document, email, password):
        super().__init__(id, name, document)
        self.email = email
        self.password = password