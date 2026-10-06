actual_cost = float(input("What is the actual product price "))
sale_amount = float(input("What is the sale amount of the product "))

if (sale_amount > actual_cost):
    profit = sale_amount - actual_cost
    print("The total profit is", profit)
else:
    print("No profit :(")