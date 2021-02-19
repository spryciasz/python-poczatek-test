from shop.order import create_new_order

def run_shop():
    print("Witaj w symulatorze sklepu")
    product_name = input("Jaki towar chcesz kupić? ")
    quantity = int(input("Ile chcesz tego kupić? "))

    result = create_new_order(product_name, quantity)
    if result is not None:
        total_price = result["total_price"]
        print(f"łączny koszt Twoich zakupów wyniesie {total_price}")

if __name__== "__main__":
    run_shop()
