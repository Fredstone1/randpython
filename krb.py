import fractions

def krb(b1,b2,n1,n2):

    # n1 er første mod, n2 er anden mod
    #  x kongruent 7 mod 15 & x kongruent 14 mod 16
    # kan skrives krb(7,14,15,16)
    tmp1 = n1
    tmp2 = n2
    if n2 > n1:
        n1 = tmp2
        n2 = tmp1

    r = n2
    x = n1
    s = z = 0;
    t = y = 1
    while r:
        q = int(x / r)
        x, r = r, int(x % r)
        y, s = s, int(y - q * s)
        z, t = t, int(z - q * t)

    u1 = int(y%(n2/x))
    u2 = int(z%(-n1/x))

    xp = u1 * n1 * b1 + u2*n2*b2

    prod = n1*n2

    string = str(xp%prod) + ' + '+ str(prod) + ' Z'

    return string

print(krb(7,14,15,16))