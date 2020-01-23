# This is a simple calculator application,
# that makes division and returns the answer as well as the remainder

# we meet our user
name = input("Enter your name: ")
name = name.capitalize()  # This capitalizes the first letter
name = name.upper()  # This capitalizes the entire string
print("\nHello {}, welcome to this app.\n".format(name))

# now we explain the app to the user
print("This is a calculator for divisions,\nenter your values to get the result as well as the remainder.\n")

# now we collect the data
dividend = int(input("Enter the dividend (numerator):\n\t"))
divisor = int(input("Enter the divisor (denominator):\n\t"))

# we do the calculations
quotient = dividend//divisor  # in this line, we removed any decimal places
remainder = dividend % divisor  # this line contains the remainder

# now we display our result
print(dividend, "divided by", divisor, ",\tis:", quotient, "remaining:", remainder)

# END
print("\n")
input("Press enter to quit...")
