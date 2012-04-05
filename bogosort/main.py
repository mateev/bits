from random import shuffle
from random import seed

def bogosort(listInput):
    'Sorts a list; returns how many iterations did it take'
    count = 0
    seed()
    while listInput!=sorted(listInput):
        shuffle(listInput)
        count += 1
    return count

def bogosortNoCount(listInput):
    'Sorts a list'
    bogosort(listInput)
