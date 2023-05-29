def unique_elements(input_list):
    return list(set(x for x in input_list))

my_list = [1, 2, 3, 2, 4, 3, 5]
unique_list = unique_elements(my_list)
print(unique_list)