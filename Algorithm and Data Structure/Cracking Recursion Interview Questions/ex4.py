def decimaltobinary(n):
    assert int(n) == n , 'The parameter must be an integer only'
    if n < 2:
        return 1
    return n % 2 + 10 * decimaltobinary(n//2)

print(decimaltobinary(13))
