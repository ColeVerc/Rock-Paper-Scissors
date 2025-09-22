#This is a rock, paper, scissors program
import random

EXIT = "QUIT"
userScore = 0
compScore = 0
def convertNumToSign(num):
    compSign = ""
    if num == 1:
        compSign = "Rock"
    elif num == 2:
        compSign = "Paper"
    elif num == 3:
        compSign = "Scissors"

    return compSign

def printScore(user, comp):
    print("The score is YOU", user, ": COMPUTER", comp, )
    
    return

userSign = input("Enter Rock, Paper, Scissors, or QUIT to exit.")
compSignNum = random.randint(1,3)

while userSign != EXIT:
    compSign = convertNumToSign(compSignNum)
    print ("The computer chose:", compSign)
    if userSign == compSign:
        print("Tie")
        printScore(userScore, compScore)
    elif (userSign == "Rock") and (compSign == "Paper"):
        print("You Lost")
        compScore += 1
        printScore(userScore, compScore)
    elif (userSign == "Rock") and (compSign == "Scissors"):
        print("You Win")
        userScore += 1
        printScore(userScore, compScore)
    elif (userSign == "Paper") and (compSign == "Scissors"):
        print("You Lost")
        compScore += 1
        printScore(userScore, compScore)
    elif (userSign == "Paper") and (compSign == "Rock"):
        print("You Win")
        userScore += 1
        printScore(userScore, compScore)
    elif (userSign == "Scissors") and (compSign == "Rock"):
        print("You Lost")
        compScore += 1
        printScore(userScore, compScore)
    elif (userSign == "Scissors") and (compSign == "Paper"):
        print("You Win")
        userScore += 1
        printScore(userScore, compScore)

    userSign = input("Enter Rock, Paper, Scissors, or QUIT to exit.")
    compSignNum = random.randint(1,3)