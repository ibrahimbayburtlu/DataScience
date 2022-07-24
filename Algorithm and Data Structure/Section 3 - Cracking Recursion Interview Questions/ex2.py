def power(base,exp):
    assert exp >=0 and int(exp) == exp, 'base has a positive and exp only int'
    if exp == 0:
        return 1
    return base * power(base,exp-1)
print(power(-4,5))