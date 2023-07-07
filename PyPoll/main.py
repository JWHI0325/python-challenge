#pypoll
#the total number of months included in dataset 
import os
import csv

filepath = os.path.join("Resources", "election_data.csv")

#Variables 
votes=[]
county=[]
candidate=[]
candidate_dictionary={}
candidates_w_Votes=[]
Percentage_Votes=[]
Total_numberVotes=0

Row = [5,10,15]

with open(filepath, "r") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")  
    csv_header=next(csvreader)
    print(f"header: {csv_header}")


    for row in csvreader:
      Total_numberVotes = Total_numberVotes + 1 
      candidate_names = row[2]  

      if candidate_names not in candidate:
         candidate.append(candidate_names)
         #print(candidate)
         candidate_dictionary[candidate_names]=0
         print(candidate_dictionary)
      candidate_dictionary[candidate_names]= candidate_dictionary + 1
       


    
    #print(Total_numberVotes)
    
        