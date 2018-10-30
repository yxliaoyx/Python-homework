def Factorial(x):
    return x if x == 1 else x * Factorial(x - 1)


def C(m, n):
    return Factorial(m) // Factorial(n) // Factorial(m - n)


print(C(49, 6))
# 13983816

print(C(100, 50))
# 100891344545564193334812497256

print(C(200, 100))
# 90548514656103281165404177077484163874504589675413336841320
