import math

def solve_quadratic(a, b, c):
    quad = math.sqrt(math.pow(b, 2) - 4 * a * c)
    root1 = (-b + quad) / 2 * a
    root2 = (-b - quad) / 2 * a

    if root1 == root2:
        return 1, [root1]
    else:
        return 2, [root1, root2]


def solve_quadratic2(a, b, c):
    quad = math.sqrt(math.pow(b, 2) - 4 * a * c)
    sgn = 1 if b > 0 else 0 if b == 0 else -1

    root1 = (-b - sgn * quad) / 2 * a
    root2 = c / (a * root1)

    if math.isclose(root1, root2):
        return 1, [root1]
    else:
        return 2, [root1, root2]



def check_root(a, b, c, root):
    value = math.pow(a * root, 2) + b * root + c
    return value == 0

a = 1
b = -10000000.0000001
c = 1
numOfRoots, roots = solve_quadratic2(a, b, c)


print(roots)
print(roots[0].__str__() + " " + check_root(a, b, c, roots[0]).__str__())
print(roots[1].__str__() + " " + check_root(a, b, c, roots[1]).__str__())