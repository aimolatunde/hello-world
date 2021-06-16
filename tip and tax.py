cost = float(input("Enter the cost of food ordered"))
# tax rrate = 7.5%
# tip rate is 18%
tax = cost * .075
tip = cost * 0.18
total_cost = cost + tax + tip
print("Grand total = $%.2f" % total_cost)
