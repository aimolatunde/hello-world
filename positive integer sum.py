# this program accepts a positive integer
# and then returns the sum of integers from
# 1 to the integer accepted
n = int(input("enter the number"))
if n > 0:
    total = n*(n+1)/2
    print("the sum of the fisrt", n, "positive integer is;", total)
else:
    print('the number you entered is not a positive integer')
