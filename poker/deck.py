from card import Card
from collections import Counter
from itertools import groupby
class Deck:
    def __init__(self):
        self.cards = []
        suits = ['clubs','diamonds','hearts','spades']
        ranks = ['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
        for rank in ranks:
            for suit in suits:
                card = Card(rank,suit)
                self.cards.append(card)

    def get_number_of_cards(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def pick(self,n):
        hand = []
        for k in range(0,n):
            hand.append(self.cards.pop())
        return hand

class Hand:
    def __init__(self,cards):
        self.cards = cards
        self.ranks =   ['high card','1 pair','2 pair','three of a kind','straight','flush',
                        'full house','4 of a kind','straight flush',
                        'royal flush']
        self.sets = set(self.sortedRanks())
    def __lt__(self, other):
        return self.get_strengt()<other.get_strengt()

    def __gt__(self, other):
        return self.get_strengt()>other.get_strengt()
    def __eq__(self, other):
        return self.get_strengt()==other.get_strengt()

    def get_number_of_cards(self):
        return len(self.cards)

    def get_rank(self):
        rank = ''
        if self.royal_flush():
            rank = 'royal flush'
        elif self.straight_flush():
            rank = 'straight flush'
        elif self.two_pair():
            rank = '2 pair'
        elif self.three_of_a_kind():
            rank = '3 of a kind'
        elif self.straight():
            rank = 'straight'
        elif self.full_house():
            rank = 'full house'
        elif self.flush():
            rank = 'flush'
        elif self.one_pair():
            rank = '1 pair'
        return rank

    def get_strengt(self):
        return self.ranks.index(self.get_rank())

    def get_strengts(self):
        stren = []
        for card in self.cards:
            stren.append(card.get_strengt())
        stren.sort(reverse=True)
        return stren

    def sortedRanks(self):
        cardRanks = []
        for card in self.cards:
            cardRanks.append(card.get_strengt())
        cardRanks.sort(reverse=True)
        return cardRanks

    def one_pair(self):
        stren = self.get_strengts()
        tracker = 0
        for i in range(1,len(stren)):
            if stren[i-1:i+1][0] == stren[i-1:i+1][1]:
                tracker = tracker+1
        if tracker == 1:
            if self.three_of_a_kind(): return False
            return True
        return False

    def two_pair(self):
        stren = self.get_strengts()
        tracker = 0
        for i in range(1,len(stren)):
            if stren[i-1:i+1][0] == stren[i-1:i+1][1]:
                tracker = tracker+1
        if tracker == 2:
            if self.three_of_a_kind(): return False
            return True
        return False

    def three_of_a_kind(self):
        if self.full_house(): return False
        stren = self.get_strengts()
        threekind = 0
        for i in range(2,len(stren)):
            if stren[i-2:i+1][0] == stren[i-2:i+1][1] and stren[i-2:i+1][1] == stren[i-2:i+1][2]:
                threekind = threekind + 1
        if threekind == 1:
            return True
        else:
            return False

    def four_of_a_kind(self):
        return self.checkPairs(4)

    def full_house(self):
        s = self.get_strengts()
        condition1 = self.hist()[s[0]] == 2 and self.hist()[s[4]] == 3
        condition2 = self.hist()[s[0]] == 3 and self.hist()[s[4]] == 2
        if condition1 or condition2:
            return True
        return False
        #return self.checkPairs(3,2)

    def checkPairs(self, *t):
        for need, have in zip(t, self.sets):
            if need > have: return False
        return True

    def straight(self):
        stren = self.get_strengts()
        for i in range(1,len(stren)):
            if abs(stren[i-1:i+1][0] - stren[i-1:i+1][1]) != 1:
                return False
        if self.same_suit():
            return False
        return True

    def straight_flush(self):
        suites = self.get_suites()
        tracker = 0;
        stren = self.get_strengts()
        for i in range(1,len(stren)):
            if abs(stren[i-1:i+1][0] - stren[i-1:i+1][1]) == 1:
                tracker = tracker+1
        if self.same_suit():
            tracker = tracker + 1;

        if tracker == 5:
            return True
        return False

        return False

    def flush(self):
        if self.straight():
            return False
        if self.same_suit():
            return True
        return False

    def royal_flush(self):
        if self.straight_flush() and self.get_strengts()[4]== 8:
            if self.get_strengts()[0]== 12:
                return True
        return False

    def get_suites(self):
        suites = []
        for card in self.cards:
            suites.append(card.get_suit())
        return suites

    def same_suit(self):
        suites = self.get_suites()
        for i in range(1,len(suites)):
            if suites[i-1:i+1][0] != suites[i-1:i+1][1]:
                return False
        return True

    def hist(self):
        hist = Counter(self.get_strengts())
        return hist
