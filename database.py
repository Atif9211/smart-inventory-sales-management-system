import sqlite3


DATABASE_NAME = "inventory.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)

    return connection


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

    connection.commit()

    connection.close()

    print("Database and products table are ready.")


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