#Analyze financial data

#Import Packages
import os # This will allow us to create file paths across operating systems
import csv # Module for reading CSV files

#Read each line of csv into array

#CSV Path
readFilePath = f'{os.path.dirname(os.path.abspath(__file__))}\Resources\\budget_data.csv'
numarray = []
with open(readFilePath) as csvfile: #, mode='rU'

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader) #skip the header

    # Initilize variables
    prevRowValue = 0
    monthCount = 0
    totalAmount = 0
    differenceTotal = 0
    greatestDecreaseValue = 0
    greatestIncreaseValue = 0
    flagFirstRow = 1

    #Read each row of data
    for row in csvreader:
        #Data is stored by month, so a simpler iterator will work to get count of months
        monthCount += 1

        #Add row value to current total
        totalAmount += int(row[1]) 

        #For remaining calculations, need to skip first row. Don't calculate if flag is 1
        if flagFirstRow == 0:
            #Difference is current row minus previous row. Positive for increase, negative for decrease
            difference = (int(row[1]) - prevRowValue) 

            #Add difference to total. Used at the end to calculate average difference
            differenceTotal += difference

            #If difference is less than previous greatest decrease, update greatest decrease information
       
            if difference < greatestDecreaseValue: 
                greatestDecreaseDate = row[0]
                greatestDecreaseValue = difference
            
            #If difference is more than previous greatest increase, update greatest increase information
            if difference > greatestIncreaseValue: 
                greatestIncreaseDate = row[0]
                greatestIncreaseValue = difference

        #Store the current row value for next loop iteration
        prevRowValue = int(row[1]) 

        #Remove first row flag
        flagFirstRow = 0

#Calculate Average Change, but adjust for first row
averageChange = differenceTotal/ (monthCount - 1)

print("Financial Analysis")
print("-------------------")
print(f'Total Months: {monthCount}')
print(f'Total: ${totalAmount}')
print(f'Average Change: ${averageChange :.2f}')
print(f'Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncreaseValue})')
print(f'Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecreaseValue})')
