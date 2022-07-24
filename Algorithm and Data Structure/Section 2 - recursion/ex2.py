def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Our number must be greater than negative and integer' 
    if n in [0,1]:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))