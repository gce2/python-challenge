import os
import csv

#Pull in CSV file and create an empty list to stor values
pypoll = []
with open(r'C:\Users\gericks\Desktop\USCHomeworkSubmissions\PythonChallenges\PyPoll\03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv') as mycsvfile:
        #Create a csvreader object
        csv_reader = csv.reader(mycsvfile, delimiter=",")
        #Loop thru each row in the file and append each row in the pybank list
        for row in csv_reader:
            pypoll.append(row)

#Calculate the total number of votes cast
votes = 0
for i in pypoll:
    votes = votes + 1

 #Create a list of candidates that received votes and dedup them
candidates = []
for i in pypoll:
    candidates.append(i[2])
    
candidates_dedup = []
for i in candidates:
    if i not in candidates_dedup:
        candidates_dedup.append(i)

print('Election Results')
print('-------------------------------')
print('Total Votes: ', votes)
print('-------------------------------')           
