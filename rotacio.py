# INPUT N
# OUTPUT : 
# - Genera N nombres aleatoris entre 1 i 100 
# - Classifica aquests nombres en base 5 
# - Mostra un gràfic de les classificacions
import sys
import random

def generaNNombres(N):
    generated = list()
    i = 0
    for i in range(int(N)):
        generated.append(random.randint(1,100))
    return generated

N = sys.argv[1]

print("Generem " + str(N) + " nombres aleatoris i els classifiquem : ")
x = generaNNombres(N)

appearances = dict()
start = 0
for number in x:
    if start % 5 in appearances.keys():
        appearances[start % 5] += 1
    else:
        appearances[start % 5] = 1
    start += number

print(appearances)

