#define the menu of restaurant

menu= {
    'Pizza': 100,
    'Pasta': 90,
    'Burgur':70,
    'Salad': 100,
    'Coffee': 80,
}

#Greet
print("Wlcome to CHURI Restaurant ")
print("Pizaa: Rs100\nPasta: Rs90\nBurgur: Rs70\nSalad: Rs100\nCoffee: Rs80")

order_total = 0

item1= input("Enter the name of item you want to order = ")
if item1 in menu:
    order_total += menu[item1]
    print(f'Your item {item1} has been added to your order')

else:
    print(f'Order item {item1} is not available yet!')

another_order = input("Do you want to add another item? (Yea/No)")
if another_order == "Yes":
    item2= input("Enter the name of second item =")
    if item2 in menu:
        order_total += menu[item2]
        print(f'Item {item2} has been added to order')
    else:
        print(f'Ordered item {item2} is not available!')    

print(f'The total amount of item to pay is {order_total}')       