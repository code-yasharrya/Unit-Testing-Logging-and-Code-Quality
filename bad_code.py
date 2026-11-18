def calculate_total(price, quantity):
    total = price * quantity
    return total


def show_result():
    price = 100
    quantity = 5
    result = calculate_total(price, quantity)
    print("Total:", result)


show_result()
