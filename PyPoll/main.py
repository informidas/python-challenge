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
winner = "Not Declared"

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


# open a new text file with "write" mode to write Election Results.
file = open("results\\election_results.txt", "w")

print()
print("Election Results")
file.write(f"Election Results\n")
print("--" * 30)
file.write("-" * 30)
print(f"Total Votes: {total_votes}")
file.write(f"\nTotal Votes: {total_votes}\n")
print("--" * 30)
print()
file.write("-" * 30 )

for s in sorted_list:
  if s == correy_total:
    print(f"Correy:  {correy_percentage}% ({correy_total})")
    print()
    file.write(f"\nCorrey:  {correy_percentage}% ({correy_total})\n")

  elif s == otooley_total:
    print(f"O'Tooley: {otooley_percentage}% ({otooley_total})")
    print()
    file.write(f"\nO'Tooley: {otooley_percentage}% ({otooley_total})\n")

  elif s == khan_total:
    print(f"Khan: {khan_percentage}% ({khan_total})")
    print()
    file.write(f"\nKhan: {khan_percentage}% ({khan_total})\n")

  elif s == li_total:
    print(f"Li: {li_percentage}% ({li_total})")
    print()
    file.write(f"\nLi: {li_percentage}% ({li_total})\n")

file.write("-" * 30 )

# get the value for the winner identified!
if correy_total == sorted_list[0]:
  winner = "Correy"
elif otooley_total == sorted_list[0]:
  winner = "O'Tooley"
elif khan_total == sorted_list[0]:
  winner = "Khan"
elif li_total == sorted_list[0]:
  winner = "Li"

print("-" * 30 )
print(f"Winner: {winner}\n")
file.write(f"\nWinner: {winner}\n")
print("-" * 30 )
file.write("-" * 30 )

# make sure to close the file we are writing the Election Results to
file.close()
