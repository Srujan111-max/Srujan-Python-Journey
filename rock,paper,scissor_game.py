import random


def play_game():
    YOU = 0
    COMPUTER = 0
    DRAWS = 0

    def last_end():
        print("---------------E N D---------------")

    def scorecard():
        print("-----------------------------------")
        print("-------------SCORECARD-------------")
        print("-----------------------------------")
        print(f"YOU: {YOU}\nCOMPUTER: {COMPUTER}\nDRAWS: {DRAWS}")

        if YOU > COMPUTER:
            print("🎉🎉🎉🎉🎉 YOU WON 🎉🎉🎉🎉🎉")
        elif YOU < COMPUTER:
            print("👎👎👎👎👎 YOU LOST 👎👎👎👎👎")
        else:
            print("********** D R A W **********")

    choices = ("rock", "paper", "scissor")

    while True:

        guess = input("Choose one; rock, paper or scissor: ").lower().strip()

        '''if guess not in choices:
            print("ERROR INPUT")
            scorecard()
            last_end()
            break'''

        if guess not in choices:
            print("INVALID CHOICE")
            print("Please enter rock or paper or scissor")
            continue
        

        computer = random.choice(choices)
        print(f"You chose: {guess}")
        print(f"Computer chose: {computer}")

        if guess == computer:
            print("You Draw")
            DRAWS += 1

        elif guess == "rock" and computer == "paper":
            print("You lose")
            COMPUTER += 1

        elif guess == "paper" and computer == "rock":
            print("You win 🎉")
            YOU += 1

        elif guess == "paper" and computer == "scissor":
            print("You lose")
            COMPUTER += 1

        elif guess == "scissor" and computer == "paper":
            print("You win 🎉")
            YOU += 1

        elif guess == "rock" and computer == "scissor":
            print("You win 🎉")
            YOU += 1

        elif guess == "scissor" and computer == "rock":
            print("You lose")
            COMPUTER += 1

        repeat = input("Do you want to continue the game? (yes/no) --> ").lower().strip()

        if repeat == "no":
            scorecard()
            last_end()
            break

        elif repeat != "yes":
            print("ERROR INPUT")
            last_end()
            scorecard()
            break


play_game()
