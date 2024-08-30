text = "  Hello, World!  "

# 1. .capitalize() - Capitalizes the first character of the string
print(f"capitalize(): '{text.capitalize()}'")  # Output: '  Hello, world!  '

# 2. .casefold() - Converts the string to lowercase, more aggressive than .lower()
print(f"casefold(): '{text.casefold()}'")  # Output: '  hello, world!  '

# 3. .center(width, fillchar) - Centers the string in a field of given width, padded with fillchar
print(f"center(20, '*'): '{text.center(20, '*')}'")  # Output: '****  Hello, World!  ****'

# 4. .count(substring) - Counts occurrences of substring
print(f"count('o'): {text.count('o')}")  # Output: 2

# 5. .encode(encoding) - Encodes the string using the specified encoding
print(f"encode('utf-8'): {text.encode('utf-8')}")  # Output: b'  Hello, World!  '

# 6. .endswith(suffix) - Checks if the string ends with the specified suffix
print(f"endswith('World!'): {text.endswith('World!')}")  # Output: True

# 7. .find(substring) - Returns the lowest index of substring if found, otherwise -1
print(f"find('World'): {text.find('World')}")  # Output: 8

# 8. .format(*args, **kwargs) - Formats the string using the provided arguments
formatted_string = "The value is: {} {} {}".format(42, 12, 53)
print(f"format(): '{formatted_string}'")  # Output: 'The value is: 42 12 53'
formatted_string = "The value is: {2} {1} {0}".format(42, 12, 53)
print(f"format(): '{formatted_string}'")  # Output: 'The value is: 53 12 42'
formatted_string = "The value is: {c} {b} {a}".format(a="Timon", b="and", c="Pumba")
print(f"format(): '{formatted_string}'")  # Output: 'The value is: Pumba and Timon'
name = Marcin
formatted_string = f"The value is: {name}"
print(formatted_string)  # Output: 'The value is: Marcin'



# 9. .isalpha() - Checks if all characters in the string are alphabetic
print(f"isalpha(): {text.isalpha()}")  # Output: False (because of spaces and punctuation)

# 10. .isdigit() - Checks if all characters in the string are digits
print(f"isdigit(): {'12345'.isdigit()}")  # Output: True

# 11. .isspace() - Checks if all characters in the string are whitespace
print(f"isspace(): {text.isspace()}")  # Output: False

# 12. .join(iterable) - Joins elements of an iterable with the string as a separator
words = ['Hello', 'World']
print(f"join(', '): '{', '.join(words)}'")  # Output: 'Hello, World'

# 13. .lstrip(chars) - Removes leading characters (default is whitespace)
print(f"lstrip(): '{text.lstrip()}'")  # Output: 'Hello, World!  '

# 14. .lower() - Converts the string to lowercase
print(f"lower(): '{text.lower()}'")  # Output: '  hello, world!  '

# 15. .replace(old, new, count) - Replaces occurrences of old with new
print(f"replace('World', 'Python'): '{text.replace('World', 'Python')}'")  # Output: '  Hello, Python!  '

# 16. .rfind(substring) - Returns the highest index of substring if found, otherwise -1
print(f"rfind('o'): {text.rfind('o')}")  # Output: 8

# 17. .rstrip(chars) - Removes trailing characters (default is whitespace)
print(f"rstrip(): '{text.rstrip()}'")  # Output: '  Hello, World!'

# 18. .split(separator, maxsplit) - Splits the string into a list using the specified separator
print(f"split(', '): {text.split(', ')}")  # Output: ['  Hello', 'World!  ']

# 19. .strip(chars) - Removes leading and trailing characters (default is whitespace)
print(f"strip(): '{text.strip()}'")  # Output: 'Hello, World!'

# 20. .title() - Capitalizes the first letter of each word
print(f"title(): '{text.title()}'")  # Output: '  Hello, World!  '

# 21. .upper() - Converts the string to uppercase
print(f"upper(): '{text.upper()}'")  # Output: '  HELLO, WORLD!  '

# 22. .zfill(width) - Pads the string on the left with zeros to reach the specified width
print(f"zfill(20): '{text.zfill(20)}'")  # Output: '000000000  Hello, World!  '

# 23. .startswith(prefix) - Checks if the string starts with the specified prefix
print(f"startswith('  Hello'): {text.startswith('  Hello')}")  # Output: True
