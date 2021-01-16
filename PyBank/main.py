import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    data_list = [row for row in csvreader]

    total_months = (len(data_list))

    date = []
    pl = []
    change = []
    high=[]
    low=[]
      
    net = 0    
    for _ in range(total_months):
        net = net + int(data_list [_][1])
        date.append(data_list[_][0])
        pl.append(int(data_list[_][1]))
        pl_changes = pl[_] - pl[(_-1)]
        change.append(pl_changes)

    change.pop(0)
    
    
    avg_change = round(sum(change)/len(change),2)

    greatest_increase = max(pl)
    greatest_decrease = min(pl)
   


    date.pop(0)
   
    changes_data = list(zip(date, pl))

    print(changes_data)



    for row in changes_data:

      if row[1] == greatest_increase:
         high = row

      if row[1] == greatest_decrease:
         low = row



print("Financial Analsys")
print("------------------------")
print(f'Total Months: {total_months}''')
print(f'Total: ${net}''')
print(f'Average Change: ${avg_change}''')
print(f'Greatest Increase in Profits: {high[0]} ${high[1]}''')
print(f'Greatest Decrease in Profits: {low[0]} ${low[1]}''')


mystring=f'''
,asmdfdsan
a.skjdgasjg
a.skjdnnfdgk
{total_months}
'''

        









