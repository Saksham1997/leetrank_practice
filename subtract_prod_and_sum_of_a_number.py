def subtractProductAndSum(n):
    n = list(str(n))
    Mul = "*".join(n)
    print(Mul)
    Sum = "+".join(n)
    print(Sum)
    #print("{}{}".format(Mul,Sum))
    return eval(Mul) - eval(Sum)

print(subtractProductAndSum(234))
