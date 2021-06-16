# p this will calculate the number of bottles returned and
# determine their incentive
# there are two categories of bottles <= 1 litre set as type a
# and >1 litre as type b
bot_type_a = 0.10
bot_type_b = 0.25
small = int(
    input("enter the number of bottles you have that are 1 Litre or below"))
big = int(input("enter the number of bottles you have that are bigger than 1 litre"))
com = (small*bot_type_a) + (big*bot_type_b)
print("your commision amounts to $%.2f." % com)
