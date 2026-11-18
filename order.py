
def calculate_discount(price, discount_percent):
    """Calculate the discount amount."""
    if price < 0:
        raise ValueError("Price cannot be negative")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")

    return price * discount_percent / 100


def calculate_gst(amount, gst_percent=18):
    """Calculate GST on an amount."""
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if not 0 <= gst_percent <= 100:
        raise ValueError("GST percentage must be between 0 and 100")

    return amount * gst_percent / 100


def calculate_order_total(price, discount_percent=0, gst_percent=18):
    """Calculate the final order total after discount and GST."""
    discount = calculate_discount(price, discount_percent)
    discounted_price = price - discount
    gst = calculate_gst(discounted_price, gst_percent)

    return round(discounted_price + gst, 2)


if __name__ == "__main__":
    price = 1000
    discount = 10
    gst = 18

    total = calculate_order_total(price, discount, gst)

    print("Original Price:", price)
    print("Discount:", discount, "%")
    print("GST:", gst, "%")
    print("Final Order Total: ₹", total)
