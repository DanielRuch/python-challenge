#Election Results

#Note: A simple set of if statements for each candidate executed a bit faster. However, this approach is much more robust and can handle a large number of different candidates

#Import Packages
import os # This will allow us to create file paths across operating systems
import csv # Module for reading CSV files

#CSV Path
readFilePath = f'{os.path.dirname(os.path.abspath(__file__))}\Resources\\election_data.csv'

with open(readFilePath) as csvfile: #, mode='rU'

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader) #skip the header

    #Initialize variables
    candidateList = []
    voteCount = 0
    
    #Read each row of data
    for row in csvreader:
        #Each row correlates to a vote, so increase voteCount for every row
        voteCount += 1
        
        #Store name of candidate for current vote
        name = row[2] 

        #Initialize found flag
        foundFlag = 0

        #Loop through list of candidate information
        for candRow in candidateList:
            #Check if the current row in candidate starts with the same name as current row
            if candRow[0] == name:
                candRow[1] += 1 #Tally vote for candidate
                foundFlag = 1 #Set flag to 1 to indicate candidate was found
                break
        #Check if candidate was found in array. If not, add them to array
        if foundFlag == 0:
            candidateList.append([name, 1])

        #Huge dataset takes a long time to process, so let the user know periodically that python is still working! (every 500,000 votes)
        if voteCount % 500000 == 0:
            print(f'Still working, {voteCount} votes tallied so far!')
        
winnerVotes = 0 #Initialize winnerVotes variable

print("") #empty line for readability

#Generate output
outputData = []

outputData.append(["Election Results"])
outputData.append(["----------------------"])
outputData.append([f'Total Votes: {voteCount}'])
outputData.append(["----------------------"])

for row in candidateList:
    candidateName = row[0] #Candidate Name
    candidateVotes = row[1] #Number of votes
    votePercent = (candidateVotes/voteCount) * 100 #Calculate percentage of total votes

    #If greater than previous candidate's votes, store name of new winning candidate
    if candidateVotes > winnerVotes:
        winnerVotes = candidateVotes
        winnerName = candidateName
    outputData.append([f'{row[0]}: {votePercent:.3f}% ({row[1]})'])

outputData.append(["----------------------"])
outputData.append([f'Winner: {winnerName}'])
outputData.append(["----------------------"])

#Output data to terminal and to text file
#Output path of text file
outputFilePath = f'{os.path.dirname(os.path.abspath(__file__))}\Resources\\electionResults.txt'

#Print results to terminal and output to file
with open(outputFilePath, 'w') as txt:
    for row in outputData:
        print(row[0])
        txt.write(f'{row[0]}{chr(10)}') #Add line feed
