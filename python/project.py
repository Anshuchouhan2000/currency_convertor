exchangerates = {
    'USD': 1.0,
     'EUR': 0.85, 'GBP': 0.72, 'INR': 74.5, 'JPY': 110.0,
    'AUD': 1.35, 'CAD': 1.25, 'SGD': 1.34, 'CHF': 0.92, 'CNY': 6.45,
    'MYR': 4.17, 'NZD': 1.42, 'KRW': 1180.0, 'RUB': 75.0, 'ZAR': 15.0,
    'BRL': 5.25, 'MXN': 20.0, 'HKD': 7.78, 'SEK': 8.65, 'NOK': 8.85,
    'DKK': 6.35, 'THB': 33.0, 'IDR': 14500.0, 'PHP': 50.0, 'TRY': 8.5,
    'SAR': 3.75, 'AED': 3.67, 'PLN': 3.95, 'CZK': 22.0, 'HUF': 300.0,
    'ILS': 3.25, 'ARS': 95.0, 'CLP': 800.0, 'COP': 3800.0, 'EGP': 15.7,
    'NGN': 410.0, 'PKR': 170.0, 'VND': 23000.0, 'BDT': 85.0, 'KWD': 0.30,
    'QAR': 3.64, 'OMR': 0.38, 'BHD': 0.38, 'JOD': 0.71, 'LKR': 200.0,
    'NPR': 120.0, 'MMK': 1800.0, 'KHR': 4100.0, 'LAK': 9500.0, 'MNT': 2850.0,
    'UZS': 10500.0, 'KZT': 430.0, 'TWD': 28.0, 'XCD': 2.7, 'BBD': 2.0,
    'BZD': 2.0, 'BSD': 1.0, 'PAB': 1.0, 'GYD': 210.0, 'HTG': 100.0,
    'JMD': 150.0, 'TTD': 6.75, 'XPF': 110.0, 'XAF': 550.0, 'XOF': 550.0,
    'DJF': 180.0, 'GNF': 10000.0, 'KGS': 85.0, 'MVR': 15.4, 'MUR': 40.0,
    'SCR': 15.0, 'SLL': 10000.0, 'SOS': 580.0, 'TJS': 11.0, 'TMT': 3.5,
    'UAH': 28.0, 'UGX': 3700.0, 'ZMW': 20.0, 'ZWL': 360.0
}

def print_currencies():
    print("Supported currencies:")
    for currency in exchangerates:
        print(f"- {currency}")

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchangerates or to_currency not in exchangerates:
        raise ValueError("Unsupported currency.")
    
    # Convert the amount to USD first
    amount_in_usd = amount / exchangerates[from_currency]
    
    # Convert the USD amount to the target currency
    converted_amount = amount_in_usd * exchangerates[to_currency]
    return converted_amount

def main():
    print("Welcome to the  Currency Converter!")
    print_currencies()

    while True:
        amount = input("\nEnter the amount (or 'q' to quit): ").strip()
        if amount.lower() == 'q':
            print("Thank you for using the Currency Converter. Goodbye!")
            break

        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue

        from_currency = input("Enter the source currency (e.g., USD): ").upper()
        to_currency = input("Enter the target currency (e.g., EUR): ").upper()

        if from_currency not in exchangerates or to_currency not in exchangerates:
            print("Unsupported currency. Please check your input.")
            continue

        converted_amount = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
