import itertools as it
import operator as op
def equal_to_24(a,b,c,d):
    numbers = [a, b, c, d]
    symbols = ["+", "-", "*", "/"]
    operations = [op.add, op.sub, op.mul, op.truediv]
    for num in it.permutations(numbers):
        for ops in it.product(operations, repeat = 3):
            try:
                value = ops[2](ops[0](num[0], num[1]), ops[1](num[2], num[3]))
                if value == 24:
                    return (f"({num[0]} {symbols[operations.index(ops[0])]} {num[1]}) {symbols[operations.index(ops[2])]} "
                            f"({num[2]} {symbols[operations.index(ops[1])]} {num[3]})")
            except ZeroDivisionError:
                pass
            try:
                if ops[2](ops[1](ops[0](num[0], num[1]), num[2]), num[3]) == 24:
                    return f"((({num[0]} {symbols[operations.index(ops[0])]} {num[1]}) {symbols[operations.index(ops[1])]} {num[2]}) {symbols[operations.index(ops[2])]} {num[3]})"
            except ZeroDivisionError:
                pass
            try:
                if ops[2](ops[0](num[0], ops[1](num[1], num[2])), num[3]) == 24:
                    return f"({num[0]} {symbols[operations.index(ops[0])]} ({num[1]} {symbols[operations.index(ops[1])]} {num[2]})) {symbols[operations.index(ops[2])]} {num[3]}"
            except ZeroDivisionError:
                pass
            try:
                if ops[0](num[0], ops[2](ops[1](num[1], num[2]), num[3])) == 24:
                    return f"{num[0]} {symbols[operations.index(ops[0])]} (({num[1]} {symbols[operations.index(ops[1])]} {num[2]}) {symbols[operations.index(ops[2])]} {num[3]})"
            except ZeroDivisionError:
                pass
            try:
                if ops[0](num[0], ops[1](num[1], ops[2](num[2], num[3]))) == 24:
                    return f"{num[0]} {symbols[operations.index(ops[0])]} ({num[1]} {symbols[operations.index(ops[1])]} ({num[2]} {symbols[operations.index(ops[2])]} {num[3]}))"
            except ZeroDivisionError:
                pass
    return "It's not possible!"


result = equal_to_24(1, 2, 3, 4)
print(result)
