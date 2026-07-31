from product import Product
from database import save_product, load_products


class Inventory:
    def __init__(self):
        self.products = []
        self.sales = []

        self.load_products_from_database()

    def load_products_from_database(self):
        product_rows = load_products()

        for row in product_rows:
            product = Product(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )

            self.products.append(product)

    def add_product(self, product):
        existing_product = self.search_product(
            str(product.product_id)
        )

        if existing_product is not None:
            print(
                "\nA product with this ID "
                "already exists."
            )
            return

        save_product(product)

        self.products.append(product)

        print(
            "\nProduct added and saved "
            "to the database successfully."
        )

    def view_products(self):
        if len(self.products) == 0:
            print("\nNo products are available.")
            return

        print("\nALL PRODUCTS")
        print("=" * 90)

        for product in self.products:
            print(
                f"ID: {product.product_id} | "
                f"Name: {product.name} | "
                f"Category: {product.category} | "
                f"Quantity: {product.quantity} | "
                f"Price: Rs. "
                f"{product.selling_price:.2f}"
            )

    def search_product(self, search_value):
        search_value = search_value.lower()

        for product in self.products:
            if (
                str(product.product_id)
                == search_value
                or search_value
                in product.name.lower()
            ):
                return product

        return None

    def update_stock(
        self,
        product_id,
        quantity_change
    ):
        product = self.search_product(
            str(product_id)
        )

        if product is None:
            return False, "Product not found."

        new_quantity = (
            product.quantity
            + quantity_change
        )

        if new_quantity < 0:
            return (
                False,
                "Stock cannot be negative."
            )

        product.quantity = new_quantity

        return (
            True,
            "Stock updated successfully."
        )

    def get_low_stock_products(self):
        low_stock_products = []

        for product in self.products:
            if (
                product.quantity
                <= product.reorder_level
            ):
                low_stock_products.append(
                    product
                )

        return low_stock_products

    def record_sale(
        self,
        product_id,
        quantity_sold
    ):
        product = self.search_product(
            str(product_id)
        )

        if product is None:
            return (
                False,
                "Product not found.",
                None
            )

        if quantity_sold <= 0:
            return (
                False,
                "Quantity must be greater "
                "than zero.",
                None
            )

        if quantity_sold > product.quantity:
            return (
                False,
                "Not enough stock available.",
                None
            )

        total_amount = (
            product.selling_price
            * quantity_sold
        )

        profit_per_item = (
            product.selling_price
            - product.purchase_price
        )

        total_profit = (
            profit_per_item
            * quantity_sold
        )

        product.quantity -= quantity_sold

        sale = {
            "product_id":
                product.product_id,

            "product_name":
                product.name,

            "quantity_sold":
                quantity_sold,

            "total_amount":
                total_amount,

            "total_profit":
                total_profit
        }

        self.sales.append(sale)

        return (
            True,
            "Sale recorded successfully.",
            sale
        )

    def view_sales(self):
        if len(self.sales) == 0:
            print(
                "\nNo sales have been "
                "recorded."
            )
            return

        print("\nSALES HISTORY")
        print("=" * 90)

        for number, sale in enumerate(
            self.sales,
            start=1
        ):
            print(
                f"Sale #{number} | "
                f"Product: "
                f"{sale['product_name']} | "
                f"Quantity: "
                f"{sale['quantity_sold']} | "
                f"Amount: Rs. "
                f"{sale['total_amount']:.2f} | "
                f"Profit: Rs. "
                f"{sale['total_profit']:.2f}"
            )

    def get_dashboard_data(self):
        total_products = len(
            self.products
        )

        total_stock_units = 0

        for product in self.products:
            total_stock_units += (
                product.quantity
            )

        total_units_sold = 0
        total_revenue = 0
        total_profit = 0

        for sale in self.sales:
            total_units_sold += (
                sale["quantity_sold"]
            )

            total_revenue += (
                sale["total_amount"]
            )

            total_profit += (
                sale["total_profit"]
            )

        best_selling_product = None

        if len(self.sales) > 0:
            product_sales = {}

            for sale in self.sales:
                product_name = (
                    sale["product_name"]
                )

                quantity = (
                    sale["quantity_sold"]
                )

                if (
                    product_name
                    in product_sales
                ):
                    product_sales[
                        product_name
                    ] += quantity

                else:
                    product_sales[
                        product_name
                    ] = quantity

            best_selling_product = max(
                product_sales,
                key=product_sales.get
            )

        dashboard_data = {
            "total_products":
                total_products,

            "total_stock_units":
                total_stock_units,

            "total_units_sold":
                total_units_sold,

            "total_revenue":
                total_revenue,

            "total_profit":
                total_profit,

            "best_selling_product":
                best_selling_product
        }

        return dashboard_data