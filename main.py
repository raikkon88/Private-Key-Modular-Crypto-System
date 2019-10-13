#import matplotlib.pyplot as plt
#from datetime import datetime
import auric
import RailFence


key = "d"
text = "asdf"

firstChar = 32
lastChar = 127

print(lastChar - firstChar)


# matrix, columns, length = auric.generateMatrix(text, L)
encoded = auric.encode(text, key, firstChar, lastChar)
print(encoded)

print("----------------------------------------------")
#
decoded = auric.decode(encoded, key, firstChar, lastChar)
print(decoded)
#
##print(matrix)
#print(columns)
#print(length)
#print(len(matrix) * len(matrix[0]))



#text = "zazaz"

#print("Codifiquem : " + text)
#encoded, key = auric.encode(text)
#print("AURI = " + encoded + " -> " + str(key))
#final = RailFence.codifica(encoded, key % 25)
#print("FENCE = " + final + " -> " + str(key))

#decoded = RailFence.descodifica(final, key % 25)
#print("FENCE = " + decoded)
#resultat = auric.decode(decoded, key)
#print("AURI = " + resultat)
