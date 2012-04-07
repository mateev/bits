from main import bogosort
from random import random
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("%s <<length of array>> <<upper bound to memebers>>" % sys.argv[0])
        exit(1)

    length, random_range = map(int, sys.argv[1:3])
    to_be_sorted = [int(random()*random_range) for _ in range(length)]

    print("Sorting %s" % to_be_sorted)
    iterations = bogosort(to_be_sorted)
    from quoter import quotes
    print("It took just %d iterations to sort." % iterations)
    print(quotes[iterations % len(quotes)])
