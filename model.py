import sqlite3

class AppBD():
    def __init__(self):
        self.connection = self.OpenConnection()
        self.create_table()

    def OpenConnection(self):
        try:
            connection = sqlite3.connect('database.db')
            return connection
        except sqlite3.Error as error:
            print("Failed to connect to database.", error)
            return None

    def create_table(self):
        create_table_query = '''CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            date DATE NOT NULL,
            payment TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL
            )'''
        try:
            cursor = self.connection.cursor()    
            cursor.execute(create_table_query)
            self.connection.commit()
            print("Table created successfully.")
        except sqlite3.Error as error:
            print("Failed to create table.", error)

    def insert_data(self, name, price, date, payment, description, status):
        insert_query = """INSERT INTO products(name, price, date, payment, description, status) VALUES(?, ?, ?, ?, ?, ?);"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query, (name, price, date, payment, description, status))
            self.connection.commit()
            print("Product inserted successfully.")
        except sqlite3.Error as error:
            print("Failed to enter data.", error)

    def select_all_products(self):
        select_query = "SELECT * FROM products"
        products = []
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query)
            products = cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to return products.", error)
        return products

    def update_products(self, products_id, name, price, date, payment, description, status):
        update_query = """UPDATE products SET name = ?, price  = ?, date = ?, payment = ?,  description = ?, status = ? WHERE id = ?"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_query, (name, price, date, payment, description, status, products_id))
            self.connection.commit()
            print("Product updated successfully.")
        except sqlite3.Error as error:
            print("Failed to update product.", error)

    def delete_products(self, products_id):
        delete_query = "DELETE FROM products WHERE id = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(delete_query, (products_id,))
            self.connection.commit()
            print("Product deleted successfully.")
        except sqlite3.Error as error:
            print("Failed to delete product.", error)
