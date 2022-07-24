def somerecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return somerecursive(arr[1:], cb)
    return True