#AUTHOR: Trevor Conger UNWSP
#DATE: 10/11/24
#TITLE: Roll 100 times, see what you get.
import random


#Function to roll two dice. DIE1 + DIE2
#RETURN: the value of them added up
def randDice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def main():
    totalSum = 0
    numRolls = 100
    for _ in range(numRolls):
        rollResult = randDice()
        totalSum += rollResult
    average = totalSum / numRolls
    print(f"The average of 100 dice rolls is: {average:.2f}")

if __name__ == "__main__":
    main()