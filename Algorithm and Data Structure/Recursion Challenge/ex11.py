
<<<<<<< HEAD
=======
# nestedEvenSum Solution

>>>>>>> b79210afeaa2f8b85b2201fa580451f74a5257fe
obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

def nestedevensum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedevensum(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
            sum+=obj[key]
<<<<<<< HEAD
    return sum

print(nestedevensum(obj2))
=======

print(nestedevensum(obj1))
>>>>>>> b79210afeaa2f8b85b2201fa580451f74a5257fe
