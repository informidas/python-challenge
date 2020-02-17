import os
import csv

# define path to data source file
csvpath = os.path.join('data', 'election_data.csv')

# declare some variables
khan_total = 0
correy_total = 0
li_total = 0
otooley_total = 0
total_votes = 0

# define array structures needed
voting = []
election = [{
  "candidate":"Li",
  "Votes": 0
},
{
  "candidate":"Khan",
  "Votes": 0
},
{
  "candidate":"Correy",
  "Votes": 0
},
{
  "candidate":"O'Tooley",
  "Votes": 0
}

]

#print(f"{election}")

with open(csvpath, newline='') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  csv_header = next(csvreader)
  print(f"CSV Header: {csv_header}")

  # Read each row of data after the header
  for row in csvreader:
      voting.append(row)

# get the total number of votes
total_votes = len(voting)

for i in range(len(voting)):
  if voting[i][2] == "Khan":
    khan_total += 1

  elif voting[i][2] == "Correy":
    correy_total += 1
    
  elif voting[i][2] == "Li":
    li_total += 1

  elif voting[i][2] == "O'Tooley":
    otooley_total += 1


#print(voting[0][2])
#print(voting[5][2])
#print(voting[1][2]) 
#print(voting[46][2]) 


print("Election Results")
print("--" * 20)
print(f"Total Votes: {total_votes}")
print("--" * 20)
print(f"Khan total is: {khan_total}")
print(f"O'Tooley total is: {otooley_total}")
print(f"Li total is: {li_total}")
print(f"Correy total is: {correy_total}")