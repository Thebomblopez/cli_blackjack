import deck, person, helpers, random

divider = "=" * 25
dealer = person.Person("Dealer", 1000000)
players = []
game_on = True
# Deck Object
deck = deck.Deck()

# ----- Main Game Loop -----
while game_on:
    user_input = input("Quit(q), add player(a), play hand(p): ")
    
    # If else block based on user input
    if user_input.lower() == "q":
        print("GAME = **OVER**")
        game_on = False
    
    # ----- Add Player -----
    elif user_input.lower() == "a":
        new_player = input("Player name?: ")
        players.append(person.Person(new_player, 100))
        print(new_player + " added, starting with 100 chips.")
        print(divider)
    
    # ----- Playing Hand -----
    elif user_input.lower() == "p":
        deck.deal(players)
        # ---------- Loop to bet or fold ----------
        for player in players:
            chosen = False
            while not chosen:
                user_choice = input(player.name + " would you like to play this hand? play(p) fold(f): ")
                
                # Type Check
                if type(user_choice) != str:
                    print("Must enter an string ex. 'p'")

                # Player folding hand
                elif user_choice.lower() == "f":
                    player.fold()
                    chosen = True
                    print(divider)

                elif user_choice.lower() == "p":
                    placed = False
                    # ---------- Loop to place bet ----------
                    while placed == False:
                        bet = input("How much do you want to bet?: ")
                        
                        # Type Check
                        if type(bet) != int:
                            print("Must enter an integer.")
                            print(divider)
                        
                        # Not Enough Chips
                        elif bet > player.chips:
                            print("Not enough chips for that bet.")
                            print(divider)

                        # Make Bet
                        else:
                            player.bet_amount = bet
                            player.chips -= bet
                            print(player.name + " placed bet for " + str(bet) + " chips.")
                            placed = True
                            print(divider)

                    chosen = True
                
                else:
                    print("Not a valid choice.")
                    print(divider)

        # print("Active Players")
        active_players = helpers.get_active(players)               
        # print(active_players)
        # for player in active_players:
        idx = 0
        # print(str(idx) + " == " + str(len(active_players)))

        # ----- Hit or Stay Sequence ----- 
        while idx < len(active_players):
            player = active_players[idx]
            player.show_hand()
            points = player.total_hand()
            print(str(points) + " points")
            print(divider)

            # Dealt Blackjack
            if points == 21:
                print("Blackjack! Winner Winner Chicken Dinner")
                active_players.remove(player)
                player.chips += player.bet_amount * 2
                print(player.name + " now has " + str(player.chips) + " chips.")
                print(divider)
                continue
                # print("making done True")
                # print(done)
                # print(divider)
            
            # Hit or Stay
            hit_stay = input(player.name + " Hit(h) or Stay(s)?: ")
            if hit_stay.lower() =="h":

                # Get Hit, Total Points
                deck.hit(player)
                points = player.total_hand()

                # Bust                
                if points > 21:
                    player.show_hand()
                    print(str(points) + " points bust!")
                    active_players.remove(player)
                    player.bet_amount = 0
                    print(str(player.chips) + " chips left.")
                    print(divider)
                    continue

                # Blackjack!
                # elif points == 21:
                #     print("Blackjack! Winner Winner Chicken Dinner")
                #     active_players.remove(player)
                #     player.chips += player.bet_amount * 2
                #     print(player.name + " has " + str(points) + " points and " + str(player.chips) + " chips.")
                #     print(divider)
                #     continue
                
                # Hit or Stay again
                else:
                    print(divider)

            # Stay 
            elif hit_stay.lower() == "s":
                print(player.name + " stays with " + str(player.total_hand())) 
                print(divider)
                idx += 1
                continue

            else:
                print("Not a valid choice.")
                print(divider)
        
        # ----- Reveal Dealer cards and check winners -----
        deck.dealer_cards(dealer)
        dealer_points = dealer.total_hand()
        dealer.show_hand()
        print(str(dealer_points) + " points")
        print(divider)
        # ----- While dealer hase less than 17 they have to hit -----
        while dealer_points < 17 and len(active_players) > 0:
            print("Dealer hits")
            new_card = random.choice(deck.cards)
            dealer.hand.append(new_card)
            deck.cards.remove(new_card)
            dealer_points = dealer.total_hand()
            dealer.show_hand()
            print(str(dealer_points) + " points")
            print(divider)
            
            if dealer_points > 21:
                print("Dealer bust with " + str(dealer_points) + " points!")
                helpers.pay_winnings(active_players)
                print(divider)
            
        # print("Length of active players: ")
        # print(active_players)
        # ----- If 17 <= dealer_points and dealer_points <= 21 compare the points with the players -----
        if dealer_points <= 21 and len(active_players) > 0:
            for player in active_players:
                if player.total_hand() >= dealer_points:
                    # ----- Winners -----
                    print(player.name + " beats the Dealer with " + str(player.total_hand()) + " points")
                    player.chips += player.bet_amount * 2
                    print(str(player.chips) + " chips stacked")
                    print(divider)
                else:
                    # ----- Losers -----
                    print(player.name + " loses to the Dealer with " + str(player.total_hand()) + " points")
                    print(str(player.chips) + " chips left")
                    print(divider)

        # Reset Flags for next hand
        helpers.reset_players(players)
        dealer.hand = []
        deck.shuffle()

    else:
        print("Not a valid choice.")