# Python Homework - PyBank

import os
import csv

#create an empty list to store values
pybank = []
with open(r'C:\Users\gericks\Desktop\USCHomeworkSubmissions\PythonChallenges\PyBank\03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv') as mycsvfile:
        #Create a csvreader object
        csv_reader = csv.reader(mycsvfile, delimiter=",")
        #Loop thru each row in the file and append each row in the pybank list
        for row in csv_reader:
            pybank.append(row)
            
#Calculate all the month-rows in the data set and make it an integer
totalmonths=len(pybank)-1         

#Calculate the total amount of "Profit/Loss" over entire period - loop thru whole list
totalprofitloss= 0
for i in range (0, len(pybank)-1):
    totalprofitloss= totalprofitloss + int(pybank[i+1][1])

#Calculate the total of the changes in Profit/Loss over the entire period 
totalchange = 0
for i in range (0, len(pybank)-2):
    totalchange = totalchange + int(pybank[i+2][1]) - int(pybank[i+1][1])  

#Calculate the average of the profit/loss over the entire period
avgchange = totalchange/(len(pybank)-2)

#Calculate the greatest increase in profits (date and amount) over the entire period - if i+2 > than i+1, then i+2 else i+1
maxprofit = 0
maxmonth = ""
for i in range (0, len(pybank)-2):
    if int(pybank[i+2][1]) - int(pybank[i+1][1])> maxprofit:
        maxprofit = int(pybank[i+2][1]) - int(pybank[i+1][1])
        maxmonth = pybank[i+2][0] 

#Calculate the greatest decrease in losses (date and amount) over the entire period 
minprofit = 0
minmonth =""
for i in range (0, len(pybank)-2):
    if int(pybank[i+2][1]) - int(pybank[i+1][1])< minprofit:
        minprofit = int(pybank[i+2][1]) - int(pybank[i+1][1])
        minmonth = pybank[i+2][0]

print('Financial Analysis')
print('-------------------------------------')
print("Total Months: ", totalmonths)
print("Total: $ ", totalprofitloss)
print("Average Change: $ ", avgchange)
print("Greatest Increase in Profits:", maxmonth, maxprofit)
print("Greatest Decrease in Profits: ", minmonth, minprofit)   

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)




