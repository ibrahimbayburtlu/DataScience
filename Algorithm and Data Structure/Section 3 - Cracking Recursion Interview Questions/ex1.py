def sumdofigits(n):
    assert n >= 0 and int(n) == n, 'Our number will be greater than negative and integer'
    if n == 0:
        return 0
    return sumdofigits(int(n/10)) + n % 10  

print(sumdofigits(569037081))