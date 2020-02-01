from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Oh wow! You tied :P")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose! Even Squeaky could beat me :)")", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose! Even Squeaky could beat me :)", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose! Even Squeaky could beat me :)", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("I'm sorry but that's not a valid answer. Sorrrryyyyyyy :(")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
