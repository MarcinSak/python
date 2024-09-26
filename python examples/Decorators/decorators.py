def function_decotation(function_name):
    def decorate():
        print("-- Prefix decoration")
        function_name()
        print("-- Sufix decoration")
    return decorate

def function_wich_need_decoration():
    print("Main Function")

@function_decotation
def function_wich_need_decoration_two():
    print("Second Function")


if __name__ == "__main__":
    decorated_function = function_decotation(function_wich_need_decoration)
    decorated_function()

    print("------------------------")

    function_wich_need_decoration_two()