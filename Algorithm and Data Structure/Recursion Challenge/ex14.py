def collectstrings(obj):
    resultarr = []
    for key in obj:
        if type(obj[key]) is str:
            resultarr.append(obj[key])
        if type(obj[key]) is dict:
            resultarr = resultarr + collectstrings(obj[key])
    return resultarr