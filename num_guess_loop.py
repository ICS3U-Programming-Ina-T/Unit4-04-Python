#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Jan. 11, 2022
# This program generates a random number
# and then uses a while true loop to ask
# the user until they guess correctly.
# It also uses a break statement to stop
# the program.

import random


# replicates a do..while loop
# uses a break statement
def main():
    # initialize the loop counter
    loop_counter = 0

    # sets the random number
    random_number = random.randint(0, 9)

    while True:
        # get the user number as a string
        user_number_string = input("Enter a whole number between 0 and 9: ")

        try:
            # converts user input to integer
            user_number_int = int(user_number_string)

            if user_number_int >= 0 and user_number_int <= 9:
                # increments the counter
                loop_counter = loop_counter + 1
                if user_number_int == random_number:
                    # display result to user
                    print("")
                    print("{} is correct! Congratulations!".
                          format(user_number_int))
                    break
                else:
                    # display result to user
                    print("{} is incorrect.".
                          format(user_number_int))
                    print("")
                    print("Tracking {0} times through the loop.".
                          format(loop_counter))
                    print("")
            else:
                print("This is not within the range!")
                print("")
        # catches any exceptions
        except Exception:
            print("{} is invalid.". format(user_number_string))
            print("")


if __name__ == "__main__":
    main()
