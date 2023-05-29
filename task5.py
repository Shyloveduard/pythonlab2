from collections.abc import Hashable

def create_sets(input_list):
    output_set = set()
    for item in input_list:
        if isinstance(item, Hashable):
            output_set.add(item)
    return output_set

input_list = [3, 'ok', [1, 2], (True, False), {'flag': 1}]
output_set = create_sets(input_list)
print(output_set)