
def readInteger():
    try:
        sNumber = raw_input()
        return int(sNumber)
    except ValueError:
        print "Skipping value '",sNumber,"'. Not a number"
        exit()

print "This will combine two sorted lists into one."

print "Enter size of the 1st list:"
iSizeM = readInteger()

print "Enter numbers from the 1st sorted list:"
iNumbersM = []
for iN in range(iSizeM):
    iNumbersM.append(readInteger())

print "Enter size of the 2nd list:"
iSizeN = readInteger()

print "Enter numbers from the 2nd sorted list:"
iNumbersN = []
for iN in range(iSizeN):
    iNumbersN.append(readInteger())

print "First list: ", iNumbersM
print "Second list: ", iNumbersN

iResultNumbers = []
indexM = 0
indexN = 0

while (indexM < iSizeM) or (indexN < iSizeN):
    if (indexN < iSizeN) and ((indexM >= iSizeM) or (iNumbersN[indexN] < iNumbersM[indexM])):
        print "Take", iNumbersN[indexN], "from second array"
        iResultNumbers.append(iNumbersN[indexN])
        indexN = indexN+1
    else:
        print "Take", iNumbersM[indexM], "from first array"
        iResultNumbers.append(iNumbersM[indexM])
        indexM = indexM+1

print "Two lists merged into one: ", iResultNumbers
print "Bye"
