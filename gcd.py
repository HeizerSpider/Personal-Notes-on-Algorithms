def gcd(a, b):
    while b!=0:
        buffer = a
        a = b
        b = buffer%b
    return a



print(gcd(11,10))