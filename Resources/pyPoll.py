#The data we need to retrieve 
#1. the total number of votes cast 
#2. A complete list of candidates who received votes 
#3. The % of votes each candidate won 
#4. The total number of votes each candidate won 
#the winner of the election based on popular vote 

#Import the datetime class from the datetime module 
#import datetime
#use the now () attribute on the datetime class to get the present time 
##now=datetime.datetime.now()
#print("The time right now is ",now)
#import csv
#directory= dir(csv)
#print(directory)

#assign a variable for the file to load and the path 
#file_to_load ='Resources\election_results.csv'
#open the file 
#with open(file_to_load) as election_data: 

    #print(election_data)

from cgitb import text
import csv

import os 
#assign a variable for the fle and the path to load 
csvpath=os.path.join("..","Resources","election_results.csv")
#open the file and read 
#with open(csvpath)as csvfile: 
 #print(csvfile)
csvSave=os.path.join("..","Resources","election_results.txt")
#1. Initialize a total vote counter 
total_votes=0 
#candidate options 
candidate_options=[]
#candidate dictionary
candidate_votes={}
winning_candidate=""
winning_count=0
winning_percent=0
#open the election results and read the file 
with open(csvpath) as electionData:
#write some data to the file 
    #txtFile.write("Hello World\n")
   # txtFile.write("Araphoe\n Denver\nJefferson")
#to do: read the file 
    fileReader=csv.reader(electionData)
#print rows 
    #for row in fileReader: 
        #print(row[0])
    headers=next(fileReader)
#print each row in the CSV file 
    for row in fileReader: 
    #2. Add to the total votes counter 
        total_votes +=1
    #print candidate name from each row 
        candidate_name=row[2]
    #if the candidate name doesnt match any existing candidate 
        if candidate_name not in candidate_options:
        #add the unique candidate name 
            candidate_options.append(candidate_name)
        # begin tracking the candidate vote counte 
            candidate_votes[candidate_name]=0
        #add vote to the candidate count 
        candidate_votes[candidate_name]+=1
    #save the results to our text file 
    with open(csvSave,"w") as text_file:
        election_results=(
                f"\nElection Results\n"
                f"----------------------\n"
                f"Total Votes:{total_votes :,}\n"
                f"----------------------\n"
        )
        print(election_results, end="")
        #save teh final vote count in text file 
        text_file.write(election_results)
        for candidate_name in candidate_votes: 
        #retrive candidate vote count 
            votes=candidate_votes[candidate_name]
        #calculate percentage of votes 
            vote_percent=float(votes)/float(total_votes)*100

        # print(f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n")   
            candidate_results=(f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n") 
            text_file.write(candidate_results)
    #determine the wining vote count and candidate 
    #determine if the votes are greater than the wining count 

            if (votes>winning_count) and (vote_percent>winning_percent):
        #if treu the set winning count =votes and winning percent=vote percent 
                winning_count=votes
                winning_percent=vote_percent 
                winning_candidate=candidate_name
        winning_summary=(
            f"------------------\n"
            f"Winner :{winning_candidate}\n"
            f"Winner Vote Count: {winning_count:,}\n"
            f"Winner Vote Percentage: {winning_percent:.1f}%\n"
            f"--------------------\n")
        text_file.write(winning_summary)
    #3 Printe the candidate list 
                        
    #print(winning_summary)