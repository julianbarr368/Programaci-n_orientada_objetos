from payment import Payment

class Card(Payment):
    num_card = int
    cvv = int
    date = str

    def __init__(self, id, num_card, cvv, date):
        super().__init__(id)
        self.num_card = num_card
        self.cvv = cvv
        self.date = date