# import modules
import mysql.connector
from mysql.connector import Error
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
import base64
# AES key for encryption and decryption
encryption_key = get_random_bytes(16)

def establish_mysql_connection():
    try:
        connection = mysql.connector.connect(
            user="root", password="", host="127.0.0.1", port="3306", database="sales_system"
        )
        print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"The error '{e}' occurred while connecting to MySQL")

def initialize_cipher():
    return AES.new(encryption_key, AES.MODE_EAX)
# Establish MySQL connection
conn = establish_mysql_connection()
cursor = conn.cursor()

# Initialize encryption cipher
cipher = initialize_cipher()

def encrypt_text(text):
    cipher_text, tag = cipher.encrypt_and_digest(text.encode('utf-8'))
    return b64encode(cipher_text).decode('utf-8')
def decrypt_text(encrypted_text):
    try:
        # Add padding to the encrypted_text if needed
        padding_length = len(encrypted_text) % 4
        if padding_length > 0:
            encrypted_text += '=' * (4 - padding_length)
        # Convert the input to bytes using UTF-8 encoding
        encrypted_bytes = encrypted_text.encode('utf-8')
        # Decode base64
        cipher_text = base64.b64decode(encrypted_bytes)
        # Represent each byte as a pair of hexadecimal characters
        hex_result = ''.join(f'{byte:02x}' for byte in cipher_text)
        return hex_result
    except Exception as e:
        print(f"Error decrypting text: {e}")
        return ""
# menu section
def print_menu():
    print("1. View Inventory")
    print("2. View Customer Information")
    print("3. Record Sales")
    print("4. Exit")
#view inventory function
def view_inventory():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        print(product)
# view customer information function
def view_customer_info():
    cursor.execute("SELECT CustomerID, CustomerName, AccountInfo FROM customer")
    customers = cursor.fetchall()
    for customer in customers:
        customer_id, name, encrypted_account_info = customer
        # print("encrypted_account_info", encrypted_account_info)
        decrypted_info = decrypt_text(encrypted_account_info)
        print(f"CustomerID: {customer_id}, CustomerName: {name}, AccountInfo: {decrypted_info}")

def record_sales():
    customer_id = input("Enter Customer ID: ")
    product_id = input("Enter Product ID: ")
    quantity = int(input("Enter Quantity:"))
    # Query product table to get pricing
    cursor.execute("SELECT Cost FROM products WHERE ProductID=%s", (product_id,))
    result = cursor.fetchone()
    if result is not None:
        cost = result[0]
    else:
        print(f"Product with ID {product_id} not found.")
        return
    # Query customer table to get encrypted account information
    cursor.execute("SELECT AccountInfo FROM customer WHERE CustomerID=%s", (customer_id,))
    encrypted_account_info = cursor.fetchone()
    if encrypted_account_info is not None:
        encrypted_account_info = encrypted_account_info[0]
    else:
        print(f"Customer with ID {customer_id} not found.")
        return

    if not encrypted_account_info:
        print(f"Customer with ID {customer_id} does not have account information.")
        return
    # Decrypt account information using the stored encryption key
    try:
        decrypted_info = decrypt_text(encrypted_account_info)
    except Exception as e:
        print(f"Error decrypting account information for customer ID {customer_id}: {e}")
        return
    # Calculate total cost
    total_cost = quantity * cost
    # Update sales records
    cursor.execute("INSERT INTO sales (customer_id, product_id, quantity, total_cost) VALUES (%s, %s, %s, %s)",
                   (customer_id, product_id, quantity, total_cost))
    # Commit the changes
    conn.commit()
    print("Sales record updated successfully.")
# Main program loop
while True:
    print_menu()
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        view_inventory()
    elif choice == '2':
        view_customer_info()
    elif choice == '3':
        record_sales()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
# Close the MySQL connection
conn.close()
