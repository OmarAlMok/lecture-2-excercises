""" Use a for loop with the range() function and an if statement to print all even numbers between 1 and 50, then rewrite it using a single while loop."""
# Using for loop with range() and if statement
for number in range(1, 51):
    if number % 2 == 0:
        print(number)
# Using a single while loop
number = 2
while number <= 50:
    print(number)
    number += 2
    indexes = self.list_view.selectedIndexes()
    if indexes:
        self.model.complete(indexes[0].row())
        self.list_view.clearSelection() 


