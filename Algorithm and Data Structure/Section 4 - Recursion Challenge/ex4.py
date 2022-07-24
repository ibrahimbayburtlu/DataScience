def recursiverange(num):
    if num == 1:
        return 1
    return num + recursiverange(num-1)