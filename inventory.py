class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("\nProduct added successfully.")

    def view_products(self):
        if len(self.products) == 0:
            print("\nNo products are available.")
            return

        print("\nAll Products")
        print("=" * 80)

        for product in self.products:
            print(
                f"ID: {product.product_id} | "
                f"Name: {product.name} | "
                f"Category: {product.category} | "
                f"Quantity: {product.quantity} | "
                f"Price: Rs. {product.selling_price}"
            )

    def search_product(self, search_value):
        search_value = search_value.lower()

        for product in self.products:
            if (
                str(product.product_id) == search_value
                or search_value in product.name.lower()
            ):
                return product

        return None

    def update_stock(self, product_id, quantity_change):
        product = self.search_product(str(product_id))

        if product is None:
            return False, "Product not found."

        new_quantity = product.quantity + quantity_change

        if new_quantity < 0:
            return False, "Stock cannot be negative."

        product.quantity = new_quantity

        return True, "Stock updated successfully."