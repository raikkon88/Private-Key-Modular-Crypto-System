from itertools import permutations

histograma = dict()
book = ""
with open("txt/codificat-modular.txt", 'r', encoding='utf-8') as fileobj:
    for line in fileobj:  
        for ch in line: 
            if ch >= chr(32) and ch <= chr(126): 
                if ch in histograma:
                    histograma[ch] += 1
                else: 
                    histograma[ch] = 1
length = len(histograma.keys())
print(length)
print(list(permutations(histograma.keys(), length)))

