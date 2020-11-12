
def readInteger():
    try:
        sNumber = raw_input()
        return int(sNumber)
    except ValueError:
        print "Value '",sNumber,"' is not a number"
        exit()

print "This will calculate ways how to pay an amount with coins."

print "Enter total number of coins:"
iCoinsCount = readInteger()

print "Enter ", iCoinsCount, " coin values from highest to lowest:"
iCoins = []
for iN in range(iCoinsCount):
    iCoins.append(readInteger())
print "Entered coins: ", iCoins

print "Enter total amount to be made by coins:"
iTotalAmount = readInteger()

print "Calculating all combinations of coins:"

def foundMatch(currentResult, currentAmount, possibleCoins, currentCoin):
    currentResult.append(currentCoin)
    leftoverAmount =  currentAmount - currentCoin
    if(leftoverAmount > 0):
        findNextCoin(currentResult, leftoverAmount, possibleCoins)
    else:
        print currentResult

def findNextCoin(result, amount, possibleCoins):
    for i, coin in enumerate(possibleCoins):
        if amount >= coin:
            foundMatch(result[0:], amount, possibleCoins[i:], coin)

findNextCoin([], iTotalAmount, iCoins)

print "Bye"



