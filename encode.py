#!/usr/bin/python3
import sys
import os
import auric
import RailFence

print(sys.argv)

bookName = sys.argv[1]
encodedFile = sys.argv[2]
password = sys.argv[3]

if len(sys.argv) < 3: 
    print("Not enought arguments")
    exit 

if not os.path.isfile(bookName):
    print("File not found")
    exit

book = ""
with open(bookName, 'r', encoding='utf-8') as fileobj:
    for line in fileobj:  
        for ch in line: 
            book += ch

firstChar = 32
lastChar = 127
firstEncoding = auric.encode(book, password, firstChar, lastChar)
encoded = RailFence.codifica(firstEncoding, 4)

if os.path.isfile(encodedFile):
    os.remove(encodedFile)

f = open(encodedFile, "a")
f.write(encoded)
f.close()

print("the file " + bookName + " has been encoded and saved as " + encodedFile)
print("Use the key " + str(password) + " (keep it secret!!) to decode the generated file.")
