#####################################################################################################
# The included python script provides a coding solution to analyze a Bank's Profit and Loss position 
# on a month over month basis.
# Name: K. Ramsay
# Created: 2/3/2020
# Updated: 5/4/2020
#####################################################################################################

# import modules
import os, csv

budget = []
deltas = []
total_months = 0
profit_loss = 0
average_change  = 0.00
greatest_increase = 0
greatest_decrease = 0


# set path for source file
srcpath = os.path.join("data", "budget_data.csv")

# open source files as readonly, and instantiate a reader object
with open(srcpath, 'r', newline='') as csvfile:
  csvreader = csv.reader(csvfile)

  # skip the header row
  next(csvreader)
  
  # loop through the remaining records and append to the budget list array we created
  for row in csvreader:
    budget.append(row)
    
# populate deltas list array 
for i in range(1, len(budget)):
  deltas.append((int(budget[i][1]) - int(budget[i-1][1])) )
  profit_loss += int(budget[i - 1][1])
  if i == (len(budget) - 1):
    profit_loss = profit_loss + int(budget[i][1])
 
# function to calculate the average profit/ loss change between periods
def calculate_average_delta():
  avg_delta = format(sum(deltas) / len(deltas), '.3f')
  return avg_delta

# function to return the month / period associated with a given variance
# function used to return both the greatest increase and decrease 
def find_month_variance(variance): 
  for m in range(0, len(deltas)): 
    if deltas[m] == int(variance): 
      return budget[m + 1][0]    
      break    

# assign variables 
total_months = len(budget)
average_change  = calculate_average_delta()
greatest_increase = max(deltas)
greatest_increase_month = find_month_variance(greatest_increase)
greatest_decrease = min(deltas)
greatest_decrease_month = find_month_variance(greatest_decrease)

# print summary with the results
print("Financial Analysis")
print("-" * 30)
print(f"Total Months: {total_months}")
print(f"Total: ${profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# open a new text file with "write" mode.
file = open("results\\report.txt", "w")

# write the results to the text file
file.write("Financial Analysis\n")
file.write("-" * 30)
file.write(f"\nTotal Months: {total_months}\n")
file.write(f"Total: ${profit_loss}\n")
file.write(f"Average Change: ${average_change}\n")
file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
# make sure the file is closed
file.close()
