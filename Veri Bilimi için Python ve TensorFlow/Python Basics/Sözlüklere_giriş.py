benimListem = [1,2,3]

print(benimListem[0])

# Key - Value pairing (anahtar kelime - değer eşleşmesi)

benimYemeklerim = ["elma","Karpuz","Muz"]

benimKalorilerim = [100,200,300]

print(benimYemeklerim[1])


# Dictionary 

benimSözlük = {"anahtarKelime" : "deger"}


print(benimSözlük)
print(type(benimSözlük))

print(benimSözlük["anahtarKelime"])


benimYemekKaloriSözlük = {"elma" : 100 , "karpuz" : 200 , "muz" : 300}

print(benimYemekKaloriSözlük["muz"])

print(benimYemekKaloriSözlük)

benimDegisikSözlük = {1:"atıl", 2:"atlas"}

print(benimDegisikSözlük[1])


yeniDictionary = {"anahtar1" : 100 , "anahtar2" : [10,20,30,40,5,"atıl"],"anahtar3" : {"anahtar9" : 4}}

print(yeniDictionary["anahtar1"])

print(yeniDictionary.keys())

print(yeniDictionary.values())
