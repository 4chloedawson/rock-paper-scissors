# Chloe Dawson
# Implements the game rock-paper-scissors for one user playing against the computer

import random

# global variables for tracking score
humanScore = 0
computerScore = 0
ties = 0


#######################
# getHumanMove
#   prompts user to enter their move (rock/paper/scissors)
def getHumanMove():
    legalMove = False
    while not legalMove:
        move = input("Please write rock, paper, or scissors: ")
        if move == "rock" or move == "paper" or move == "scissors":
            return move
        print ("That is not a valid move.")
#
# end of getHumanMove
#######################



#######################
# getComputerMove
#   randomly chooses a move (rock/paper/scissors)
def getComputerMove():
    ranNum = random.randint(0,2)

    if ranNum == 0:
        return "rock"
    elif ranNum == 1:
        return "paper"
    else:
        return "scissors"
#
# end of getComputerMove
#######################


#######################
# getWinner
#   compares moves for player1 and player2, determines which player won and increments the score
def getWinner(player1, player2):
    if player1 == player2:
        print("It's a tie")
        global ties
        ties = ties + 1
    elif player1 == "rock" and player2 == "scissors" or player1 == "paper" and player2 == "rock" or player1 == "scissors" and player2 == "paper":
        print("You won!")
        global humanScore
        humanScore = humanScore + 1
    else:
        print("I won!")
        global computerScore
        computerScore = computerScore + 1
#
# end of getWinner
#######################

#######################
# displayScore
#   displays the current score
def displayScore():
    print("Here is the score:")
    print("your wins: ", humanScore, ", my wins: ", computerScore, ", ties: ", ties)
#
# end of displayScore
#######################

# ### MAIN PROGRAM ################
#
print ("Welcome to the game of rock paper scissors.  I know you know the rules so let's go.\n")

rounds = int(input ("How many rounds would you like to play? "))
count = 0

while count <= rounds:
    displayScore()
    if count == rounds:
        print ("We played", rounds, "rounds.")
        playinput = input("Would you like to play again? (yes/no): ")
        if playinput == "yes" or playinput == "y" or playinput == "Yes" or playinput == "Y":
            rounds = int(input ("How many rounds would you like to play? "))
            count = 0
            humanScore = 0
            computerScore = 0
            ties = 0
        else:
            count = count + 1
    else:
        player1 = getHumanMove()
        player2 = getComputerMove()
        print ("your move: " + player1 + ", my move: " + player2)
        getWinner(player1, player2)
        count = count + 1


print ("The game is over. Thanks for playing!")
