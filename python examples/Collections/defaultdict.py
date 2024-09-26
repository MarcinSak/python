from collections import defaultdict
if __name__ == "__main__":
    normal_dict = {'a': 1, 'b': 2, 'c': 3}
    print(normal_dict)
    print(normal_dict['a'])
    try:
        print(normal_dict['s'])
    except KeyError as e:
        print(f"KeyError: {e}")
    print("- - - -  -")

    d_dict = defaultdict(lambda: 0)
    print(d_dict)
    print(d_dict['s'])
    print(d_dict)

    words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    word_count = defaultdict(int)
    for word in words:
         word_count[word] += 1
    print("\nWord Count:")
    print(word_count)