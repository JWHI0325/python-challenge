#PyBank Instructions
#the total number of months included in dataset 
import os
import csv

filepath = os.path.join("Resources", "budget_data.csv")

with open (filepath,"r") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")  
    header=next(csvreader)
    months=[]
    profitlosses=[]
    date=[]
    change_profit=[]
    total_revenue = 0
    total_change_profits = 0 
    initial_profit = 0
    total_profit = 0
    count = 0
    for row in csvreader:
        months.append(row[0]) 
        profitlosses.append(int(row[1]))
    totalmonth=len(months)
    total_profit = total_profit + int(row[1])
    print("total_profit:" + "$" + str(total_profit))
    print(totalmonth)

#net total amount of "Profit/losses" over the entire period 
    netamount= sum(profitlosses)
    print("netamount:" + "$" + str(netamount))
#changes in "Profit/Losses" over the entire period and then the average of those changes
    for i in range(len(profitlosses)-1):
        change_profit.append(profitlosses [i+1]-profitlosses[i])
        print(change_profit)
# calculate the average change in profits 
average_change_profit = sum(change_profit)/ len(change_profit)
average_change = round(average_change_profit, 2)
print("average_change:" + "$" + str(average_change))
#add the max and the min 
increase = max(change_profit)
decrease = min(change_profit)
print("increase:" + str(months[change_profit.index(max(change_profit))+1]) + " " + "($" + str(increase) + ")")
print("decrease:" + str(months[change_profit.index(min(change_profit))+1]) + " " + "($" + str(decrease) + ")")

#convert this to txt file 
filepath = open("output.txt", "w")

filepath.write("Financial Analysis" + "\n")

filepath.write("total Month: " + str(totalmonth) + "\n")

filepath.write("Total: " +"$" + str(netamount) +"\n")

filepath.write("Average Change: " + "$" + str(average_change) + "\n")

filepath.write("Greatest Increase in Profits: " + str(months[change_profit.index(max(change_profit))+1])+ " " + "($" + str(increase) + ")")

filepath.write("Greatest Decrease in Profits: " + str(months[change_profit.index(min(change_profit))+1]) + " " + "($" + str(decrease) + ")")

filepath.close()

             