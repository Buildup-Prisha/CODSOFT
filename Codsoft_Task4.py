import random

CHOICES = ("rock", "paper", "scissors")
WIN_RULES = {
    ("rock", "scissors"),
    ("paper", "rock"),
    ("scissors", "paper"),
}

def get_player_choice():
    while True:
        user = input("Enter your choice (rock/r | paper/p | scissors/s): ").strip().lower()
        if user in ("rock", "r"):
            return "rock"
        elif user in ("paper", "p"):
            return "paper"
        elif user in ("scissors", "s"):
            return "scissors"
        else:
            print("Invalid choice, Please choose from the options provided.")

def get_computer_choice():
    return random.choice(CHOICES)

def decide_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player, computer) in WIN_RULES:
        return "win"
    else:
        return "lose"

def play_round():
    player_move = get_player_choice()
    computer_move = get_computer_choice()
    outcome = decide_winner(player_move, computer_move)

    print(f"\n  You chose:      {player_move}")
    print(f"  Computer chose: {computer_move}")

    if outcome == "win":
        print(" Congratulations! You win this round!")
    elif outcome == "lose":
        print(" Sorry! You lose this round.")
    else:
        print(" It's a tie.")

    return outcome

def play_game():
    scores = {"win": 0, "lose": 0, "tie": 0}
    print("=== WELCOME! LET'S PLAY! ===")
    print("=== Rock-Paper-Scissors ===")

    while True:
        result = play_round()
        scores[result] += 1

        print(
            f"\nScoreboard — You: {scores['win']} | "
            f"Computer: {scores['lose']} | Ties: {scores['tie']}\n"
        )

        again = input("Play another round? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nThanks for playing! ")
            print("Final score: ")
            print(
                f" Wins: {scores['win']}, "
                f" Losses: {scores['lose']}, "
                f" Ties: {scores['tie']}"
            )
            break
        print("-" * 50)

if __name__ == "__main__":
    play_game()
