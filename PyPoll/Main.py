import os
import csv

csvpath = os.path.join('Resources', 'Election_Data.csv')


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
      
    # The total number of votes cast
    data_list = [row for row in csvreader]
   
    total_votes = (len(data_list))
  

#A complete list of candidates who received vote 
#The total number of votes each candidate won
candidates = {}
for row in data_list:
    if row[2] not in candidates.keys():
        candidates[row[2]] = 1
    else:
        candidates[row[2]]=candidates[row[2]]+1


total_Khan=candidates['Khan']
total_Correy=candidates['Correy']
total_Li=candidates['Li']
total_Otooley=candidates["O'Tooley"]
 
#The percentage of votes each candidate won

vp_Khan=(candidates['Khan']/total_votes)*100
vp_Correy=(candidates['Correy']/total_votes)*100
vp_Li=(candidates['Li']/total_votes)*100
vp_Otooley=(candidates["O'Tooley"]/total_votes)*100

  
#The winner of the election based on popular vote.
winner = max(candidates)




print("Election Results")
print("-------------------------")
print("Total Votes:", total_votes)
print("-------------------------")
print("Khan", total_Khan, round(vp_Khan,2))
print("Correy", total_Correy, round(vp_Correy,2))
print("Li", total_Li, round(vp_Li,2))
print("O'Tooley", total_Otooley, round(vp_Otooley,2))
print("Winner:Khan")
print("-------------------------")


    
