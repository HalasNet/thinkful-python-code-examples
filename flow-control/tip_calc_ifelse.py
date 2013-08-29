import sys

meal = float(sys.argv[1])
tax_rate = float(sys.argv[2])
tip = float(sys.argv[3])
tax = tax_rate / 100.0
tax_value = meal * tax 
meal_with_tax = meal + tax_value
tip_value = meal * tip / 100.0

print "meal", meal
if meal > 50.0:
    print "You won a coupon for your next visit"
else:
    print "no coupon"

total = meal_with_tax + tip_value

print "The cost of your meal is {:0.2f}." .format(meal)
print "The cost of the tax is %0.2f" % tax_value 
print "Here's the amount of tip you'll need to pay: {tip_value:0.2f}".format(tip_value=tip_value)
print "Total amount: $%0.2f." % total 
