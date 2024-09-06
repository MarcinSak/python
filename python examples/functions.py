def replace_in_list(to_be_replaced, replace_for, list_to_proceed):
    new_list = list_to_proceed
    for index, element in enumerate(list_to_proceed):
        if element == to_be_replaced:
            new_list[index] = replace_for
    return new_list