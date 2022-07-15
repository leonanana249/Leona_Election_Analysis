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

import csv
import os 
#assign a variable for the fle and the path to load 
csvpath=os.path.join("..","Resources","election_results.csv")
#open the file and read 
#with open(csvpath)as csvfile: 
 #print(csvfile)
csvSave=os.path.join("..","Resources","election_results.txt")
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
    print(headers)