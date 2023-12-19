import random

numberOfStreaks = 0
head = 0        # Numeric value of the Head
tail = 1        # Numeric value of the Tail
headStreaksNumber = 0
tailStreaksNumber = 0

def flipTheCoin(numberOfTries):
    ''' Function which imitates flipping the coin numberOfTries time '''
    flipResult = []
    for i in range(numberOfTries):
        flipResult.append(random.randint(0,1))
    
    return flipResult


for experimentNumber in range(10000):
    flipCoinResult = flipTheCoin(100)
#    print(flipCoinResult)
    consecutiveHeads = 0 # Initial consecutive heads
    consecutiveTails = 0 # Initial consecutive tails
    for coinState in flipCoinResult:
        if coinState == head:
#            print('Tails reset')
            consecutiveTails = 0
#            print('Head increase to one')
            consecutiveHeads += 1
#            print('Current headValue=', headValue)
        
        if coinState == tail:
#            print('Heads reset')
            consecutiveHeads = 0
#            print('Tail value increase to one')
            consecutiveTails += 1
#            print('Current tailValue=', tailValue)

        if consecutiveHeads == 6:
#            print('Head Streak')
            consecutiveHeads = 0
            headStreaksNumber += 1

        if consecutiveTails == 6:
#            print('Tail Streak')
            tailValue = 0
            tailStreaksNumber += 1

numberOfStreaks = headStreaksNumber + tailStreaksNumber

print('Total streaks = ', numberOfStreaks)
print('Number of Head Streaks = ', headStreaksNumber)
print('Number of Tail Streaks = ', tailStreaksNumber)