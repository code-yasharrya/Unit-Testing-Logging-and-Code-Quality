
import logging

from order import calculate_order_total


logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)


def process_order(price, discount):
    logging.debug(
        "Starting order calculation: price=%s, discount=%s",
        price,
        discount,
    )

    try:
        total = calculate_order_total(price, discount)

        logging.info("Order processed successfully: total=%s", total)

        if discount == 0:
            logging.warning("No discount applied to this order")

        return total

    except ValueError as error:
        logging.error("Order processing failed: %s", error)
        return None


if __name__ == "__main__":
    process_order(1000, 10)
    process_order(500, 0)
    process_order(-100, 10)

    print("Logging completed. Check application.log")
