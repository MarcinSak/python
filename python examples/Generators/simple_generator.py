def simple_gen(n):
    for i in range(n):
        yield i

if __name__ == "__main__":
    g = simple_gen(9)
    print(g)
    for i in range(3):
        print(next(g))

    for num in simple_gen(5):
        print(num)

    string = "QwErTyUiOp"
    iter_string = iter(string)
    for i in range(5):
        print(next(iter_string))