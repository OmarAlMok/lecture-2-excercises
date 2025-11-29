"""Implement the recursive Fibonacci sequence function, tracing the function calls for fib(4) to clearly illustrate the call stack and the base case """ 
def fib(n):
    ##computes with recursion the nth Fibonacci number
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
# Example usage
print("Fibonacci of 4:", fib(4))  # Output: Fibonacci of 4: 3