products = []

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter stock quantity: "))

    product = {
        "name": name,
        "price": price,
        "stock": stock
    }

    products.append(product)
    print("Product added successfully!\n")


def view_products():
    if len(products) == 0:
        print("No products available.\n")
        return

    print("\n--- Product List ---")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product['name']} | Price: ₹{product['price']} | Stock: {product['stock']}")
    print()


def delete_product():
    view_products()

    if len(products) == 0:
        return

    index = int(input("Enter product number to delete: ")) - 1

    if 0 <= index < len(products):
        removed = products.pop(index)
        print(f"{removed['name']} deleted successfully!\n")
    else:
        print("Invalid product number.\n")