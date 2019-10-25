import math
import matplotlib.pyplot as plt

def obteNum(text):
# retorna un enter corresponent al desplaçament d'un simple xifrat tipus Cèsar
    desp = input(text)
    return int(desp) 

def ic_calculation(file, first_char, last_char):
# Donat un fitxer file, el valor del primer caràcter, el valor de l'ultim caràcter a la taula ascii
# Retorna l'IC que s'ha calculat d'aquell fitxer. 
    histograma = dict()
    text_length = 0
    with open(file, 'r', encoding='utf-8') as fileobj:
        for line in fileobj:  
            for ch in line: 
                text_length += 1
                if ch >= chr(first_char) and ch <= chr(last_char): 
                    if ch in histograma:
                        histograma[ch] += 1
                    else: 
                        histograma[ch] = 1

    # Nombre de caràcters de llenguatge
    L=len(histograma.keys())
    print("L=" + str(L))
    suma = 0
    for value in histograma.values():
        suma += value * (value - 1)
    ic = L * suma / (text_length * (text_length - 1))
    return ic

def entrophy(file):
# Donat un fitxer d'entrada file
# Cerquem el valor per l'entropia del text del fitxer.  
    print(file)

def getCharactersDict(file):
# Donat un fitxer d'entrada file
# Retorna un diccionari dels caràcters i les seves aparicions i la llargada de file en caràcters. 
    histograma = dict()
    text_length = 0
    with open(file, 'r', encoding='utf-8') as fileobj:
        for line in fileobj:  
            for ch in line: 
                text_length += 1
                if ch >= chr(32) and ch <= chr(126): 
                    if ch in histograma:
                        histograma[ch] += 1
                    else: 
                        histograma[ch] = 1
    return histograma, text_length

def getWordsLengthDict(file): 
# Donat un fitxer d'entrada file
# Retorna un diccionari amb clau llargada de paraula i valor aparicions de mots amb llargada de paraula
    histograma = dict()
    max = 0
    with open(file, 'r', encoding='utf-8') as fileobj:
        for line in fileobj:  
            word = line[:-1]
            length = len(word)
            if length in histograma:
                histograma[length] += 1
            else: 
                histograma[length] = 1

            if length > max: 
                max = length

    return histograma, max

def getWordsLengthDictSpaceSeparator(file):
# Donat un fitxer
# Retorna tots els mots en un diccionari d'aparicions per llargada de mot, considerem mot el que estigui separat per \n i ' '
    histograma = dict()
    max = 0
    with open(file, 'r', encoding='utf-8') as fileobj:
        for line in fileobj:  
            words = line[:-1].split()
            for word in words: 
                length = len(word)
                if length in histograma:
                    histograma[length] += 1
                else: 
                    histograma[length] = 1

                if length > max: 
                    max = length

    return histograma, max

def getr(n, N):
# Donat: 
# n com a nombre de paraules de mida N i N 
# retorna el valor de r. 
    return math.log(n, 2) / N

def evalDictionary(dictionary, max):
# Donat un hashmap amb clau |paraula| i valor |aparicions| de paraules de llargada |paraula|
# Retorna : 
# - vector de valors de r
# - vector de |paraula|'s assignades als valors de r
    rs = []
    i = 1
    for i in dictionary.keys():
        #print("---------------------------------------------------")
        #print("| " + str(i))
        #print("| " + str(getr(dictionary[i], i)))
        #print("---------------------------------------------------")
        rs.append(getr(dictionary[i], i))
    return rs

def getAbsoluteRatio(L):
# Donat L com el nombre de caràcters de l'alfabet
# Retorna la ràtio absoluta del llenguatge (R)
    return math.log(L, 2)


def plotGraphic(rs, lengths, title, x, y):
# Donades rs com a llistat de valors de r i lengths com a llargades
# Mostra el gràfic de de valors de r en funció de les llargades. 
    plt.plot(rs, lengths, "ro")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.grid(True)
    plt.show()