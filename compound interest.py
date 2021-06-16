i = 0.04
cap = float(input("enter your capital"))
n = int(input("for how many years?"))
interest = cap*(1+i)**n
print("your compounded interest in", n, "years is %.2f" % interest)
