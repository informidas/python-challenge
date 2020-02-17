import os
import csv

# define path to data source file
csvpath = os.path.join('data', 'election_data.csv')

# declare some variables
khan_total = 0
khan_percentage = 0.000
correy_total = 0
correy_percentage = 0.000
li_total = 0
li_percentage = 0.000
otooley_total = 0
otooley_percentage = 0.000
total_votes = 0

# define array structures needed
voting = []


#print(f"{election}")

with open(csvpath, newline='') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  csv_header = next(csvreader)

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



# write the results to a dictionary array
candidate_totals = [correy_total, otooley_total, khan_total, li_total]

#sort the list
sorted_list = sorted(candidate_totals, reverse=True)

# get the percentages for each candidate
correy_percentage = format(((correy_total/total_votes) * 100), '.3f')
khan_percentage = format(((khan_total/total_votes) * 100), '.3f')
otooley_percentage = format(((otooley_total/total_votes) * 100), '.3f')
li_percentage = format(((li_total/total_votes) * 100.000), '.3f')


print(sorted_list)

print("Election Results")
print("--" * 20)
print(f"Total Votes: {total_votes}")
print("--" * 20)

for s in sorted_list:
  if s == correy_total:
    print(f"Correy:  {correy_percentage}% ({correy_total})")
  
  elif s == otooley_total:
    print(f"O'Tooley: {otooley_percentage}% ({otooley_total})")

  elif s == khan_total:
    print(f"Khan: {khan_percentage}% ({khan_total})")

  elif s == li_total:
    print(f"Li: {li_percentage}% ({li_total})")




