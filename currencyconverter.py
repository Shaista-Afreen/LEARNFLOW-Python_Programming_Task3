#Install necessary library
#pip install CurrencyConverter

from currency_converter import CurrencyConverter

def main():
    print("This is a Currency Converter Project")
    
    # Initialize CurrencyConverter
    c = CurrencyConverter()

    # Get list of supported currencies
    supported_currencies = c.currencies

    # Displaying supported currencies to user
    print("Currencies that can be used are:", supported_currencies)

    while True:
        try:
            value = float(input("Enter the value you wish to convert: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        while True:
            input_currency = input("Please input the source currency: ").upper()
            if input_currency in supported_currencies:
                break
            else:
                print("Invalid currency code. Please enter a valid currency code.")

        while True:
            desired_currency = input("Please input the desired currency: ").upper()
            if desired_currency in supported_currencies:
                break
            else:
                print("Invalid currency code. Please enter a valid currency code.")

        # Currency conversion
        converted_value = c.convert(value, input_currency, desired_currency)

        print(f"The {value} {input_currency} in {desired_currency} is : {converted_value}")

        choice = input("Do you wish to do another conversion? (yes/no): ").lower()
        if choice != 'yes':
            break

    print("Thank you for using the Currency Converter.")


main()
