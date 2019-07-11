def variable_count():
    variable = 0
    while 1:
        variable = variable + 1
        yield variable
        print("{0} has been tested".format(variable))


def ccs():
    for i in variable_count():
        while i != 1:
            if i % 2 == 0:
                i = i / 2
            else:
                i = i * 3 + 1

ccs()
