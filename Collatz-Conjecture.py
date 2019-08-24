import itertools

for i in itertools.count(1):
    print("{0} is being tested".format(i))
    while i != 1:
        if i % 2 == 0:
            i = i / 2
        elif i % 2 != 0:
            i = i * 3 + 1
        else:
          print("{0} has failed the collatz conjecture. Possible solution discovered. ".format(i))
          f= open("counterexample.txt","w+")
          f.write("A possible counterexample has been found: " + i)
