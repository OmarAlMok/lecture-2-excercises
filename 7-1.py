## Exc1: Compute the average with error handling
def compute_average(data_lists):
    ## computes the average of a grade handling empty lists
    if not data_lists:
        return 0
    return sum(data_lists) / len(data_lists)

# Example usage
grades = [85, 90, 78, 92]
grades_empty = []
print("Average of grades:", compute_average(grades))  # Output: Average of grades: 86.25
print("Average of empty list:", compute_average(grades_empty))  # Output: Average of empty list: 0

