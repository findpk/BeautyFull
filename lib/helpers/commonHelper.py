import string
import random


def generateRandomString(length):
    return str(''.join(random.choices(string.ascii_uppercase + string.digits, k=length)))


def generateRandomNumber(length):
    range_start = 10**(length-1)
    range_end = (10**length)-1
    return random.randint(range_start, range_end)
