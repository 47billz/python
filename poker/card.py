class Card:
    def __init__(self, card_rank, card_suite):
        self.card_rank = card_rank.lower()
        self.card_suite = card_suite.lower()
        self.card_name = card_rank+" of "+card_suite
        self.card_ranks = ['two','three','four','five','six','seven','eight',
                           'nine','ten','jack','queen','king','ace']

    def get_name(self):
        return self.card_name
    def get_suit(self):
        return self.card_suite
    def get_rank(self):
        #print self.card_rank,':',self.card_name
        return self.card_rank
    def get_strengt(self):
        return self.card_ranks.index(self.get_rank())
