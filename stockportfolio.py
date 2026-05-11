# Hardcoded dictionary to define stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420
}

def build_portfolio():
    portfolio = {}
    total_investment = 0
    
    print("--- Stock Portfolio Tracker ---")
    print(f"Available stocks: {', '.join(stock_prices.keys())}\n")

    while True:
        symbol = input("Enter stock symbol (or type 'done' to finish): ").upper()
        
        if symbol == 'DONE':
            break
        
        if symbol in stock_prices:
            try:
                quantity = int(input(f"Enter quantity for {symbol}: "))
                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue
                
                # Calculate value for this specific stock
                price = stock_prices[symbol]
                item_total = price * quantity
                
                # Store in portfolio and update grand total
                portfolio[symbol] = {'quantity': quantity, 'total': item_total}
                total_investment += item_total
                
            except ValueError:
                print("Please enter a valid number for quantity.")
        else:
            print(f"Stock symbol '{symbol}' not found in our price list.")

    # Display results
    print("\n--- Portfolio Summary ---")
    for stock, data in portfolio.items():
        print(f"{stock}: {data['quantity']} shares | Value: ${data['total']}")
    
    print(f"\nTotal Investment Value: ${total_investment}")

    # Optional: Save result to a .txt file
    save_choice = input("\nWould you like to save this to a file? (y/n): ").lower()
    if save_choice == 'y':
        with open("portfolio_report.txt", "w") as f:
            f.write("Stock Portfolio Report\n")
            f.write("-" * 25 + "\n")
            for stock, data in portfolio.items():
                f.write(f"{stock}: {data['quantity']} shares - ${data['total']}\n")
            f.write("-" * 25 + "\n")
            f.write(f"Grand Total: ${total_investment}")
        print("Portfolio saved to 'portfolio_report.txt'.")

if __name__ == "__main__":
    build_portfolio()