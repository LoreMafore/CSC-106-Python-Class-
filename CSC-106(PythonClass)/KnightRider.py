# importing libraries
import time
from termcolor import colored

# starting value of the while loop
a = 1

# defining all the terms so that only one light would be on at a given time
display_1 = colored(' ', 'red', attrs=['reverse', 'blink']) + colored(' ', 'black',
                                                                      attrs=['reverse', 'blink']) + colored(' ',
                                                                                                            'black',
                                                                                                            attrs=[
                                                                                                                'reverse',
                                                                                                                'blink']) + colored(
    ' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black', attrs=['reverse', 'blink']) + colored(' ',
                                                                                                            'black',
                                                                                                            attrs=[
                                                                                                                'reverse',
                                                                                                                'blink']) + colored(
    ' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black', attrs=['reverse', 'blink'])

display_2 = colored(' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'red',
                                                                        attrs=['reverse', 'blink']) + colored(' ',
                                                                                                              'black',
                                                                                                              attrs=[
                                                                                                                  'reverse',
                                                                                                                  'blink']) + colored(
    ' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black', attrs=['reverse', 'blink']) + colored(' ',
                                                                                                            'black',
                                                                                                            attrs=[
                                                                                                                'reverse',
                                                                                                                'blink']) + colored(
    ' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black', attrs=['reverse', 'blink'])

display_3 = colored(' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black',
                                                                        attrs=['reverse', 'blink']) + colored(' ',
                                                                                                              'red',
                                                                                                              attrs=[
                                                                                                                  'reverse',
                                                                                                                  'blink']) + colored(
    ' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black', attrs=['reverse', 'blink']) + colored(' ',
                                                                                                            'black',
                                                                                                            attrs=[
                                                                                                                'reverse',
                                                                                                                'blink']) + colored(
    ' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black', attrs=['reverse', 'blink'])

display_4 = colored(' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black',
                                                                        attrs=['reverse', 'blink']) + colored(' ',
                                                                                                              'black',
                                                                                                              attrs=[
                                                                                                                  'reverse',
                                                                                                                  'blink']) + colored(
    ' ', 'red', attrs=['reverse', 'blink']) + colored(' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black',
                                                                                                          attrs=[
                                                                                                              'reverse',
                                                                                                              'blink']) + colored(
    ' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black', attrs=['reverse', 'blink'])

display_5 = colored(' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black',
                                                                        attrs=['reverse', 'blink']) + colored(' ',
                                                                                                              'black',
                                                                                                              attrs=[
                                                                                                                  'reverse',
                                                                                                                  'blink']) + colored(
    ' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'red', attrs=['reverse', 'blink']) + colored(' ', 'black',
                                                                                                          attrs=[
                                                                                                              'reverse',
                                                                                                              'blink']) + colored(
    ' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black', attrs=['reverse', 'blink'])

display_6 = colored(' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black',
                                                                        attrs=['reverse', 'blink']) + colored(' ',
                                                                                                              'black',
                                                                                                              attrs=[
                                                                                                                  'reverse',
                                                                                                                  'blink']) + colored(
    ' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'red',
                                                                                                            attrs=[
                                                                                                                'reverse',
                                                                                                                'blink']) + colored(
    ' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black', attrs=['reverse', 'blink'])

display_7 = colored(' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black',
                                                                        attrs=['reverse', 'blink']) + colored(' ',
                                                                                                              'black',
                                                                                                              attrs=[
                                                                                                                  'reverse',
                                                                                                                  'blink']) + colored(
    ' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black', attrs=['reverse', 'blink']) + colored(' ',
                                                                                                            'black',
                                                                                                            attrs=[
                                                                                                                'reverse',
                                                                                                                'blink']) + colored(
    ' ', 'red', attrs=['reverse', 'blink']) + colored(' ', 'black', attrs=['reverse', 'blink'])

display_8 = colored(' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black',
                                                                        attrs=['reverse', 'blink']) + colored(' ',
                                                                                                              'black',
                                                                                                              attrs=[
                                                                                                                  'reverse',
                                                                                                                  'blink']) + colored(
    ' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'black', attrs=['reverse', 'blink']) + colored(' ',
                                                                                                            'black',
                                                                                                            attrs=[
                                                                                                                'reverse',
                                                                                                                'blink']) + colored(
    ' ', 'black', attrs=['reverse', 'blink']) + colored(' ', 'red', attrs=['reverse', 'blink'])

# while is < 4 so that it would only repeat 3 times
while a < 4:
    # turn on color from left to right
    for number in range(1, 10):

        if number == 1:
            print(display_1)
            time.sleep(.5)

        elif number == 2:
            print(display_2)
            time.sleep(.5)

        elif number == 3:
            print(display_3)
            time.sleep(.5)

        elif number == 4:
            print(display_4)
            time.sleep(.5)

        elif number == 5:
            print(display_5)
            time.sleep(.5)

        elif number == 6:
            print(display_6)
            time.sleep(.5)

        elif number == 7:
            print(display_7)
            time.sleep(.5)

        elif number == 8:
            print(display_8)
            time.sleep(.5)

        elif number == 9:
            # turn on color from right to left
            for number in reversed(range(0, 8)):
                if number == 1:
                    print(display_1)
                    time.sleep(.5)

                elif number == 2:
                    print(display_2)
                    time.sleep(.5)

                elif number == 3:
                    print(display_3)
                    time.sleep(.5)

                elif number == 4:
                    print(display_4)
                    time.sleep(.5)

                elif number == 5:
                    print(display_5)
                    time.sleep(.5)

                elif number == 6:
                    print(display_6)
                    time.sleep(.5)

                elif number == 7:
                    print(display_7)
                    time.sleep(.5)

                elif number == 0:
                    # addinga value to a so that the loop would restart up to 2 times
                    a += 1

        number += 1