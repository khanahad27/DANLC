#4.Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.
#Taking the input from the user.
C = int(input("Enter the Numeric code (1 for battery-based, 2 for key-based toys, 3 for charging-based):"))
order_amount = float(input("Enter the Amount:"))
discount = int(0)
net_amount = int(0)
#Applying the conditions
if C == 1:
    if order_amount > 1000:
        discount = (0.10 * order_amount)
        net_amount = order_amount - discount
        print("The amount after the discount is",net_amount)
    else:
        print("Discount is not applicable.")
        print("Amount =",order_amount)
elif C == 2:
    if order_amount > 100:
        discount = (0.05 * order_amount)
        net_amount = order_amount - discount
        print("The amount after the discount is",net_amount)
    else:
        print("Discount is not applicable.")
        print("Amount =",order_amount)
elif C == 3:
    if order_amount > 500:
        discount = (0.10 * order_amount)
        net_amount = order_amount - discount
        print("The amount after the discount is",net_amount)
    else:
        print("Discount is not applicable.")
        print("Amount =",order_amount)
else:
    print("Invalid Code.")