#PyBank
#dependencies
import csv
import os

#specify path to file
csvpath = os.path.join("Resources", "budget_data.csv")
 
#set lists for months and profit/loss amounts
months = []
amounts = []

with open(csvpath) as budget_data:
    csvreader= csv.reader(budget_data)

    #header row
    header = next(csvreader)

    #rows of data after header, add to month and amounts list
    for row in csvreader:
        
        #add months to list
        month = row[0]
        months.append(month)
        
        #add total profit/loss
        profit = row[1]
        amounts.append(int(profit))

    #calculating differences in profit amounts
    differences = []
    for i in range(0,len(amounts)-1):
        first_amount = amounts[i]
        second_amount = amounts[i+1]

        difference = second_amount - first_amount
        #add to differences list
        differences.append(difference)

    #find max of differences of greatest increase
    greatest_increase = max(differences)
    #identify the index of the max difference
    greatest_increase_index = differences.index(greatest_increase)
    #find the corresponding month index
    greatest_increase_index_month = greatest_increase_index + 1
    #use index to pull month
    greatest_increase_month = months[greatest_increase_index_month]

    #find max of differences for greatest decrease
    greatest_decrease = min(differences)
    greatest_decrease_index = differences.index(greatest_decrease)
    greatest_decrease_index_month = greatest_decrease_index + 1
    greatest_decrease_month = months[greatest_decrease_index_month]

#calculate average change and round
average_change = sum(differences) / len(differences)
average_change_rounded = round(average_change, 2)

#calculate total months and amounts
total_months = len(months)
net_total = sum(amounts)

#analysis text for output file
analysis = f"""
    Financial Analysis
    ----------------------------
    Total Months: {total_months}
    Total: ${net_total}
    Average Change: {average_change_rounded}
    Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
    Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})"""

#print analysis to terminal
print(analysis)
  
#export to text file
output_file = os.path.join("analysis", "analysis.txt")
with open(output_file, "w") as txt_file:
    txt_file.write(analysis)

