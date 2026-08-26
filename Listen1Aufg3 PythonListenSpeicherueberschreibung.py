liste1 = [1]*10
print(liste1)
liste2 = liste1 # gemeinsamer speicher
print(liste2)
liste1[0] = 13
print(liste1)
print(liste2)
#deshalb wird auch liste 2 geändert.