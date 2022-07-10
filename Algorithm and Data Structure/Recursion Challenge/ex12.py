<<<<<<< HEAD
print("Hello World!")
=======
def capitalizewords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizewords(arr[1:])

arr = ["ı","am","ibo","your","name","is","deniz"]
print(capitalizewords(arr))
>>>>>>> b79210afeaa2f8b85b2201fa580451f74a5257fe
