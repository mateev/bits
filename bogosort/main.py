from random import shuffle


def bogosort(listInput):
    'Sorts a list'
    while listInput!=sorted(listInput):
        shuffle(listInput)
