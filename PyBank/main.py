import os
import csv
bank_csv = os.path.join("Resources","budget_data.csv")

# THIS SCRIPT IS FOR THE "PyBank PROBLEM" in Module #3 Homework

# READ THE DATASET 
with open (bank_csv, encoding='utf-8') as csv_file:
    csv_read = csv.reader(csv_file, delimiter=",")
    
    # SKIP the HEADER ROW
    next(csv_read, None)
    
    # INITIALIZE VARIABLES
    total_months = 0
    total_profit_losses = 0
    previous_profit_loss = 0
    profit_losses_changes = []
    dates = []
    
    # Read through (Loop) the rows in the dataset
    for row in csv_read:
        # Calculate TOTAL MONTHS and TOTAL PROFIS/LOSSES
        total_months += 1
        total_profit_losses += int(row[1])
        
        # Calculate PROFIT/LOSSES changes
        profit_loss_change = int(row[1]) - previous_profit_loss
        profit_losses_changes.append(profit_loss_change)
        dates.append(row[0])
        
        previous_profit_loss = int(row[1])

# Calculate AVERAGE CHANGE
average_change = sum(profit_losses_changes[1:]) / (total_months - 1)

# Find the GREATEST INCREASE and DECREASE in PROFITS
greatest_increase = max(profit_losses_changes)
greatest_decrease = min(profit_losses_changes)

# Get the corresponding dates for the GREATEST INCREASE and DECREASE
increase_date = dates[profit_losses_changes.index(greatest_increase)]
decrease_date = dates[profit_losses_changes.index(greatest_decrease)]

# Print the ANALYSIS RESULTS to the TERMINAL
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

# Export the RESULTS to a TEXT FILE (.txt)
with open('analysis/financial_analysis.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_losses}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: (${greatest_increase})\n {increase_date}")
    output_file.write(f"Greatest Decrease in Profits: (${greatest_decrease})\n {decrease_date}")