import random
def game_play():
    diff = input("Choose difficulty level: \n1.Easy\n2.Medium\n3.Hard\n").lower().strip()

    count = 0

    easy = random.randint(1,25)
    medium = random.randint(1,50)
    hard = random.randint(1,100)

    def compare(comp_num,guess_num):
            if comp_num == guess_num:
                print("Your guess is CORRECT")
                count = 1
            elif comp_num > guess_num:
                print("TOO LOW!")
                count = 0
            elif comp_num < guess_num:
                print("TOO HIGH!")
                count = 0
            return count

    while True:

        if diff == "1.easy" or diff == "1." or diff == "1" or diff == "easy":
            guess = int(input("Guess any number between 1-25: "))
            if guess >= 1 and guess <= 25:
                count = compare(easy,guess)
            else:
                print("OUT OF RANGE")
                continue

            if count == 1:
                print("THE END")
                break
            else:
                continue        
            
        elif diff == "2.medium" or diff == "2." or diff == "2" or diff == "medium":
            guess = int(input("Guess any number between 1-50: "))
            if guess >= 1 and guess <= 50:
                count = compare(medium,guess)
            else:
                print("OUT OF RANGE")
                continue

            if count == 1:
                print("THE END")
                break
            else:
                continue

        elif diff == "3.hard" or diff == "3." or diff == "3" or diff == "hard":
            guess = int(input("Guess any number between 1-100: "))
            if guess >= 1 and guess <= 100:
                count = compare(hard,guess)
            else:
                print("OUT OF RANGE")
                continue

            if count == 1:
                print("THE END")
                break
            else:
                continue

        repeat = input("Do you still want to continue-(yes/no): ").lower().strip()

        if repeat == "yes":
            game_play()
        else:
            break
                
game_play()