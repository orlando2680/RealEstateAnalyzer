# get validated float input
import math
def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be positive and non-zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Calculations
def getGallonsOfPaint(square_feet, feet_per_gallon):
    return math.ceil(square_feet / feet_per_gallon)

def getLaborHours(gallons, labor_hours_per_gallon):
    return gallons * labor_hours_per_gallon

def getLaborCost(labor_hours, charge_per_hour):
    return labor_hours * charge_per_hour

def getPaintCost(gallons, paint_price):
    return gallons * paint_price

def getSalesTax(state):
    state_tax_rates = {
        "CT": 0.06,
        "MA": 0.0625,
        "ME": 0.085,
        "NH": 0.0,
        "RI": 0.07,
        "VT": 0.06
    }
    return state_tax_rates.get(state.upper(), 0.0)

#cost estimate
def showCostEstimate(customer_name, gallons, labor_hours, labor_cost, paint_cost, total_cost, file_name):
    output = (
        f"Customer Name: {customer_name}\n"
        f"Gallons of Paint: {gallons}\n"
        f"Labor Hours: {labor_hours:.2f}\n"
        f"Labor Cost: ${labor_cost:.2f}\n"
        f"Paint Cost: ${paint_cost:.2f}\n"
        f"Total Cost (incl. tax): ${total_cost:.2f}\n"
    )
    print(output)
    with open(file_name, "w") as file:
        file.write(output)
    print(f"File created: {file_name}")

# Main function
def main():
    square_feet = getFloatInput("Enter Square Feet of the Wall: ")
    paint_price = getFloatInput("Enter Paint Price per Gallon: ")
    feet_per_gallon = getFloatInput("Enter Feet Covered per Gallon of Paint: ")
    labor_hours_per_gallon = getFloatInput("Enter Labor Hours per Gallon of Paint: ")
    labor_charge_per_hour = getFloatInput("Enter Labor Charge per Hour: ")
    state = input("Enter the state (e.g., CT, MA, etc.): ")
    customer_name = input("Enter Customer's Last Name: ")
#Calculations
    gallons = getGallonsOfPaint(square_feet, feet_per_gallon)
    labor_hours = getLaborHours(gallons, labor_hours_per_gallon)
    labor_cost = getLaborCost(labor_hours, labor_charge_per_hour)
    paint_cost = getPaintCost(gallons, paint_price)
    sales_tax_rate = getSalesTax(state)
    subtotal = labor_cost + paint_cost
    total_cost = subtotal * (1 + sales_tax_rate)
#estimate
    file_name = f"{customer_name}_PaintJobOutput.txt"
    showCostEstimate(customer_name, gallons, labor_hours, labor_cost, paint_cost, total_cost, file_name)

#Point of program
if __name__ == "__main__":
    main()
