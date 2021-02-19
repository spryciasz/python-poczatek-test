# W innym zaimplementuj funkcję, która na podstawie nazwy produktu i zamawianej ilości stworzy nowe zamówienie
# i doda je do listy zamówień. Zamówienie składa się z nazwy produktu, zamówionej ilości i łącznej ceny.

from shop.products_store import products, update_product_quantity

orders = [
    {
        "name": "chleb",
        "quantity": 10,
        "price": 35
    }
]

def create_new_order(product_name, quantity):
    price = products[product_name]["price"]
    available_quantity = products[product_name]["quantity"]

    if available_quantity < quantity:
        print("Brak towaru")
        return None

    total_price = price * quantity
    new_order = {
        "product": product_name,
        "quantity": quantity,
        "total_price": total_price
    }
    update_product_quantity(product_name, quantity)
    orders.append(new_order)
    return new_order
