import itertools


for i in itertools.count(1):
    print("{0} is being tested".format(i))
    while i != 1:
        if i % 2 == 0:
            i = i / 2
        else:
            i = i * 3 + 1

