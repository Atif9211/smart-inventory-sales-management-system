class Product:
    def __init__(
        self,
        product_id,
        name,
        category,
        purchase_price,
        selling_price,
        quantity,
        reorder_level
    ):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.purchase_price = purchase_price
        self.selling_price = selling_price
        self.quantity = quantity
        self.reorder_level = reorder_level

    def display_product(self):
        print("\nProduct Details")
        print("-" * 30)
        print(f"ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Purchase Price: Rs. {self.purchase_price}")
        print(f"Selling Price: Rs. {self.selling_price}")
        print(f"Quantity: {self.quantity}")
        print(f"Reorder Level: {self.reorder_level}")