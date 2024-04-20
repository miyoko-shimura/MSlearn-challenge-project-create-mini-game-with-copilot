import random

def play_round(player_choice):
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    
    print(f"Computer's choice: {computer_choice}")
    
    if player_choice not in options:
        print("Invalid option. Please choose rock, paper, or scissors.")
        return 'invalid'
    
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'win'
    else:
        return 'lose'

def main():
    player_score = 0
    
    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        result = play_round(player_choice)
        
        if result == 'invalid':
            continue
        elif result == 'win':
            print("You won!")
            player_score += 1
        elif result == 'lose':
            print("You lost!")
        else:
            print("It's a tie!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print(f"Your final score: {player_score}")

if __name__ == "__main__":
    main()
