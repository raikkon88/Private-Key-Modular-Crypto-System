import random
def fibonacci(n):
# Donat un n
# Retorn el nombre n-essim de la sèrie de fibonacci
    if n < 0: 
        raise Exception("Fibonnacci of " + str(n) + " does not exists.")
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def generateAppearances(fibonacci300, L):
# Donada una llista de nombres i un valor L
# Genera un hash on : 
# - clau : valor del nombre a Z/L
# - valor : llista de nombres congruents amb clau a Z/L
    appearences = dict()
    for i in fibonacci300:
        number = i % L
        if number in appearences:
            appearences[number].append(i)
        else:
            appearences[number] = [i]
    return appearences

def circularless(start, n):
# Donats start i n enters positius
# retorna start - n % 300
    for i in range(n):
        start -= 1
        if start < 0: 
            start = 299
    return start


def printAppearances(appearances, L):
# Donat un diccionari en forma d'histograma i un L enter positiu
# Mostra appearances per la sortida estàndard. 
    i = 0
    for i in range(L):
        print("|" + str(i) + "| = " + str(len(appearances[i])) + " -> " + str(appearances[i]))

def printMatrix(matrix):
# Donada una matriu de valors enters
# Mostra la matriu per la sortida estàndard
    for i in range(len(matrix)):
        result = str(i) + " -> " 
        for j in range(len(matrix[i])):
            result += str(matrix[i][j])
    print(result)

def generateMatrix(L, random):
# Donada L com enter positiu i random com a llavor
# Genera una matriu quadrada d'un rang aleatori de nombres de L * L caselles on : 
# - Cada columna significa el nombre a Z/L
# - Els valors de les columnes son tots congruents amb el valor de la mateixa columna. 
    start = random.randint(1, 10000000000000) 
    stop = random.randint(1, 1000000000000000000000000000000000000000000000000)
    if start > stop: 
        tmp = start
        start = stop
        stop = tmp
    matrix = list()
    i = 0
    while i < L:
        matrix.append(list())
        while len(matrix[i]) < L:
            if start % L == i:
                matrix[i].append(start)
            start += 1
        i += 1
    return matrix

def encode(text, key, firstChar, lastChar):
# Donats text per xifrar, key com a clau, firstChar i lastChar com valors decimals dels caràcters que defineixen el rang de la taula ascii a processar
# Retorna un nou string amb tots els caràcters entre firstChar i lastChar de text codificats amb key
    L = lastChar - firstChar 
    random.seed(key, version=2)
    matrix = generateMatrix(L, random)
    length = len(matrix) * len(matrix[0])
    result= ""
    counter = random.randint(0, length)
    i = 0
    for char in text:
        if ord(char) >= firstChar and ord(char) <= lastChar: 
            numb = matrix[counter % L][counter // L]
            valueZN = numb % L 
            result += chr(valueZN + firstChar) 
            counter += ord(char)
            counter = counter % length
        else: 
            result += char
        i += 1

    last = 0
    while matrix[counter % L][counter // L] % L != 0:
        last += 1
        counter += 1

    result += chr(last + firstChar)
    

    return result


def inRange(char, first, last): 
# Donats char com a caràcter, first i last com enters positius (valors decimals de caràcters)
# Retorna cert si char està dins del rang que delimiten first i last, fals altrament
    return (ord(char) >= first and ord(char) <= last)

def decode(cryptedText, key, firstChar, lastChar):
# Donats cryptedText per desxifrar, key com a clau, firstChar i lastChar com valors decimals dels caràcters que defineixen el rang de la taula ascii a processar
# Retorna un nou string amb tots els caràcters entre firstChar i lastChar de cryptedText descodificats amb key
    L = lastChar -  firstChar 
    random.seed(key, version=2)
    matrix = generateMatrix(L, random)
    length = len(matrix) * len(matrix[0])
    unciferedResult = ""
    start = random.randint(0, length) + firstChar 
    textLength = len(cryptedText) - 1
    i = 0
    while i < len(cryptedText) - 1: 

        stop = start + L % length

        while i < textLength and not inRange(cryptedText[i], firstChar, lastChar):
            unciferedResult += cryptedText[i]
            i += 1

        j = i + 1

        tmp = ""
        while j < textLength and not inRange(cryptedText[j], firstChar, lastChar):
            tmp = tmp + cryptedText[j]
            j += 1        

        
        if j < textLength and i < textLength:
            c2 = ord(cryptedText[j]) - firstChar
            counter = 0
            while start != stop and matrix[start % L][start // L] % L != c2:
                counter += 1
                start += 1 
                start = start % length
            start += firstChar
            start = start % length
            unciferedResult += chr(counter + firstChar) + tmp


        elif j >= textLength  and i < textLength:
            # Tinc start a la penúltima lletra, processem el separador. 
            last = start + ord(cryptedText[j])
            while matrix[last % L][last // L] % L != 0:
                last += 1
                last = last % length
            
            unciferedResult += chr(last - ord(cryptedText[j]) - start + 1 - firstChar) + tmp
        # else: 
            # Nothing to do ... print("els altres casos ")
       
        i = j

    return unciferedResult
