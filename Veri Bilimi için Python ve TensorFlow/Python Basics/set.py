benimListem = [1,2,3,1,2,3]

print(benimListem[0])

# List -> Set
benimListeSetim = set(benimListem)
print(benimListeSetim)

# Set => Kümeler 
benimSet = {"b","c","a"}

print(type(benimSet))


bosListe = []
print(bosListe)
bosListe.append(1)

bosSet = {}
print(type(bosSet)) # dict olarak kabul etti.
print(bosSet)

# Set bu şekilde boş oluşturulur.
benimBosSet = set()

benimBosSet.add(10)
benimBosSet.add(20)
print(benimBosSet)
