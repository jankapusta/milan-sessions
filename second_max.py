
print "This will calculate second biggest number from the list."
print "Enter numbers separated by spaces:"

spaceSeparatedNumbers = raw_input()
sNumbers = spaceSeparatedNumbers.split(" ")

print "Entered numbers: ", sNumbers

iNumbers = []
for sNumber in sNumbers:
    try:
        iNumbers.append(int(sNumber))
    except ValueError:
        print "Skipping value '",sNumber,"'. Not a number"

iNumbers.sort();

print "Sorted numbers: ", iNumbers

iNumbersCount = len(iNumbers)
if (iNumbersCount < 2):
    print "Cannot calculate. At least 2 numbers are needed."
else:
    print "Second biggest number is: ", iNumbers[iNumbersCount-2]

