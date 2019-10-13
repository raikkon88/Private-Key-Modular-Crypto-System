import random
def fibonacci(n):
    if n < 0: 
        raise Exception("Fibonnacci of " + str(n) + " does not exists.")
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def generateAppearances(fibonacci300, L):
    appearences = dict()
    for i in fibonacci300:
        number = i % L
        if number in appearences:
            appearences[number].append(i)
        else:
            appearences[number] = [i]
    return appearences

def circularless(start, n):
    for i in range(n):
        start -= 1
        if start < 0: 
            start = 299
    return start


def printAppearances(appearances, L):
    i = 0
    for i in range(L):
        print("|" + str(i) + "| = " + str(len(appearances[i])) + " -> " + str(appearances[i]))

def printMatrix(matrix):
    for i in range(len(matrix)):
        result = str(i) + " -> " 
        for j in range(len(matrix[i])):
            result += str(matrix[i][j])
    print(result)

def generateMatrix(L, random):
# Donada una clau s'ha de poder generar una llavor. 
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
    return (ord(char) >= first and ord(char) <= last)

def decode(cryptedText, key, firstChar, lastChar):
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
