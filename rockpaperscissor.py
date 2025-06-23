import random
choices = ["rock", "paper", "scissors"]
wins = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
def play_round():
    user = input("enter rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice, please try again.")
        return None
    comp = random.choice(choices)
    print(f"Computer chose: {comp}")
    if user == comp:
        return "tie"
    elif wins[user] == comp:
        return "win"
    else:
        return "lose"
def game():
    score_user = score_comp = 0
    while True:
        result = play_round()
        if result == "win":
            print("You win this round!")
            score_user += 1
        elif result == "lose":
            print("You lose this round.")
            score_comp += 1
        elif result == "tie":
            print("This round is a tie.")
        else:
            continue
        print(f"Score - You: {score_user}, Computer: {score_comp}")
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            print(f"Final Score - You: {score_user}, Computer: {score_comp}")
            break
if __name__ == "__main__":
    game()    



