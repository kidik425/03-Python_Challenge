#declare and initiate variables
import csv

#declare totals variables
tot = 0
totMnth = 0
totMnthAvgDenom = 0

#declare profit and loss variables and get avg change
curPL = 0 
prevPL = 0
curChange = 0 #used for the currect total change
prevChange = 0 #used to hold the previous total change
totChange = 0 #used to get the sum of the total change
avgChange = 0 #user to get the ave of the total change

#declare to hold max and min change values
maxInc = 0
maxDec = 0

#declare file paths
csvPath =  'PyBank/Resources/budget_data.csv'
fileOutput = 'PyBank/Analysis/budget_data.txt'
with open(csvPath,'r') as csvFile:

    csvReader = csv.reader(csvFile, delimiter = ',')
    next(csvReader)

    #Read in file and loop through
    for row in csvReader:        
        #increm the total month counter
        totMnth += 1

        #convert second element of row list to Int
        try:
            curPL = int(row[1])
            tot += curPL
        except ValueError:
            print(row[1]+" will not convert to int")

        #Get profit/loss change for the current period
        if totMnth != 1:
            mnth = row[0]
            curChange = (curPL - prevPL)
            totChange += curChange
            totMnthAvgDenom += 1

            #look for max and min changes
            if curChange > maxInc:
                maxInc = curChange
                maxIMnth = mnth
            if curChange < maxDec:
                maxDec = curChange
                maxDMnth = mnth

            #set prevChange to curChange for next evalution in loop
            prevChange = curChange

        #set previous profit loss to the current so that it can be evaluated next time
        prevPL = curPL


    avgChange = (totChange)/(totMnthAvgDenom)

#capture all output into a variable that will be used later for both output to screen and file

output = (   
    f"Financial Analysis\n"
    f"-----------------------\n"
    f"Total Months: {totMnth}\n"
    f"Total: ${tot:,}\n"
    f"Average Change: ${avgChange:,.2f}\n"
    f"Greatest Increase in Profits: {maxIMnth} (${maxInc:,})\n"
    f"Greatest Decrease in Profits: {maxDMnth} (${maxDec:,})\n"
)

#print to screen and file
print(output)
with open(fileOutput, "w", newline="") as textFile:
    textFile.write(output)
