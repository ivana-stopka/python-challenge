# PyBank

# Run a financial analysis on PyBank.csv to provide the following info
	# The total number of months included in the dataset
	# The net total amount of "Profit/Losses" over the entire period
	# The average of the changes in "Profit/Losses" over the entire period
	# The greatest increase in profits (date and amount) over the entire period
	# The greatest decrease in losses (date and amount) over the entire period

# Import the modules
import os
import csv
import shutil

# Print heading
print("----------------------------")
print("Financial Analysis")
print("----------------------------")

# Define list variables
profit_loss = []
date = []

# Set path for the csv file
PyBank_csv = os.path.join("Resources","budget_data.csv")

# Open the csv
with open(PyBank_csv) as csv_file:
	csv_reader=csv.reader(csv_file,delimiter=",")

	# Loop through the first column(0) and move values to the list 'date' then remove column header.
	for col in csv_reader:
		date.append(col[0])
date.remove("Date")

# Open the csv again
with open(PyBank_csv) as csv_file:
	csv_reader=csv.reader(csv_file,delimiter=",")

	# Loop through the second column(1) and move values to the list 'profit_loss' then remove column header.
	for col in csv_reader:
		profit_loss.append(col[1])
profit_loss.remove("Profit/Losses")

# Convert list of strings to list of integers
profit_loss_ints = [int(item) for item in profit_loss]

# Count the elements in the profit_loss list to get the number of months
element_count = len(profit_loss_ints)
print("Total Months: ",element_count)

# Sum the elements in the profit_loss list and print Total Profit/Loss
Sum = sum(profit_loss_ints)
formatted_Sum = "${:,.0f}".format(Sum)
print("Total: ",formatted_Sum)

# Create new list that calculates a moving difference over the profit/loss using a for loop
diff_profit_loss = []

i=0
for i in range(len(profit_loss_ints)-1):
    diff_profit_loss.append(profit_loss_ints[i+1]-profit_loss_ints[i])
    i=i+1
     
# Calculate and print the average Profit/Loss
element_count_2 = len(diff_profit_loss)
Sum_2 = sum(diff_profit_loss)
ave_profit_loss = Sum_2/element_count_2
formatted_ave_profit_loss = "${:,.2f}".format(ave_profit_loss)
print("Average: ",formatted_ave_profit_loss)

# Determine and print the greatest increase in profits (date and amount)
Max = max(diff_profit_loss)
formatted_Max = "${:,.0f}".format(Max)
Max_Index = diff_profit_loss.index(Max)
print("Greatest increase in profits: ",date[Max_Index+1],formatted_Max)

# Determine and print the greatest decrease in profits (date and amount)    
Min = min(diff_profit_loss)
formatted_Min = "${:,.0f}".format(Min)
Min_Index = diff_profit_loss.index(Min)
print("Greatest decrease in profits: ",date[Min_Index+1],formatted_Min)
print("----------------------------")

# Write to a text file the results
lines = ["Financial Analysis",
         "Total Months: " + str(element_count),
         "Total: " + str(formatted_Sum),
         "Average: " + str(formatted_ave_profit_loss),
         "Greatest increase in profits: " + str(date[Max_Index+1]) + " " +str(formatted_Max),
         "Greatest decrease in profits: " + str(date[Min_Index+1]) + " " + str(formatted_Min)] 
with open('results.txt','w') as f:
    f.write('\n'.join(lines))

# Move new result.txt file to Analysis folder.
source = "results.txt"
destination = "Analysis"
new_path=shutil.move(source,destination)


