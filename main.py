from product import Product
from inventory import Inventory
from database import create_database


# Create the SQLite database and tables
create_database()


# Create the Inventory object
inventory = Inventory()


def get_integer(message, minimum=None):
    while True:
        try:
            value = int(input(message))

            if (
                minimum is not None
                and value < minimum
            ):
                print(
                    f"Please enter a value "
                    f"greater than or equal to "
                    f"{minimum}."
                )
                continue

            return value

        except ValueError:
            print(
                "Invalid input. "
                "Please enter a whole number."
            )


def get_float(message, minimum=None):
    while True:
        try:
            value = float(input(message))

            if (
                minimum is not None
                and value < minimum
            ):
                print(
                    f"Please enter a value "
                    f"greater than or equal to "
                    f"{minimum}."
                )
                continue

            return value

        except ValueError:
            print(
                "Invalid input. "
                "Please enter a valid number."
            )


def get_text(message):
    while True:
        value = input(message).strip()

        if value == "":
            print(
                "This field cannot be empty."
            )
            continue

        return value


def show_menu():
    print("\n" + "=" * 55)
    print(" SMART INVENTORY & SALES MANAGEMENT SYSTEM")
    print("=" * 55)
    print("1. Add Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. View Low-Stock Products")
    print("6. Record a Sale")
    print("7. View Sales History")
    print("8. View Sales Dashboard")
    print("9. Exit")
    print("=" * 55)


def add_product():
    print("\nADD NEW PRODUCT")
    print("-" * 55)

    product_id = get_integer(
        "Enter product ID: ",
        minimum=1
    )

    name = get_text(
        "Enter product name: "
    )

    category = get_text(
        "Enter category: "
    )

    purchase_price = get_float(
        "Enter purchase price: ",
        minimum=0
    )

    selling_price = get_float(
        "Enter selling price: ",
        minimum=0
    )

    quantity = get_integer(
        "Enter quantity: ",
        minimum=0
    )

    reorder_level = get_integer(
        "Enter reorder level: ",
        minimum=0
    )

    product = Product(
        product_id,
        name,
        category,
        purchase_price,
        selling_price,
        quantity,
        reorder_level
    )

    inventory.add_product(product)


def search_product():
    search_value = get_text(
        "\nEnter product ID or "
        "product name: "
    )

    product = inventory.search_product(
        search_value
    )

    if product is not None:
        print(
            "\nProduct found successfully."
        )

        product.display_product()

    else:
        print("\nProduct not found.")


def update_stock():
    print("\nUPDATE PRODUCT STOCK")
    print("-" * 55)

    product_id = get_text(
        "Enter product ID: "
    )

    product = inventory.search_product(
        product_id
    )

    if product is None:
        print("\nProduct not found.")
        return

    print(
        f"\nProduct: {product.name}"
    )

    print(
        f"Current quantity: "
        f"{product.quantity}"
    )

    print("\n1. Add Stock")
    print("2. Remove Stock")

    while True:
        choice = input(
            "Choose an option: "
        ).strip()

        if choice in ["1", "2"]:
            break

        print(
            "Invalid option. "
            "Please enter 1 or 2."
        )

    quantity = get_integer(
        "Enter quantity: ",
        minimum=1
    )

    if choice == "1":
        quantity_change = quantity

    else:
        quantity_change = -quantity

    success, message = (
        inventory.update_stock(
            product_id,
            quantity_change
        )
    )

    print(f"\n{message}")

    if success:
        print(
            f"New quantity: "
            f"{product.quantity}"
        )


def view_low_stock_products():
    low_stock_products = (
        inventory.get_low_stock_products()
    )

    if len(low_stock_products) == 0:
        print(
            "\nAll products have "
            "sufficient stock."
        )
        return

    print("\nLOW-STOCK ALERT")
    print("=" * 80)

    for product in low_stock_products:
        print(
            f"ID: {product.product_id} | "
            f"Name: {product.name} | "
            f"Current Stock: "
            f"{product.quantity} | "
            f"Reorder Level: "
            f"{product.reorder_level}"
        )


def record_sale():
    print("\nRECORD A NEW SALE")
    print("-" * 55)

    product_id = get_text(
        "Enter product ID: "
    )

    product = inventory.search_product(
        product_id
    )

    if product is None:
        print("\nProduct not found.")
        return

    print(
        f"\nProduct: {product.name}"
    )

    print(
        f"Selling price: Rs. "
        f"{product.selling_price:.2f}"
    )

    print(
        f"Available stock: "
        f"{product.quantity}"
    )

    quantity_sold = get_integer(
        "Enter quantity sold: ",
        minimum=1
    )

    success, message, sale = (
        inventory.record_sale(
            product_id,
            quantity_sold
        )
    )

    print(f"\n{message}")

    if success:
        print("-" * 45)

        print(
            f"Product: "
            f"{sale['product_name']}"
        )

        print(
            f"Quantity sold: "
            f"{sale['quantity_sold']}"
        )

        print(
            f"Total amount: "
            f"Rs. "
            f"{sale['total_amount']:.2f}"
        )

        print(
            f"Total profit: "
            f"Rs. "
            f"{sale['total_profit']:.2f}"
        )

        print(
            f"Remaining stock: "
            f"{product.quantity}"
        )

        print("-" * 45)


def view_sales():
    inventory.view_sales()


def show_dashboard():
    data = (
        inventory.get_dashboard_data()
    )

    print("\nSALES DASHBOARD")
    print("=" * 55)

    print(
        f"Total Products: "
        f"{data['total_products']}"
    )

    print(
        f"Total Stock Units: "
        f"{data['total_stock_units']}"
    )

    print(
        f"Total Units Sold: "
        f"{data['total_units_sold']}"
    )

    print(
        f"Total Revenue: "
        f"Rs. "
        f"{data['total_revenue']:.2f}"
    )

    print(
        f"Total Profit: "
        f"Rs. "
        f"{data['total_profit']:.2f}"
    )

    if (
        data["best_selling_product"]
        is None
    ):
        print(
            "Best-Selling Product: "
            "No sales recorded"
        )

    else:
        print(
            f"Best-Selling Product: "
            f"{data['best_selling_product']}"
        )

    print("=" * 55)


# Main program loop
while True:
    show_menu()

    choice = input(
        "Enter your choice: "
    ).strip()

    if choice == "1":
        add_product()

    elif choice == "2":
        inventory.view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_stock()

    elif choice == "5":
        view_low_stock_products()

    elif choice == "6":
        record_sale()

    elif choice == "7":
        view_sales()

    elif choice == "8":
        show_dashboard()

    elif choice == "9":
        print(
            "\nThank you for using "
            "the system."
        )
        break

    else:
        print(
            "\nInvalid choice. "
            "Please enter a number "
            "from 1 to 9."
        )