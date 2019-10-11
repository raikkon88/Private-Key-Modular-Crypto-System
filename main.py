import matplotlib.pyplot as plt
from datetime import datetime
import auric
import RailFence

text = "zfaksjhdflkauehkaetal ukeyhtaksjdhlkathekjryh askdjhajtahsbdafba z z z"
#text = "zazaz"

print("Codifiquem : " + text)
encoded, key = auric.encode(text)
print("AURI = " + encoded + " -> " + str(key))
final = RailFence.codifica(encoded, key % 25)
print("FENCE = " + final + " -> " + str(key))

decoded = RailFence.descodifica(final, key % 25)
print("FENCE = " + decoded)
resultat = auric.decode(decoded, key)
print("AURI = " + resultat)
