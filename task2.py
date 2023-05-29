def filter_squares(lst):
    return [x for x in lst if x**2 <= 30]

numbers = [1, 2, 5, 6];
print(filter_squares(numbers));