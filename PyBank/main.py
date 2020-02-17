import os
import csv
      
# set source path
srcpath = os.path.join("data","budget_data.csv")

# initialize list arrays and variables needed 
csvdata = []
periods = []
pnl = []
avg_change = []
total_months = 0
profit_loss = 0
average_change  = 0.00
greatest_increase = 0
greatest_decrease = 0
delta = 0

# load list arrays for periods and pnl data
with open(srcpath, newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    #print(row['Date'], row['Profit/Losses'])
    periods.append(row['Date'])
    pnl.append(int(row['Profit/Losses']))
    profit_loss += int(row['Profit/Losses'])

# determine the deltas for pnl changes over the course of the 86 month period
for i in range(len(pnl)):  
  if i < (len(pnl) - 1):
    avg_change.append((pnl[i+1] - pnl[i]))
    delta += (pnl[i+1] - pnl[i])

# calculate totals and averages for Financial Analysis
total_months = len(periods)
average_change = round((delta / (len(pnl)-1)),2)
greatest_increase = max(avg_change)
greatest_decrease = min(avg_change)



# print summary with the results
print("Financial Analysis")
print("-" * 30)
print(f"Total Months: {total_months}")
print(f"Total: ${profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: (${greatest_increase})")
print(f"Greatest Decrease in Profits: (${greatest_decrease})")

