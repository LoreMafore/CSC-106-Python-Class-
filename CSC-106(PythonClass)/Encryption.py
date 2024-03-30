import sympy

a = float(sympy.randprime(0, 100))
b = float(sympy.randprime(0, 100))

print("This is our first number", a)
print("This is our second number", b)

sum = a + b

# our first totent
totent = (a - 1) * (b - 1)

# our key
e = 0
while e == 0 or 5 or 10:
    if e == 0:
        # encryption
        d = (a ** e) * totent
        f = (b ** e) * totent
        print("\nencryption 1a:", d)
        print("encryption 1b:", f)

        # decryption
        ud = (d / totent) * a
        uf = (f / totent) * b
        print("decryption 1a:", round(ud))
        print("decryption 1b:", round(uf))

        # if it went through or not
        print("\nFinally .. !!")

        # continues on to the next key
        e += 5


    elif e == 5:
        # encryption
        d = (a ** e) * totent
        f = (b ** e) * totent
        print("\nencryption 2a:", d)
        print("encryption 2b:", f)

        # decryption
        ud = (d / totent) ** (1 / e)
        uf = (f / totent) ** (1 / e)
        print("decryption 2a:", round(ud))
        print("decryption 2b:", round(uf))
        # if it went through or not
        print("\nFinally !!")

        # continues on to the next key
        e += 5


    elif e == 10:
        # encryption
        d = (a ** e) * totent
        f = (b ** e) * totent
        print("\nencryption 3a:", d)
        print("encryption 3b:", f)

        # decryption
        ud = (d / totent) ** (1 / e)
        uf = (f / totent) ** (1 / e)
        print("decryption 3a:", round(ud))
        print("decryption 3b:", round(uf))
        # if it went through or not
        print("\nFinally !!")

        # continues on to the next key or gets out of the loop
        e += 5
