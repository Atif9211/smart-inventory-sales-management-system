from product import Product
from inventory import Inventory


inventory = Inventory()


def show_menu():
    print("\n" + "=" * 50)
    print(" SMART INVENTORY & SALES MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Exit")
    print("=" * 50)


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
        print("\nThank you for using the system.")
        break

    else:
        print("\nInvalid choice. Please try again.")