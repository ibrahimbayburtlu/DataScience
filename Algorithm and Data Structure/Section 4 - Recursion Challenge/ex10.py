'''Write a recursive function called capitalizeFirst. Given an arrat of strings, capitalize the first letter of each string in the array.'''

def capitalsizefirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper()+ arr[0][1:])
    return result + capitalsizefirst(arr[1:])

print(capitalsizefirst(['car','taco','banana']))