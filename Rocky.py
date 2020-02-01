from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Listen up will ya? Rock, Paper or Scissors?")
    if player == computer:
        print("Woah, that was a tie! Yee-haw!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose! Even Victor Tran could beat this game!", computer, "covers", player)
        else:
            print("You win and #youwonwithrock!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose! Even Victor Tran could beat this game!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose! Even Victor Tran could beat this game!", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Squeaky is sorry for you.")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
    