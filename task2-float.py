value1 = 0.1
value2 = 0.2
result = value1 + value2
print("The result of adding", value1, "and", value2, "is:", result)
# This program adds two floating-point numbers and prints the result.
# The expected output is 0.3, but due to floating-point precision issues, it may print 0.30000000000000004.
# To mitigate this, we can use the round function to limit the number of decimal places.
if result == 0.3:
    print("The result is exactly 0.3")
else:
    print("The result is not exactly 0.3, it is:", round(result, 1))