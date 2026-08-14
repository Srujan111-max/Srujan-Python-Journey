import random

def play_game():
    YOU = 0
    COMPUTER = 0
    while True:
        repeat = input("Do you still continue the game:(yes/no) --> ").lower().strip()
        if repeat == "yes":
            guess = input("Choose one; rock, paper or scissor: ").lower().strip()
            choices = ("rock","paper","scissor")
            computer = random.choice(choices)
            if guess == computer:
                print("You Draw")
            elif guess == "rock" and computer == "paper":
                print("You win 🎉")
                YOU+=1
            elif guess == "paper" and computer == "rock":
                print("You lose")
                COMPUTER+=1
            elif guess == "paper" and computer == "scissor":
                print("You lose")
                COMPUTER+=1
            elif guess == "scissor" and computer == "paper":
                print("You win 🎉")
                YOU+=1
            elif guess == "rock" and computer == "scissor":
                print("You win 🎉")
                YOU+=1
            elif guess == "scissor" and computer == "rock":
                print("You lose")
                COMPUTER+=1
            print(f"computer chose: {computer}")
        else: 
            print("---------------E N D---------------")
            print("-----------------------------------")
            print("------------SCORECARD--------------")
            print("-----------------------------------")
            print(f"YOU: {YOU} \nCOMPUTER: {COMPUTER}")
            if YOU > COMPUTER:
                print("🎉🎉🎉🎉🎉YOU WON🎉🎉🎉🎉🎉")
            else:
                print("👎👎👎👎👎YOU LOST👎👎👎👎👎")
            break
play_game()

