import Utils

# Generem el diccionari d'aparicions dels caràcters. 
#histogram, length = Utils.getCharactersDict("txt/words.txt")
#print(len(histogram.values()))

# histograma_mots = Utils.getWordsLengthDictSpaceSeparator("txt/codificat-modular.txt")
# print(histograma_mots)


codificat = "_~^wCGR(\f*lPyK,bIo~foZE*zrN&pP7{gT|JC-sGCwKmN9x%nT1"
descodificat = ""
i = 0
last = 0
for c in codificat: 
    print("---------------------------------------------------")
    valorCodificat = ord(c)
    if i != 0:
        print(str(valorCodificat) + " -> " + str(last))
        if valorCodificat > last: 
            print(chr(valorCodificat - last))
            descodificat += chr(valorCodificat - last)
        else: 
            print(chr(last - valorCodificat))
            descodificat += chr(last - valorCodificat)
    else: 
        print(str(c) + " -> " + str(valorCodificat))
    last = valorCodificat
    print("---------------------------------------------------")
    i += 1

print(descodificat + "****")