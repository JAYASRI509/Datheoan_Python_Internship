import csv

stocks = []

print("================================")
print(" STOCK PORTFOLIO TRACKER")
print("================================")

n = int(input("Enter number of stocks: "))

for i in range(n):

    print("\nEnter Stock Details", i + 1)

    name = input("Enter stock name: ")
    quantity = int(input("Enter number of shares: "))
    buy_price = float(input("Enter purchase price: "))
    current_price = float(input("Enter current price: "))

    investment = quantity * buy_price
    current_value = quantity * current_price
    profit_loss = current_value - investment

    stocks.append([
        name, quantity, buy_price,
        current_price, investment,
        current_value, profit_loss
    ])

print("\n========== PORTFOLIO REPORT ==========")

total_investment = 0
total_value = 0

for stock in stocks:

    print("\nStock Name:", stock[0])
    print("Quantity:", stock[1])
    print("Investment:", stock[4])
    print("Current Value:", stock[5])
    print("Profit/Loss:", stock[6])

    total_investment += stock[4]
    total_value += stock[5]

print("\n========== SUMMARY ==========")

print("Total Investment:", total_investment)
print("Total Current Value:", total_value)

total_profit = total_value - total_investment

print("Total Profit/Loss:", total_profit)

if total_profit > 0:
    print("Status: PROFIT")
elif total_profit < 0:
    print("Status: LOSS")
else:
    print("Status: NO PROFIT NO LOSS")

with open("portfolio.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Stock Name", "Quantity", "Buy Price",
        "Current Price", "Investment",
        "Current Value", "Profit/Loss"
    ])

    writer.writerows(stocks)

print("\nPortfolio saved successfully!")