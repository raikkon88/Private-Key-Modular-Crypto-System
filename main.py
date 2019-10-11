import matplotlib.pyplot as plt
from datetime import datetime
import auric

text = "faksjhdflkauehkaetalukeyhtaksjdhlkathekjryhaskdjhajtahsbdafba"
encoded, key = auric.encode(text)
print(encoded + " -> " + str(key))
decoded = auric.decode(encoded, key)
print(decoded)
