def get_no_of_airports():
    """Get number of airports from user and validate input."""
    while True:
        try:
            no_airports = int(input("Enter the number of airports (0 to exit): "))
            if no_airports > 300 or no_airports < 0:
                print("The number must be between 1 and 300.")
            else:
                break
        except ValueError:
            print("This must be a valid number.")
            
    return int(no_airports)

def calculate_budget(no_airports):
    """calculate buded needed to win a game base on number of airports needed to win"""
    sum = 0 # start sum
    price = 800
    for i in range(no_airports):
        sum += price
        price *= 1.05

    return sum

if __name__ == "__main__":
    while True:        
        no_airports = get_no_of_airports()
        if no_airports == 0:
            print("EXIT")
            break
        budget = int(calculate_budget(no_airports))
        print(f"$ {budget:,.0f}".replace(",", " ") + ".-")
