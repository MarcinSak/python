# Numeric types
integer_value = 10               # Integer (int)
float_value = 3.14               # Floating point number (float)
complex_value = 2 + 3j           # Complex number (complex)

# Sequence types
string_value = "Hello, World!"   # String (str)
list_value = [1, 2, 3, 4, 5]     # List (list)
tuple_value = (1, 2, 3, 4, 5)    # Tuple (tuple)
range_value = range(5)           # Range (range)

# Set types
set_value = {1, 2, 3, 4, 5}      # Set (set)
frozenset_value = frozenset([1, 2, 3, 4, 5])  # Frozenset (frozenset)

# Mapping type
dict_value = {"a": 1, "b": 2, "c": 3}  # Dictionary (dict)

# Boolean type
boolean_value = True             # Boolean (bool)

# None type
none_value = None                # NoneType (None)

# Operations on data types

# Numbers
sum_value = integer_value + float_value  # Addition of integer and float
complex_conjugate = complex_value.conjugate()  # Conjugate of a complex number

# Strings
upper_string = string_value.upper()  # Convert string to uppercase

# Lists
list_value.append(6)  # Add an element to the list
list_length = len(list_value)  # Get the length of the list

# Tuples
first_element = tuple_value[0]  # Access the first element of the tuple

# Range
range_list = list(range_value)  # Convert range to a list

# Sets
set_value.add(6)  # Add an element to the set
is_subset = set_value.issubset({1, 2, 3, 4, 5, 6})  # Check if set is a subset

# Frozenset
is_frozen_subset = frozenset_value.issubset({1, 2, 3, 4, 5, 6})  # Check if frozenset is a subset

# Dictionaries
dict_value["d"] = 4  # Add a new key-value pair to the dictionary
keys = dict_value.keys()  # Get all keys from the dictionary

# Boolean
negate_boolean = not boolean_value  # Negate the boolean value

# None type
is_none = none_value is None  # Check if the value is None

# Print results
print(f"Integer value: {integer_value}")
print(f"Float value: {float_value}")
print(f"Complex value: {complex_value}")
print(f"String value: {string_value}")
print(f"List value: {list_value}")
print(f"Tuple value: {tuple_value}")
print(f"Range value: {range_list}")
print(f"Set value: {set_value}")
print(f"Frozenset value: {frozenset_value}")
print(f"Dictionary value: {dict_value}")
print(f"Boolean value: {boolean_value}")
print(f"None value: {none_value}")

print("\nOperations:")
print(f"Sum of integer and float: {sum_value}")
print(f"Conjugate of complex value: {complex_conjugate}")
print(f"Uppercase string: {upper_string}")
print(f"Length of list: {list_length}")
print(f"First element of tuple: {first_element}")
print(f"Is set a subset: {is_subset}")
print(f"Is frozenset a subset: {is_frozen_subset}")
print(f"Dictionary keys: {keys}")
print(f"Negated boolean: {negate_boolean}")
print(f"Is None: {is_none}")
