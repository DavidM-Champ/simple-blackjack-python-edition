import random

def calculateScore(cards):
    score = 0
    hasAce = False
    
    for card in cards:
        try:
            cardValue = int(card)
            score += cardValue
        except ValueError:
            if card == "A":
                hasAce = True
            else:
                score += 10

    if hasAce:
        if (score + 11) > 21:
            score += 1
        else:
            score += 11
            
    return score

def printStatus(player_cards, dealer_cards):
    print("\n")
    print("Player total is " + str(calculateScore(player_cards)) + ".\n")
    
    for card in player_cards:
        print(card)
    print("\n")
    
    print("Dealer total is " + str(calculateScore(dealer_cards)) + ".\n")
    
    for card in dealer_cards:
        print(card)

def main():
    deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    dealer_cards = []
    player_cards = []
    random.shuffle(deck)
    
    print("Dealer draws first card.")
    dealer_cards.append(deck[-1])
    deck.pop()
    print("Player draws two cards")
    player_cards.append(deck[-1])
    deck.pop()
    player_cards.append(deck[-1])
    deck.pop()
    printStatus(player_cards, dealer_cards)
    
    while True:
        choice = input("Do you want to Hit, Stay, or Quit?")
        choice = choice.upper()
        if choice == "H":
            player_cards.append(deck[-1])
            deck.pop()
            printStatus(player_cards, dealer_cards)
            
            if calculateScore(player_cards) > 21:
                print("You busted! You lose!")
                return
        elif choice == "S":
            break
        elif choice == "Q":
            return
    
    print("Dealer draws rest of cards")
    while calculateScore(dealer_cards) < 17:
        dealer_cards.append(deck[-1])
        deck.pop()
    
    printStatus(player_cards, dealer_cards)
    
    if calculateScore(dealer_cards) > 21:
        print("Dealer busts! You win!")
    elif calculateScore(dealer_cards) > calculateScore(player_cards):
        print("Dealer wins!")
    elif calculateScore(dealer_cards) < calculateScore(player_cards):
        print("You win!")
    else:
        print("It's a tie!")
        
main()
