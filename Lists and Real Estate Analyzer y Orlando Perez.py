# Real Estate Sales Analyzer

def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be greater than zero. Please try again.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid decimal number.")

def getMedian(values):
    n = len(values)

    # Sort the list
    values.sort()
    mid = n // 2
    if n % 2 == 1:
        return values[mid]  # Odd length
    else:
        return (values[mid - 1] + values[mid]) / 2  # Even length

# Main function to analyze real estate sales.
def main():
    print("\nWelcome to the Real Estate Sales Analyzer by Orlando Perez.\n")
    sales_list = []  # List to store sales values

    # Get sales price input and append it to the list
    while True:

        sale_price = getFloatInput("Enter the property sales value: ")
        sales_list.append(sale_price)

        # Ask user whether to input another value
        while True:
            choice = input("\nDo you want to enter another value? (Y/N): ").strip().lower()
            if choice in ('y', 'n'):
                break
            else:
                print("Error: Enter 'Y' for Yes or 'N' for No.")
        if choice == 'n':
            break

    # Sort the list in ascending order
    sales_list.sort()

    # Display results
    print("\nSales Summary:")
    for i, value in enumerate(sales_list, start=1):
        print(f"Sale {i}: ${value:.2f}")

    # Calculate and display statistics
    min_value = min(sales_list)
    max_value = max(sales_list)
    total = sum(sales_list)
    average = total / len(sales_list)
    median = getMedian(sales_list)
    commission = total * 0.03

    print(f"\nMinimum Sale: ${min_value:.2f}")
    print(f"Maximum Sale: ${max_value:.2f}")
    print(f"Total Sales: ${total:.2f}")
    print(f"Average Sale: ${average:.2f}")
    print(f"Median Sale: ${median:.2f}")
    print(f"Commission (3%): ${commission:.2f}")

if __name__ == "__main__":
    main()
