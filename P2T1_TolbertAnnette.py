# Projecting sales profit from total sales
# 20 Feb 2020
# CTI-110 P2T1 - Sales Prediction
# Annette Tolbert
#

#declare variables for input

totalSales = 0.0
COMPANY_PROFIT_PERCENTAGE = 0.23
annualProfit = 0.0

#Get input

totalSales = float(input("Enter the projected annual total sales: "))

#Calculations

annualProfit = totalSales * COMPANY_PROFIT_PERCENTAGE

#Display
print("The projected annual profit is $",format(annualProfit,',.2f'))
