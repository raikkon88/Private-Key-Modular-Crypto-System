#import matplotlib.pyplot as plt
#from datetime import datetime
import auric
import RailFence

def doAction(fileName, key, firstChar, lastChar):
    text = ""
    with open(fileName, 'r', encoding='utf-8') as fileobj:
        for line in fileobj:  
            for ch in line: 
                text += ch

    # matrix, columns, length = auric.generateMatrix(text, L)
    print("")
    encoded = auric.encode(text, key, firstChar, lastChar)
    print("ENCODED TEXT By SUBSTITUTION :")
    print("-----------------------------------------------")
    print(encoded)

    print("")
    fenced = RailFence.codifica(encoded, len(key))
    print("ENCODED TEXT By SUBSTITUTION + TRANSFORMATION :")
    print("-----------------------------------------------")
    print(fenced)

    print("")
    defenced = RailFence.descodifica(fenced, len(key))
    print("DECODED TEXT By SUBSTITUTION + TRANSFORMATION :")
    print("-----------------------------------------------")
    print(defenced)

    print("")
    decoded = auric.decode(defenced, key, firstChar, lastChar)
    print("DECODED TEXT By SUBSTITUTION + TRANSFORMATION :")
    print("-----------------------------------------------")
    print(decoded)


key = "frankenstain"
firstChar = 32
lastChar = 127
shortFileName = "txt/short.txt"
doAction(shortFileName, key, firstChar, lastChar)

print("-----------------------------------------------------------------------------------------------------")

longFileName = "txt/long.txt"
doAction(longFileName, key, firstChar, lastChar)
