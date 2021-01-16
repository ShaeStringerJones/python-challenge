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

                
print(candidates)
 


#The percentage of votes each candidate won

print((candidates['Khan']/total_votes)*100)
print((candidates['Correy']/total_votes)*100)
print((candidates['Li']/total_votes)*100)
print((candidates["O'Tooley"]/total_votes)*100)


  

#The winner of the election based on popular vote.
winner = max(candidates)
print(winner)



# print("Election Results")
# print("-------------------------")
# print("Total Votes:")
# print("-------------------------")
# print("candidate & stats")
# print("candidate & stats")
# print("candidate & stats")
# print("candidate & stats")
# print("Winner")
# print("-------------------------")


    
