#Instructions:
    #In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses". (Thankfully, your company has rather lax standards for accounting, so the records are simple.)
    # Your task is to create a Python script that analyzes the records to calculate each of the following:
    # The total number of months included in the dataset.
    # The net total amount of "Profit/Losses" over the entire period.
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period. 
    # Your analysis should look similar to the following:

        #Financial Analysis
        #----------------------------
            # Total Months: 86
            # Total: $22564198
            # Average Change: $-8311.11
            # Greatest Increase in Profits: Aug-16 ($1862002)
            # Greatest Decrease in Profits: Feb-14 ($-1825558)

# Coding
# import all files
import os
import csv

# You can also do import statistics to avoid doing all the statistical calsulations. Sweet stuff.
import statistics

# Open Resources folder and then in that folder open the budget_data file and name it budget_data_csv.
budget_data_csv = os.path.join("C:\Users\aoyedira\Starter_Code\Instructions\PyBank\Resources\budget_data.csv")

# Open the file
with open (budget_data_csv, newline=" ") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Header Row
    csvheader = next(csvreader)
    print(f'Header:{csvheader}')

# Give variable names and values first
totalmonth = 0
totalnetrevenue = 0
averagechange = 0
date = []
profits = []
past_profits = 0
diff_monthly = []
total_diff = 0
profit_increase = {"month": "", "profit": 0}
profit_decrease = {"month": "", "losses": 0}

# For loops for mathematics and stuff.
  for row in csvreader:
        totalmonth +=1
        totalnetrevenue += int(row[1])
        # To keep track of net total in date and revenue or profit and losses over time.
        date.append(row[0])
        profit = int(row[1])
        profits.append(profit)

        # Now this will calculate the changes in revenue over the time period.
        ozzychanges = 0
        if past_profits != 0:
            ozzychanges = profits - past_profits
            diff_monthly.append(ozzychanges)
            past_profits = profit

            # Calculating the profit increase and decrease over the time period.
            if ozzychanges > profit_increase['profits']:
                profit_increase['profits'] = ozzychanges
                 profit_increase['month'] = row[0]
            if ozzychanges < profit_decrease['losses']:
                profit_decrease['losses'] = ozzychanges
                profit_decrease['month'] = row[0]

            # Now find the average.
            averagechange = sum(diff_monthly)/len(diff_monthly)

# Create Tempelate for the text file and results
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {totalmonth}")
print(f"Total: ${totalnetrevenue}")
print(f"Average Change: ${averagechange:.2f}")
print(f"Greatest Increase in Profits: {profit_increase['month']} ${profit_increase['profits']}")
print(f"Greatest Decrease in Profits: {profit_decrease['month']} ${profit_decrease['losses']}")

# Output instructions: Output as txt file into analysis folder use"w" function to write to folder
# \n is to indicate that the output is to be in a new line.
output = open("PyBank/Analysis/file.txt","w")
output.write(f"Financial Analysis\n")
output.write(f"----------------------------\n")
output.write(f"Total Months: {totalmonth}\n")
output.write(f"Total: ${totalnetrevenue}\n")
output.write(f"Average Change: ${averagechange:.2f}\n")
output.write(f"Greatest Increase in Profits: {profit_increase['month']} ${profit_increase['profits']}\n")
output.write(f"Greatest Decrease in Profits: {profit_decrease['month']} ${profit_decrease['losses']}\n")


            










