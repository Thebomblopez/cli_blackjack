# Make Person Class
class Person:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []
        self.bet_amount = int
        self.playing = True

    # String Representation
    def __repr__(self):
        return self.name
    
    # Function to gamble
    def bet(self, chips):
        if chips > self.chips:
            return "Not Enough Chips"
        self.chips -= chips
        return [self.name + " placed bet for " + chips + " chips", chips]
    
    # Fold hand
    def fold(self):
        print(self.name + ' folds')
        self.playing = False

    # Total Hand points
    def total_hand(self):
        aces = []
        point_total = 0
        for card in self.hand:
            if card.val == "Ace":
                aces.append(card)
            point_total += card.points
        
        # If Sore is over 21 and they have an Ace subtract 10 From their score
        while point_total > 21:
            if len(aces) > 0:
                point_total -= 10
                aces.pop()
            else:
                break
        
        return point_total

    # Show hand
    def show_hand(self):
        print(self.name + "'s hand is:")
        for card in self.hand:
            print(card.val + " of " + card.suit)
    