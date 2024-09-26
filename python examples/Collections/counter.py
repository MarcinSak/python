from collections import Counter
if __name__ == "__main__":
    list = [1,1,2,3,3,'s','s','a']
    print(Counter(list))
    print(Counter('asssddfff')) 

    data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana', 'apple']

    counter = Counter(data)

    print(counter)

    total_count = counter.total()
    print(f"Total count of all elements: {total_count}")