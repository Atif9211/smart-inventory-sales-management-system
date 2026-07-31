import sqlite3


DATABASE_NAME = "inventory.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            purchase_price REAL NOT NULL,
            selling_price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            reorder_level INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            quantity_sold INTEGER NOT NULL,
            total_amount REAL NOT NULL,
            total_profit REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()

    print("Database tables are ready.")


def save_product(product):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO products (
            product_id,
            name,
            category,
            purchase_price,
            selling_price,
            quantity,
            reorder_level
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        product.product_id,
        product.name,
        product.category,
        product.purchase_price,
        product.selling_price,
        product.quantity,
        product.reorder_level
    ))

    connection.commit()
    connection.close()


def load_products():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            product_id,
            name,
            category,
            purchase_price,
            selling_price,
            quantity,
            reorder_level
        FROM products
        ORDER BY product_id
    """)

    products = cursor.fetchall()

    connection.close()

    return products


def update_product_quantity(
    product_id,
    new_quantity
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE products
        SET quantity = ?
        WHERE product_id = ?
    """, (
        new_quantity,
        product_id
    ))

    connection.commit()
    connection.close()


def update_product(product):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE products
        SET
            name = ?,
            category = ?,
            purchase_price = ?,
            selling_price = ?,
            quantity = ?,
            reorder_level = ?
        WHERE product_id = ?
    """, (
        product.name,
        product.category,
        product.purchase_price,
        product.selling_price,
        product.quantity,
        product.reorder_level,
        product.product_id
    ))

    connection.commit()
    connection.close()


def delete_product(product_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM products
        WHERE product_id = ?
    """, (
        product_id,
    ))

    connection.commit()
    connection.close()


def save_sale(sale):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO sales (
            product_id,
            product_name,
            quantity_sold,
            total_amount,
            total_profit
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        sale["product_id"],
        sale["product_name"],
        sale["quantity_sold"],
        sale["total_amount"],
        sale["total_profit"]
    ))

    connection.commit()
    connection.close()


def load_sales():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            sale_id,
            product_id,
            product_name,
            quantity_sold,
            total_amount,
            total_profit
        FROM sales
        ORDER BY sale_id
    """)

    sales = cursor.fetchall()

    connection.close()

    return sales