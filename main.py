from product import Product
from inventory import Inventory


inventory = Inventory()


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
    print("\nAdd New Product")

    product_id = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    category = input("Enter category: ")
    purchase_price = float(input("Enter purchase price: "))
    selling_price = float(input("Enter selling price: "))
    quantity = int(input("Enter quantity: "))
    reorder_level = int(input("Enter reorder level: "))

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
    search_value = input(
        "\nEnter product ID or product name: "
    )

    product = inventory.search_product(search_value)

    if product is not None:
        print("\nProduct found successfully.")
        product.display_product()

    else:
        print("\nProduct not found.")


def update_stock():
    print("\nUpdate Product Stock")

    product_id = input("Enter product ID: ")

    product = inventory.search_product(product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print(f"\nProduct: {product.name}")
    print(f"Current quantity: {product.quantity}")

    print("\n1. Add Stock")
    print("2. Remove Stock")

    choice = input("Choose an option: ")

    quantity = int(input("Enter quantity: "))

    if choice == "1":
        quantity_change = quantity

    elif choice == "2":
        quantity_change = -quantity

    else:
        print("\nInvalid option.")
        return

    success, message = inventory.update_stock(
        product_id,
        quantity_change
    )

    print(f"\n{message}")

    if success:
        print(f"New quantity: {product.quantity}")


def view_low_stock_products():
    low_stock_products = inventory.get_low_stock_products()

    if len(low_stock_products) == 0:
        print("\nAll products have sufficient stock.")
        return

    print("\nLOW-STOCK ALERT")
    print("=" * 80)

    for product in low_stock_products:
        print(
            f"ID: {product.product_id} | "
            f"Name: {product.name} | "
            f"Current Stock: {product.quantity} | "
            f"Reorder Level: {product.reorder_level}"
        )


def record_sale():
    print("\nRecord a New Sale")

    product_id = input("Enter product ID: ")

    product = inventory.search_product(product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print(f"\nProduct: {product.name}")
    print(f"Selling price: Rs. {product.selling_price:.2f}")
    print(f"Available stock: {product.quantity}")

    quantity_sold = int(
        input("Enter quantity sold: ")
    )

    success, message, sale = inventory.record_sale(
        product_id,
        quantity_sold
    )

    print(f"\n{message}")

    if success:
        print("-" * 40)

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
            f"Rs. {sale['total_amount']:.2f}"
        )

        print(
            f"Total profit: "
            f"Rs. {sale['total_profit']:.2f}"
        )

        print(
            f"Remaining stock: "
            f"{product.quantity}"
        )

        print("-" * 40)


def view_sales():
    inventory.view_sales()


def show_dashboard():
    data = inventory.get_dashboard_data()

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
        f"Rs. {data['total_revenue']:.2f}"
    )

    print(
        f"Total Profit: "
        f"Rs. {data['total_profit']:.2f}"
    )

    if data["best_selling_product"] is None:
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


while True:
    show_menu()

    choice = input("Enter your choice: ")

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
        print("\nThank you for using the system.")
        break

    else:
        print("\nInvalid choice. Please try again.")