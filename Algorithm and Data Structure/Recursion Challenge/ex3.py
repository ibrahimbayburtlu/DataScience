def productofarray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productofarray(arr[1:])

print(productofarray(arr = [2,3,4,6,7,8,9,10]))