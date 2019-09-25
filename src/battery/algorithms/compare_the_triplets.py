import operator

def compare(a, b):
    if a > b:
        return (1,0)
    elif a < b:
        return (0,1)

    return (0,0)

def add_tuples(a, b):
    return tuple(map(operator.add, a, b))

def solve(a0, a1, a2, b0, b1, b2):
    points = add_tuples(compare(a0,b0), compare(a1,b1))
    return add_tuples(points, compare(a2, b2))

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
