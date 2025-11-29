"""
Write a function with a variable named x, and an outer script with a global variable x. Inside the function, print x and explain which scope's x was used based on the LEGB rule.
"""
x = "global x"
def outer_function():
    x = "enclosing x"
    def inner_function():
        x = "local x"
        print("Inside inner_function:") # This will print the local x
    inner_function()
    print("Inside outer_function:") # This will print the enclosing x

outer_function()
print("In global scope:", x) # This will print the global x
print("Explanation: According to the LEGB rule, the inner_function first looks for x in its local scope, then in the enclosing scope (outer_function), and finally in the global scope.")   

