sport = input("Enter a sport: ")
player_1_score = int(input("Enter player 1 score: "))
player_2_score = int(input("Enter player 2 score: "))

sport = sport.lower()

if sport == "basketball":
    if player_1_score == player_2_score:
        print("The game is a draw.")
    elif player_1_score > player_2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")

elif sport == "golf":
    if player_1_score == player_2_score:
        print("The game is a draw.")
    elif player_1_score < player_2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")

else:
    print("Unknown sport!")
               
