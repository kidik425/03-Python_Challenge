#declare and initiate variables
import csv

#declare totals variables
tot = 0
totVotes = 0
totMnthAvgDenom = 0

#declare profit and loss variables and get avg change
curPL = 0 
prevPL = 0

#declare to hold max and min change values
maxInc = 0
maxDec = 0

candDict = dict()

csvPath =  'PyRoll/Resources/election_data.csv'
fileOutput = 'PyRoll/Analysis/election_date_output.txt'

with open(csvPath,'r') as csvFile:

    csvReader = csv.reader(csvFile, delimiter = ',')
    next(csvReader)

    #Read in file and loop through
    for row in csvReader:        
       totVotes += 1

       if row[2] in candDict:
            #print("Candidate is there")
            candDict[row[2]] += 1
       else: 
            #print("Candidate is not there")
            candDict[row[2]] = 1

    winner = max(candDict, key=candDict.get)

#capture all output into a variable that will be used later for both output to screen and file
#output variable will be appended to itself a few times to allow looping to work

output = (    
    f"\nElection Results\n"
    f"-----------------------\n"
    f"Total Votes: {totVotes:,}\n"
    f"-----------------------\n\n"
)
for cand in candDict:
    output += f"{cand}: {(candDict.get(cand)/totVotes)*100: .3f}% ({candDict.get(cand):,}) \n"

output += ( 
    f"\n-----------------------\n"
    f"Winner: {winner}\n"
    f"-----------------------"
    )


#print to screen and file
print(output)
with open(fileOutput, "w", newline="") as textFile:
    textFile.write(output)
