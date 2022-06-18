
def gcd(a,b):
    assert int(b) == b and int(a) == a, 'Number has positive integers'
    if a < 0:
        a = -1 *a
    if b < 0:
        b = -1*b
    if b == 0:
        return a
    return gcd(b,a%b)

print(gcd(45,18))