#This code checks calculates the amount
price=float(input("Enter the price of the item: "))
quantity=int(input("Enter the quantity of the item: "))
amt = price * quantity
if amt > 10000:
    discount = amt * 0.25
else:
    discount = amt * 0.10

final_amt= amt - discount

print(f"The final amount after discount is: {final_amt:.2f}")
