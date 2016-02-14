#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result


def main():
    print repeat(sys.argv[1], True)      ## YayYayYay
    print repeat(sys.argv[2], False)   ## Woo HooWoo HooWoo Hoo!!!


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()