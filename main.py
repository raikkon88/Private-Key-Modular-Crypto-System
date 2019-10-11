import matplotlib.pyplot as plt
from datetime import datetime
import auric

#text = "zfaksjhdflkauehkaetal ukeyhtaksjdhlkathekjryh askdjhajtahsbdafba z z z"
text = "zazaz"
encoded, key = auric.encode(text)
print(encoded + " -> " + str(key))
decoded = auric.decode(encoded, key)
print(decoded)
