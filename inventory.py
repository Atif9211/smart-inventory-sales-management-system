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