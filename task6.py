"""Read a monetary value from the user (as a string), convert it to a float, and use f-string formatting to display it rounded to two decimal places and prefixed with a dollar sign."""

value= input("Enter a monetary value: ")
amount = float(value)

print(f"${amount:.2f}")
