from billing import sales
from product import products

def sales_report():
    if len(sales) == 0:
        print("No sales available.\n")
        return

    total_revenue = 0

    print("\n--- Sales Report ---")
    for sale in sales:
        print(f"{sale['product']} | Qty: {sale['quantity']} | Total: ₹{sale['total']}")
        total_revenue += sale['total']

    print(f"\nTotal Revenue: ₹{total_revenue}\n")


def low_stock_report():
    print("\n--- Low Stock Products ---")

    found = False

    for product in products:
        if product["stock"] <= 5:
            print(f"{product['name']} | Remaining Stock: {product['stock']}")
            found = True

    if not found:
        print("No low stock products.")

    print()