import sys
import os.path
from os import path


def openFileForRead(filename):
    try:
        return open(filename, "r")
    except IOError:
        print "Could not read", filename
        exit()


print "This will parse one file and count number of words."

if len(sys.argv) != 2:
    print "You have to run this program with 1 parameter. E.g.: words-count.py filename1.txt"
    exit()

inputFile = sys.argv[1]

if (not(path.exists(inputFile))) or (not(path.isfile(inputFile))):
    print "File", inputFile, "does not exists"
    exit()

print "Reading", inputFile
fInput = openFileForRead(inputFile)
allContent = fInput.read()
fInput.close()
print "Content of input file:"
print "---------------------"
print allContent, "---------------------"

wordsCount = len(allContent.split())
print "Words count: ", wordsCount
print "Bye"






