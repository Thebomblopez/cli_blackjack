def get_active(players):
    return [p for p in players if p.playing == True]

# Give Winners their money
def pay_winnings(players):
    for p in players:
        p.chips += p.bet_amount * 2
        p.bet_amount = 0
        print(p.name + " now has " + str(p.chips) + " chips.")

# Reset all player flags for next hand
def reset_players(players):
    for p in players:
        p.playing = True
        p.bet_amount = 0
        p.hand = []
