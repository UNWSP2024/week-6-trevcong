#AUTHOR: Trevor Conger UNWSP
#DATE: 10/11/24
#TITLE: Calculate tax!

#PSEUDO CODE
#------------------------------------------------------------------------------------------------------------------------------------------
#    First get user input( from a function call ), keep trying to get a numeric value, if not, tell them they need to give a numeric value
#       Pass into a function the totalSales, this will be used to calculate the taxes
#
#                 stateTax = totalSales * stateTaxRate
#                 countyTax = totalSales * countyTaxRate
#                 totalTax = stateTax + countyTax
#
#       Next return the three values back to main, as we will be returning all at once with multiple assignments
#       
#       While in main take these 3 values and present them to the user with a print statement, we also want to round to the hundreds
#
#------------------------------------------------------------------------------------------------------------------------------------------

#Function to calculate the sales tax
#PARAM totalSales as a float
#RETURN countyTax 2.5%
#RETURN stateTax 5%
#RETURN totalTax countryTax + stateTax
def calculateTaxes(totalSales):
    stateTaxRate = 0.05 
    countyTaxRate = 0.025 

    stateTax = totalSales * stateTaxRate
    countyTax = totalSales * countyTaxRate
    totalTax = stateTax + countyTax

    return countyTax, stateTax, totalTax

#Get user input about the sales for the month
#Keep trying till they give a numeric value
#RETURN sales to be used in calculateTax function 
def getSalesInput():
    while True:
        try:
            sales = float(input("Enter the total sales for the month in USD$: "))
            if sales < 0:
                print("Sales amount cannot be negative. Please enter a positive number.")
            else:
                return sales
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    totalSales = getSalesInput()
    countyTax, stateTax, totalTax = calculateTaxes(totalSales)

    print(f"\nMonthly Sales Tax Report")
    print(f"Total Sales: ${totalSales:.2f}")
    print(f"County Sales Tax (2.5%): ${countyTax:.2f}")
    print(f"State Sales Tax (5%): ${stateTax:.2f}")
    print(f"Total Sales Tax: ${totalTax:.2f}")

if __name__ == "__main__":
    main()