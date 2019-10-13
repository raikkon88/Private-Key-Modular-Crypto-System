#!/usr/bin/python3
# Autor : Marc Sànchez Pifarré
# Programa de descodificació
# IN : 
# - encodedFile -> Nom de fitxer a descodificar
# - decodedFile -> Nom de fitxer a on desar el text descodificat
# - password -> Paraula de pas o clau per a la descodificació

# OUT : 
# - A decodedFile hi ha el text de encodedFile desxifrat amb la clau password

import sys
import os
import auric
import RailFence

print(sys.argv)

encodedFile = sys.argv[1]
decodedFile = sys.argv[2]
password = sys.argv[3]

if len(sys.argv) < 4: 
    print("Not enought arguments")
    exit 

if not os.path.isfile(encodedFile):
    print("File not found")
    exit

book = ""
with open(encodedFile, 'r', encoding='utf-8') as fileobj:
    for line in fileobj:  
        for ch in line: 
            book += ch

firstChar = 32
lastChar = 127
firstDecode = RailFence.descodifica(book, len(password))
decoded = auric.decode(firstDecode, password, firstChar, lastChar)

if os.path.isfile(decodedFile):
    os.remove(decodedFile)

f = open(decodedFile, "a")
f.write(decoded)
f.close()

print("The file has been decoded into " + decodedFile + ", enjoy your secrets!")
