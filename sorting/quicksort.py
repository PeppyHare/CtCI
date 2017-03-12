def quicksort(input_list):
    less = []
    equal = []
    greater = []

    if len(input_list) > 1:
        pivot = input_list[0]
        for x in input_list:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quicksort(less) + equal + quicksort(
            greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your input_list, just return the input_list.
        return input_list
