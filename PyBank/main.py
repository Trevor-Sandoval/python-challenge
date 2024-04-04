import os
import csv
bank_csv = os.path.join("Resources","budget_data.csv")

# This script is for the "PyBank Problem" based on the Python lectures

# Read the dataset
with open (bank_csv, encoding='utf-8') as csv_file:
    csv_read = csv.reader(csv_file, delimiter=",")
    
    # Skip the header row
    next(csv_read, None)
    
    # Initialize variables
    total_months = 0
    total_profit_losses = 0
    previous_profit_loss = 0
    profit_losses_changes = []
    dates = []
    
    # Read through (Loop) the rows in the dataset
    for row in csv_read:
        # Calculate total months and total profit/losses
        total_months += 1
        total_profit_losses += int(row[1])
        
        # Calculate profit/losses changes
        profit_loss_change = int(row[1]) - previous_profit_loss
        profit_losses_changes.append(profit_loss_change)
        dates.append(row[0])
        
        previous_profit_loss = int(row[1])

# Calculate average change
average_change = sum(profit_losses_changes[1:]) / (total_months - 1)

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_losses_changes)
greatest_decrease = min(profit_losses_changes)

# Get the corresponding dates for the greatest increase and decrease
increase_date = dates[profit_losses_changes.index(greatest_increase)]
decrease_date = dates[profit_losses_changes.index(greatest_decrease)]

# Print the analysis results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

# Export the results to a text file
with open('financial_analysis.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_losses}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")