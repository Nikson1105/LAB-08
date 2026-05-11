from product import products

sales = []

def generate_bill():
    if len(products) == 0:
        print("No products available.\n")
        return

    print("\n--- Available Products ---")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product['name']} | Price: ₹{product['price']} | Stock: {product['stock']}")

    choice = int(input("\nSelect product number: ")) - 1

    if choice < 0 or choice >= len(products):
        print("Invalid choice.\n")
        return

    quantity = int(input("Enter quantity: "))

    selected_product = products[choice]

    if quantity > selected_product["stock"]:
        print("Insufficient stock.\n")
        return

    total = quantity * selected_product["price"]

    selected_product["stock"] -= quantity

    sale = {
        "product": selected_product["name"],
        "quantity": quantity,
        "total": total
    }

    sales.append(sale)

    print("\n------ Invoice ------")
    print("Product :", selected_product["name"])
    print("Quantity:", quantity)
    print("Total   : ₹", total)
    print("---------------------\n")