import random

rock = "ROCK"
paper = "PAPER"
scissors = "SCISSORS"
options = ("ROCK", "PAPER", "SCISSORS")
result = 0
while True:
    if result == 0:
        userChoice = input("PLEASE CHOOSE ROCK, PAPER, SCISSORS. WRITE Q FOR QUIT : ")
        print(" ")
        if userChoice in options:
            print("You choose " + userChoice)
        elif userChoice == "Q":
            print("THANKS FOR PLAYING\nmade by eysir")
            result = 3
        else:
            print("Invalid option. Please write again!\n")
            continue


        def cpumove():
            return random.choice(options)


        cpumove = cpumove()
        if userChoice == cpumove:
            print("Your opponent choose ", cpumove, "\nDRAW\n")
            result = 0
        elif userChoice == rock and cpumove == scissors or userChoice == scissors and cpumove == paper or userChoice == paper and cpumove == rock:
            print("Your opponent choose ", cpumove, "\nYOU WIN\n")
            result = 1
        elif userChoice == rock and cpumove == paper or userChoice == scissors and cpumove == rock or userChoice == paper and cpumove == scissors:
            print("Your opponent choose ", cpumove, "\nYOU LOSE\n")
            result = 2
    elif result == 1:
        if userChoice == rock:
            userChoice = input("PLEASE CHOOSE ROCK, PAPER, SCISSORS. WRITE Q FOR QUIT : ")
            print(" ")
            if userChoice in options:
                print("You choose " + userChoice)
            elif userChoice == "Q":
                print("THANKS FOR PLAYING\nmade by eysir")
                result = 3
            else:
                print("Invalid option. Please write again!\n")
                result = 1
                userChoice = rock
                continue

            cpumove = paper

            if userChoice == cpumove:
                print("Your opponent choose ", cpumove, "\nDRAW\n")
                result = 0
            elif userChoice == scissors:
                print("Your opponent choose ", cpumove, "\nYOU WIN\n")
                result = 1
            elif userChoice == rock:
                print("Your opponent choose ", cpumove, "\nYOU LOSE\n")
                result = 2
        elif userChoice == paper:
            userChoice = input("PLEASE CHOOSE ROCK, PAPER, SCISSORS. WRITE Q FOR QUIT : ")
            print(" ")
            if userChoice in options:
                print("You choose " + userChoice)
            elif userChoice == "Q":
                print("THANKS FOR PLAYING\nmade by eysir")
                result = 3
            else:
                print("Invalid option. Please write again!\n")
                result = 1
                userChoice = paper
                continue
            cpumove = scissors
            if userChoice == cpumove:
                print("Your opponent choose ", cpumove, "\nDRAW\n")
                result = 0
            elif userChoice == rock:
                print("Your opponent choose ", cpumove, "\nYOU WIN\n")
                result = 1
            elif userChoice == paper:
                print("Your opponent choose ", cpumove, "\nYOU LOSE\n")
                result = 2
        elif userChoice == scissors:
            userChoice = input("PLEASE CHOOSE ROCK, PAPER, SCISSORS. WRITE Q FOR QUIT : ")
            print(" ")
            if userChoice in options:
                print("You choose " + userChoice)
            elif userChoice == "Q":
                print("THANKS FOR PLAYING\nmade by eysir")
                result = 3
            else:
                print("Invalid option. Please write again!\n")
                result = 1
                userChoice = scissors
                continue
            cpumove = rock

            if userChoice == cpumove:
                print("Your opponent choose ", cpumove, "\nDRAW\n")
                result = 0
            elif userChoice == paper:
                print("Your opponent choose ", cpumove, "\nYOU WIN\n")
                result = 1
            elif userChoice == scissors:
                print("Your opponent choose ", cpumove, "\nYOU LOSE\n")
                result = 2
    elif result == 2:

        if userChoice == rock:
            userChoice = input("PLEASE CHOOSE ROCK, PAPER, SCISSORS. WRITE Q FOR QUIT : ")
            print(" ")
            if userChoice in options:
                print("You choose " + userChoice)
            elif userChoice == "Q":
                print("THANKS FOR PLAYING\nmade by eysir")
                result = 3
            else:
                print("Invalid option. Please write again!\n")
                result = 2
                userChoice = rock
                continue
            options2 = ("ROCK", "SCISSORS")
            cpumove = random.choice(options2)
            if userChoice == cpumove:
                print("Your opponent choose ", cpumove, "\nDRAW\n")
                result = 0
            elif userChoice == rock and cpumove == scissors or userChoice == scissors and cpumove == paper or userChoice == paper and cpumove == rock:
                print("Your opponent choose ", cpumove, "\nYOU WIN\n")
                result = 1
            elif userChoice == rock and cpumove == paper or userChoice == scissors and cpumove == rock or userChoice == paper and cpumove == scissors:
                print("Your opponent choose ", cpumove, "\nYOU LOSE\n")
                result = 2
        elif userChoice == paper:
            userChoice = input("PLEASE CHOOSE ROCK, PAPER, SCISSORS. WRITE Q FOR QUIT : ")
            print(" ")
            if userChoice in options:
                print("You choose " + userChoice)
            elif userChoice == "Q":
                print("THANKS FOR PLAYING\nmade by eysir")
                result = 3
            else:
                print("Invalid option. Please write again!\n")
                result = 2
                userChoice = paper
                continue
            options2 = ("ROCK", "PAPER")
            cpumove = random.choice(options2)
            if userChoice == cpumove:
                print("Your opponent choose ", cpumove, "\nDRAW\n")
                result = 0
            elif userChoice == rock and cpumove == scissors or userChoice == scissors and cpumove == paper or userChoice == paper and cpumove == rock:
                print("Your opponent choose ", cpumove, "\nYOU WIN\n")
                result = 1
            elif userChoice == rock and cpumove == paper or userChoice == scissors and cpumove == rock or userChoice == paper and cpumove == scissors:
                print("Your opponent choose ", cpumove, "\nYOU LOSE\n")
                result = 2
        elif userChoice == scissors:
            userChoice = input("PLEASE CHOOSE ROCK, PAPER, SCISSORS. WRITE Q FOR QUIT : ")
            print(" ")
            if userChoice in options:
                print("You choose " + userChoice)
            elif userChoice == "Q":
                print("THANKS FOR PLAYING\nmade by eysir")
                result = 3
            else:
                print("Invalid option. Please write again!\n")
                result = 2
                userChoice = scissors
                continue
            options2 = ("PAPER", "SCISSORS")
            cpumove = random.choice(options2)
            if userChoice == cpumove:
                print("Your opponent choose ", cpumove, "\nDRAW\n")
                result = 0
            elif userChoice == rock and cpumove == scissors or userChoice == scissors and cpumove == paper or userChoice == paper and cpumove == rock:
                print("Your opponent choose ", cpumove, "\nYOU WIN\n")
                result = 1
            elif userChoice == rock and cpumove == paper or userChoice == scissors and cpumove == rock or userChoice == paper and cpumove == scissors:
                print("Your opponent choose ", cpumove, "\nYOU LOSE\n")
                result = 2
    elif result == 3:
        break
