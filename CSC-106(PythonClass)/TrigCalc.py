# imports math for use of trig functions
import math

while True:
    # determining what equation the person wants
    eqs = input(
        "Do you want to use the trig calculator or the normal calculator? \nType trig for the trig calculator and normal for the noraml calculator: ")

    # once you determine that they want to use the normal calculator, I asked for two numbers anf a sign
    if eqs == "normal":
        a = input("First Number: ")
        ad = a.isnumeric()

        sign = input("Sign(+,-,/,*, ^): ")

        b = input("Second Number: ")
        bd = b.isnumeric()

        # With the two numbers and the sides I made conditions that the numbers had to be numbers in range between...
        # 0-9. I also made that for whatever sign was chosen it made be use the sign in conjunction of the two numbers.

        if ad == 1.0 and int(a) >= 0 and int(a) <= 9 and bd == 1 and int(b) >= 0 and int(b) <= 9 and sign == "+":
            print(int(a) + int(b))
            break

        elif ad == 1.0 and int(a) >= 0 and int(a) <= 9 and bd == 1 and int(b) >= 0 and int(b) <= 9 and sign == "-":
            print(int(a) - int(b))
            break

        elif ad == 1.0 and int(a) >= 0 and int(a) <= 9 and bd == 1 and int(b) >= 0 and int(b) <= 9 and sign == "/":
            print(int(a) / int(b))
            break

        elif ad == 1.0 and int(a) >= 0 and int(a) <= 9 and bd == 1 and int(b) >= 0 and int(b) <= 9 and sign == "*":
            print(int(a) * int(b))
            break

        elif ad == 1.0 and int(a) >= 0 and int(a) <= 9 and bd == 1 and int(b) >= 0 and int(b) <= 9 and sign == "^":
            print(int(a) ** int(b))
            break

        # I did not put a break here so you do not have to manually restart the program if you made a syntax mistake
        else:
            print("\nTRY AGAIN")
    # once you determine that they want to use the trig calculator, you ask for what trig function are they going...
    # to use and what number for x
    elif eqs == "trig":
        trigsign = input("Trig Function(sin,cos,tan): ")

        d = input("x: ")
        dd = d.isnumeric()

        # Now with the wanted trig function and the number we can set conditions. I made conditions that the...
        # numbers had to be numbers in range between 0-9. And that whatever trig function was chosen it would...
        # be used on the given inputed number

        if dd == 1.0 and int(d) >= 0 and int(d) <= 9 and trigsign == "sin":
            print("The sin in radians is ", math.sin(int(d)))
            break

        elif dd == 1.0 and int(d) >= 0 and int(d) <= 9 and trigsign == "cos":
            print("The cos in radians is", math.cos(int(d)))
            break

        elif dd == 1.0 and int(d) >= 0 and int(d) <= 9 and trigsign == "tan":
            print("The tan in radians is", math.tan(int(d)))
            break

        # I did not put a break here so you do not have to manually restart the program if you made a syntax mistake
        else:
            print("\nTRY AGAIN")

    # I did not put a break here so you do not have to manually restart the program if you made a syntax mistake
    else:
        print("\nTRY AGAIN")

