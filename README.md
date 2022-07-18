# Leona_Election_Analysis
## Overview of Election Audit 
The purpose of this analysis is to present the election audit results to the election commission. The report will cover votes results for each candidate in each of the counties. 


## Election-Audit Results  
There were 369,711 votes in total. Denver has the largest number of county turnout (82.8%, 306,855 votes), followed by Jefferson (10.5%, 38,855 votes). Arapahoe has the least number of votes for the remaining 6.7% (24,801 votes). Regarding the candidate vote results, Diana DeGette has the largest number of votes (73.8%, 272,892 votes), followed by Charles Casper Stockham (23.0%, 85,213 votes). Raymon Anthony Doane has the least number of votes (3.1%, 11,606 votes). Therefore, Diana DeGette won  the election. 

![image](https://user-images.githubusercontent.com/107721712/179436204-0d3cd40e-2082-4037-b328-d7bcb152c15e.png)


## Election-Audit Summary 
The election commission can use the script for future elections with respective modifications. First, if the results file doesn’t have header, header = next(reader) is not required. Second, the user should make sure which column candidate names are recorded. For example, row [2] means candidate names are in the third column. Similarly, the user will need to modify the row number for county name. 
  
![image](https://user-images.githubusercontent.com/107721712/179436772-9decdefb-d58d-4d98-8b6f-5c89ce98cba4.png)
