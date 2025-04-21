print("-"*47)
print("Welcome to supermarket billing system")
print("-"*47)

name=input("Please enter your name: " )
# Dictionary containing items and their respective prices
list_of_items={"Colgate": 90.0,
               "Eggs": 60.0,
               "Milk": 30.0,
               "Curd": 45.0,
               "Soap": 75.0,
               "Detergent": 120.0,
               "waterbottle": 25.0,
               "Dairymilk": 80.0,
               "Potatos": 35.0,
               "Maggi": 105.0,
               "Ricebag": 1015.0,
               "Panner": 100.0,
               "Salt": 20.0,
               "Sugar": 45.0,
               }
print("-"*47)
print("LIST OF ITEMS         PRICE(INR)")
print("-"*47)
# Display available items with their prices
for i,j in list_of_items.items():
    print("{:15} {:15}".format(i,j))

print("-"*47)
cart = {}
# Item selection loop
while True:
    item_name = input("Enter item name (or type 'done' to finish): ").title()

    if item_name.lower() == 'done':
        break

    if item_name in list_of_items:
        try:
            qty = int(input(f"Enter quantity for {item_name}: "))
             # If item already in cart, add quantity; else, add new entry
            if item_name in cart:
                cart[item_name] += qty
            else:
                cart[item_name] = qty
        except ValueError:
            print("Please enter a valid number for quantity.")
    else:
        print("Invalid item name. Please try again.")

# Print final bill
print("\n" + "-" * 47)
print(f"Customer Name: {name}")
print("BILL SUMMARY")
print("-" * 47)
total = 0

for item, qty in cart.items():
    price = list_of_items[item]
    item_total = price * qty
    total += item_total
    print("{:15} x {:2} = INR {:.2f}".format(item, qty, item_total))
#.2f means: display it as a floating-point number with 2 decimal places

print("-" * 47)
print("TOTAL AMOUNT: INR {:.2f}".format(total))
print("-" * 47)
print("Thank you for shopping with us!")
