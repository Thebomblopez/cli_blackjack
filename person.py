# Make Person Class
class Person:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []
        self.bet_amount = int
        self.playing = True
    
    # Function to gamble
    def bet(self, chips):
        if chips > self.chips:
            return "Not Enough Chips"
        self.chips -= chips
        return [self.name + " placed bet for " + chips + " chips", chips]
    
    # Fold hand
    def fold(self):
        self.playing = False

    # Total Hand points
    def total_hand(self):
        has_ace = False
        point_total = 0
        for card in self.hand:
            if card.val == "Ace":
                has_ace = True

            point_total += card.points
        
        if point_total > 21 and has_ace:
            point_total -= 10
        
        return point_total

    # Show hand
    def show_hand(self):
        print(self.name + "'s hand is:")
        for card in self.hand:
            print(card.val + " of " + card.suit)
    