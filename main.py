import product
import billing
import reports

while True:
    print("===== Mini Inventory Manager =====")
    print("1. Product Management")
    print("2. Billing System")
    print("3. Reports")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Product Module
    if choice == "1":
        while True:
            print("\n--- Product Management ---")
            print("1. Add Product")
            print("2. View Products")
            print("3. Delete Product")
            print("4. Back")

            p_choice = input("Enter choice: ")

            if p_choice == "1":
                product.add_product()

            elif p_choice == "2":
                product.view_products()

            elif p_choice == "3":
                product.delete_product()

            elif p_choice == "4":
                break

            else:
                print("Invalid choice.\n")

    # Billing Module
    elif choice == "2":
        billing.generate_bill()

    # Reports Module
    elif choice == "3":
        while True:
            print("\n--- Reports ---")
            print("1. Sales Report")
            print("2. Low Stock Report")
            print("3. Back")

            r_choice = input("Enter choice: ")

            if r_choice == "1":
                reports.sales_report()

            elif r_choice == "2":
                reports.low_stock_report()

            elif r_choice == "3":
                break

            else:
                print("Invalid choice.\n")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice.\n")