def stringifynumbers(obj):
    newobj = obj
    for key in newobj:
        if type(newobj[key]) is int:
            newobj[key] = str(newobj[key])
        if type(newobj[key]) is dict:
            newobj[key] = stringifynumbers(newobj[key])
    return newobj

obj = {
    "num1":1,
    "test":[],
    "data":{
        "val":4,
        "info":{
            "isRight":True,
            "random":66
        }
    }
}


print(stringifynumbers(obj))