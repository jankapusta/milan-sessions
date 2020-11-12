import sys
import os.path
from os import path


def openFileForRead(filename):
    try:
        return open(filename, "r")
    except IOError:
        print "Could not read", filename
        exit()

def openFileForWrite(filename):
    try:
        return open(filename, "w")
    except IOError:
        print "Could not open", filename
        exit()


print "This will parse one file and write line separated sentences into second file."

if len(sys.argv) != 3:
    print "You have to run this program with 2 parameters. E.g.: sentences.py filename1.txt output.txt"
    exit()

inputFile = sys.argv[1]
outputFile = sys.argv[2]

if (not(path.exists(inputFile))) or (not(path.isfile(inputFile))):
    print "File", inputFile, "does not exists"
    exit()

print "Reading", inputFile
fInput = openFileForRead(inputFile)
allContent = fInput.read()
fInput.close()
print "Content of input file:"
print "---------------------"
print allContent

print "Write to", outputFile, "..."
print "---------------------"
fOut = openFileForWrite(outputFile)
sentences = allContent.replace("\r"," ").replace("\n"," ").replace(". ",".. ").split(". ")
for sentence in sentences:
    print sentence
    fOut.write(sentence)
print "Bye"
fOut.close()





