import Utils

# Generem el diccionari d'aparicions dels caràcters. 
#histogram, length = Utils.getCharactersDict("txt/words.txt")
#print(len(histogram.values()))

histograma_mots = Utils.getWordsLengthDictSpaceSeparator("txt/codificat-modular.txt")
print(histograma_mots)