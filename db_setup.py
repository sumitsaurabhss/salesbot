import mysql.connector
from mysql.connector import Error

def setup_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        if conn.is_connected():
            cursor = conn.cursor()

            cursor.execute("CREATE DATABASE IF NOT EXISTS multiagent_sales_db")
 
            cursor.execute("USE multiagent_sales_db")


            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    category VARCHAR(50),
                    price DECIMAL(10, 2)
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE,
                    address TEXT
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sales (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    product_id INT,
                    customer_id INT,
                    quantity INT,
                    sale_date DATE,
                    revenue DECIMAL(10, 2),
                    FOREIGN KEY (product_id) REFERENCES products(id),
                    FOREIGN KEY (customer_id) REFERENCES customers(id)
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    sale_id INT,
                    transaction_date TIMESTAMP,
                    payment_method VARCHAR(50),
                    FOREIGN KEY (sale_id) REFERENCES sales(id)
                )
            """)

            cursor.execute("""
                INSERT INTO products (name, category, price) VALUES
                ('Laptop', 'Electronics', 999.99),
                ('Smartphone', 'Electronics', 699.99),
                ('Headphones', 'Electronics', 199.99),
                ('T-shirt', 'Clothing', 19.99),
                ('Jeans', 'Clothing', 49.99)
            """)

            cursor.execute("""
                INSERT INTO customers (name, email, address) VALUES
                ('John Doe', 'john@gmail.com', '123 Main St, City, Country'),
                ('Jane Smith', 'jane@gmail.com', '456 Elm St, City, Country'),
                ('Bob Johnson', 'bob@gmail.com', '789 Oak St, City, Country'),
                ('Alice Brown', 'alice@gmail.com', '321 Pine St, City, Country'),
                ('Charlie Wilson', 'charlie@gmail.com', '654 Maple St, City, Country')
            """)

            cursor.execute("""
                INSERT INTO sales (product_id, customer_id, quantity, sale_date, revenue) VALUES
                (1, 1, 1, '2024-01-15', 999.99),
                (2, 2, 2, '2024-01-20', 1399.98),
                (3, 3, 1, '2024-02-05', 199.99),
                (4, 4, 3, '2024-02-10', 59.97),
                (5, 5, 2, '2024-03-01', 99.98)
            """)

            cursor.execute("""
                INSERT INTO transactions (sale_id, transaction_date, payment_method) VALUES
                (1, '2024-01-15 10:30:00', 'Credit Card'),
                (2, '2024-01-20 14:45:00', 'PayPal'),
                (3, '2024-02-05 09:15:00', 'Debit Card'),
                (4, '2024-02-10 16:20:00', 'Cash'),
                (5, '2024-03-01 11:00:00', 'Credit Card')
            """)

            conn.commit()
            print("Database setup completed successfully.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        database="multiagent_sales_db",
        user="root",
        password="root"
    )
    return conn

if __name__ == "__main__":
    setup_database()
