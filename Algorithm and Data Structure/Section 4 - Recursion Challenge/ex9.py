def flatten(arr):
    resultarr = []
    for custitem in arr:
        if type(custitem) is list:
            resultarr.extend(flatten(custitem))
        else: 
            resultarr.append(custitem)
    return resultarr 
print(flatten([2,[[4]],[5],[[8]]]))