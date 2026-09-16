import requests
import time


# Get crypto price from CoinGecko
def get_price(coin):

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": coin,
        "vs_currencies": "pkr"
    }

    try:
        response = requests.get(url,params=params,timeout=10)

        response.raise_for_status()

        data = response.json()

        if coin not in data:
            print("Coin not found!")
            return None

        return data[coin]["pkr"]

    except requests.RequestException as e:
        print(f"API error: {e}")
        return None

    except KeyError:
        print("Price data not found.")
        return None


# Set a price alert
def set_alert():

    coin = input("Enter coin ID: ").lower()

    try:
        target = float(input("Enter target price in PKR: "))

    except ValueError:
        print("Please enter a valid number.")
        return

    condition = input("Alert when price is 'above' or 'below': ").lower()

    if condition not in ["above", "below"]:
        print("Invalid condition.")
        return

    monitor(coin, target, condition)


# Monitor crypto price
def monitor(coin, target, condition):

    print("\nMonitoring started...")
    print("Checking price every 60 seconds.")
    print("Press Ctrl+C to stop.\n")

    try:

        while True:

            price = get_price(coin)

            if price is not None:

                print(
                    f"Current {coin} price: "
                    f"{price:,.2f} PKR"
                )

                # Price goes above target
                if condition == "above" and price >= target:

                    print("\n🚨 PRICE ALERT!")
                    print(
                        f"{coin} reached "
                        f"{price:,.2f} PKR"
                    )

                    break

                # Price goes below target
                if condition == "below" and price <= target:

                    print("\n🚨 PRICE ALERT!")
                    print(
                        f"{coin} reached "
                        f"{price:,.2f} PKR"
                    )

                    break

            # Wait 60 seconds
            time.sleep(5)

    except KeyboardInterrupt:

        print("\nMonitoring stopped.")


# Main program
def main():

    try:

        while True:

            print("\n===== Crypto Price Alert =====")
            print("1. Get price")
            print("2. Set price alert")
            print("3. Exit")

            choice = input("Choose: ")

            # Get current price
            if choice == "1":

                coin = input("Enter coin ID: ").lower()

                price = get_price(coin)

                if price is not None:

                    print(
                        f"{coin} price: "
                        f"{price:,.2f} PKR"
                    )

            # Set alert
            elif choice == "2":

                set_alert()

            # Exit
            elif choice == "3":

                print("Goodbye!")
                break

            else:

                print("Invalid choice.")

    except KeyboardInterrupt:

        print("\nProgram stopped.")


main()