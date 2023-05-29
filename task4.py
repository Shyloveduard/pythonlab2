def create_dict():
    my_dict = {str(num): num**2 for num in range(20, 31) if num % 3 == 0 and num % 5 != 0}
    return my_dict

my_dict = create_dict()
print(my_dict)