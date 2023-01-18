
# Coding
# import all files
import os
import csv

# You can also do import statistics to avoid doing all the statistical calsulations. Sweet stuff.
import statistics
#print(os.getcwd())
#print(__file__)
os.chdir(os.path.dirname(os.path.realpath(__file__)))
#print(os.getcwd())
# Open Resources folder and then in that folder open the budget_data file and name it budget_data_csv.
election_data_csv = os.path.join( "Resources", "election_data.csv")
output_path = os.path.join("analysis", "file.txt")

with open(election_data_csv) as csv_file:
    csvreader = csv.reader(csv_file)
    csvheader = next(csv_file)
    print(f"Header:{csvheader}")
    output = open(output_path, "w")
#variable names
    votecasted=0
    totalvotecasted=0
    candidates=[]
    numbers_votes_won = {}
    percentage_won=0
    name_of_winner=""
    votes_for_winner=0
  
#The total number of votes cast
    for row in csvreader:
        votecasted +=1
        if row[2] not in candidates:
            candidates.append(row[2])
            numbers_votes_won[row[2]]=0
        numbers_votes_won[row[2]]+=1
        
#Print
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {votecasted}")
print(f"-------------------------")
output.write(f"Election Results\n")
output.write(f"---------------------\n")
output.write(f"Total Votes: {votecasted}\n")
output.write(f"--------------------\n")

#The percentage of votes each candidate won
for names in numbers_votes_won:
    votes = numbers_votes_won[names]
    percentage = votes / votecasted
    inhouse = percentage * 100
    print(f"{names}: {inhouse:.3f}% ({votes})")
    output.write(f"{names}: {inhouse:.3f}% ({votes})\n")

#The winner of the election based on popular vote.
    if votes > votes_for_winner: 
        winnervotes = votes
        winner = names
#Print 
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")
output.write(f"-------------------------\n")
output.write(f"Winner: {winner}\n")
output.write(f"-------------------------\n")