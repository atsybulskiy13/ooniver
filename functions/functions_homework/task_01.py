def min_max(*args):
    min_elem = min(args)
    max_elem = max(args)
    return min_elem, max_elem


elements = [1, 2, 3, 4, 5, 6, 7, 8]

min_element, max_element = min_max(*elements)
print(min_element)
print(max_element)
