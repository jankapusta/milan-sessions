def readInteger():
    try:
        sNumber = raw_input()
        return int(sNumber)
    except ValueError:
        print "Skipping value '",sNumber,"'. Not a number"
        exit()

print "This will find indexes/positions of numbers from the list."

print "Enter size of the 1st list (the original data):"
iSizeDataset = readInteger()

print "Enter size of the 2nd list (the numbers to look for in original data):"
iSizeLookFor = readInteger()

print "Enter", iSizeDataset, "numbers for the 1st list (the original data):"
iNumbersDataset = []
for iN in range(iSizeDataset):
    iNumbersDataset.append(readInteger())

print "Enter", iSizeLookFor, " numbers for the 2nd list (the numbers to look for in original data):"
iNumbersLookFor = []
for iN in range(iSizeLookFor):
    iNumbersLookFor.append(readInteger())

print "Original dataset: ", iNumbersDataset
iIndexedDataset = dict({})
print "Indexing original dataset ..."
for i, number in enumerate(iNumbersDataset):
    if not number in iIndexedDataset.keys():
        iIndexedDataset[number] = i + 1
print "Original dataset was indexed:", iIndexedDataset

print "Numbers to look for: ", iNumbersLookFor
iResultIndexes = []
for i, number in enumerate(iNumbersLookFor):
    iResultIndexes.append(iIndexedDataset[number] if (number in iIndexedDataset.keys()) else 0)

print "Indexes found: ", iResultIndexes
print "Bye"
