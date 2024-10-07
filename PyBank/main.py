#Dependencies and Setup
from pathlib import Path
import os
import csv

#Files to load and output
file_to_load = os.path.join("Resources", "python-challenge\PyBank\Resources\budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "python-challenge\PyBank\analysis\budget_analysis.txt")  # Output file path

#Define Vars and track financial data
total_months = 0
total_net = 0 

# Track the total and net change
net_change_list = []
total_net = 0
greatest_increase = (' ', 0)  # (month, amt)
greatest_decrease = (' ', 0)  # (month, amt)

# Open and read the csv
with open('python-challenge\PyBank\Resources\budget_data.csv') as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)  # Get the first data row
    last_profit = int(first_row[1])  #Starting the Profit/Losses Column
    total_months += 1
    total_net += int(first_row[1])

    # Process each row of data
    for row in reader:

        #Track number of months
        total_months+= 1
        
        # Track the total
        total_net += int(row[1])

        # Track the net change
        current_profit = int(row[1])
        net_change = current_profit - last_profit
        net_change_list.append(net_change)

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase = (row[0], net_change)

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease = (row[0], net_change)

        last_profit = current_profit

# Calculate the average net change across the months
if len(net_change_list) != 0:  # Check if the list is not empty
    average_change = sum(net_change_list) / len(net_change_list)
else:
    average_change = 0  # Avoid division by zero


#Generate Output Summary
output_summary = (
    "Election Results\n"
    "----------------------------\n"
    f'Total Months: {total_months}\n'
    "----------------------------\n"
    
    f'Total Months: {total_months}\n'
    f'Total: ${total_net}\n'
    f'Average Change: ${average_change:.2f}\n'
    f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n'
    f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n'
)

# Write the results to a text file
with open('python-challenge\PyBank\analysis\budget_analysis.txt', "w") as txt_file:
    txt_file.write(output_summary)
