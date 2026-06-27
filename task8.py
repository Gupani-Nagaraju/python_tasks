from collections import deque

inventory = {}

recent_products = []

orders = deque()

def add_product(product, quantity):
    inventory[product] = (
        inventory.get(product, 0) + quantity
    )
    recent_products.append(product)

    print(
        f"{quantity} units of "
        f"{product} added."
    )


def view_inventory():
    print("\n----- Inventory -----")
    if not inventory:
        print("Inventory is Empty")
        return 
    else:
        for product, quantity in inventory.items():
            print(f"{product} : {quantity}")

    
def remove_recent_products():
    if not recent_products:
        print("No recent products were added.")

    else:
        recent_product = recent_products.pop()

        print(f"Recent Product is{recent_product}")


def add_orders(customer_name, product_name):
    orders.append((customer_name, product_name))
    print("Oreder successfully placed by",customer_name)

def process_order():
    if not orders:
        print("No orders to process")
        return 
    customer, product = orders.popleft()

    if inventory.get(product, 0) > 0:
        inventory[product] -= 1

        print(f"order processed for {customer}")
    else:
        print("Items out of stock")


add_product("Laptop", 5)
add_product("Mouse", 10)
add_product("Keyboard", 3)

view_inventory()

print("\nRecent Products Stack:")
print(recent_products)

remove_recent_products()

print("\nRecent Products Stack:")
print(recent_products)

add_orders("Ramesh", "Laptop")
add_orders("Suresh", "Mouse")
add_orders("Mahesh", "Monitor")

print("\nProcessing Orders")

process_order()
process_order()
process_order()

view_inventory()


    


