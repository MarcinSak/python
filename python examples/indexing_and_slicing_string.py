# Example string
text = "Hello, World!"


first_char = text[0]
print(f"First character: {first_char}")  # Output: 'H'

last_char = text[-1]
print(f"Last character: {last_char}")  # Output: '!'

middle_char = text[7]
print(f"Middle character: {middle_char}")  # Output: 'W'

# Slicing examples

substring1 = text[0:5]
print(f"Substring (0:5): {substring1}")  # Output: 'Hello'

substring2 = text[:5]
print(f"Substring (:5): {substring2}")  # Output: 'Hello'

substring3 = text[7:]
print(f"Substring (7:): {substring3}")  # Output: 'World!'

substring4 = text[-6:-1]
print(f"Substring (-6:-1): {substring4}")  # Output: 'World'

# Slicing with a step

substring5 = text[::2]
print(f"Substring with step 2: {substring5}")  # Output: 'Hlo ol!'

reversed_text = text[::-1]
print(f"Reversed string: {reversed_text}")  # Output: '!dlroW ,olleH'
