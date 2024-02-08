# Exercise 1.1

for i in range(-4,5):
    toprint = "x" * (5-abs(i))
    print(toprint)


##

# Exercice 1.2

def addNumberInString(input_str):
    list_carac = list(input_str)
    sum = 0
    for i in range(0,len(list_carac)):
        if list_carac[i].isdigit() : sum += int(list_carac[i])
    print("Sum : ", sum)

input_str = input("Your String : ")
addNumberInString(input_str)

##

# Exercice 1.3

def findMaxExponentOfTwo(nb) :
    exp = 0
    while(nb > 2 ** exp):
        exp +=1
    return exp

def binary(nb) :
    exp = findMaxExponentOfTwo(nb)
    rest = nb
    binary = ""
    for i in range(exp,-1,-1):
        if rest >= 2 ** i :
            binary += "1"
            rest -= 2 ** i
        else :
            binary += "0"
    print("Binary of ", nb, " is : ", binary)

input_nb = int(input("Your Number : "))
binary(input_nb)

##

# Exercice 1.4

def fibonacci(maxnb):
    return_list = [0,1]
    fib0 = 0
    fib1 = 1

    while (fib0 + fib1 <= maxnb):
        fib_next = fib0 + fib1
        return_list.append(fib_next)
        fib0 = fib1
        fib1 = fib_next

    print(return_list)
    return(return_list)

input_nb = int(input("Your Number : "))
fibonacci(input_nb)


##

# Exercice 1.5

import random

def rock_paper_scissors():

    n_rounds = int(input("How many rounds ? "))

    user_score = 0
    computer_score = 0

    moves = ['rock', 'paper', 'scissors']

    for n in range(1,n_rounds+1):
        print("_______________________________________________________________")
        print("Round : ", n, " / ", n_rounds)
        print("User\'s score : ", user_score)
        print("Computer\'s score : ", computer_score, "\n")

        user_move = input("Choose your move (rock, paper, scissors): ").lower()

        if user_move not in moves:
            print("Invalid move. Please select rock, paper, or scissors.")
            return

        computer_move = random.choice(moves)

        print(f"Computer chose {computer_move}")

        # Who is the winner
        if user_move == computer_move:
            print("It is a tie for this round")
        elif (user_move == "rock" and computer_move == "scissors") or (user_move == "scissors" and computer_move == "paper") or (user_move == "paper" and computer_move == "rock"):
            print("You win this round")
            user_score += 1
        else:
            print("You lose this round")
            computer_score +=1

    # Who is the winner of the game
    print("_______________________________________________________________")
    print("RESULT OF THE GAME")
    if user_score == computer_score :
        print("It is a tie")
    elif user_score > computer_score :
        print("You win")
    else:
        print("You lose")

rock_paper_scissors()













