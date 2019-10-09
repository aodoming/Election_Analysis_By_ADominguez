#The data we need to retrieve. 
candidates_list = 'Charles C. Stockham", "Diane DeGette", "Raymond A. Doane'
print(candidates_list)

# A complete list of candidates who received votes. Using the Comparison Operators (<,>, <=,<=, == etc) 


candidates_list = ["Charles C. Stockham", "Diane DeGette", "Raymond A. Doane"]
if candidates_list[1] == 'Diane DeGette':
    print(candidates_list[1], ("is in the list of candidates"))  
if candidates_list[2] == 'Raymond A. Doane':
    print(candidates_list[2], ("is in the list of candidates")) 
if candidates_list[0] != 'Raymond A. Doane':
    print(candidates_list[0], ("is in the list of candidates"))


#The total number of votes cast.



#Total number of votes each candidate won.
#The % of votes each candidate won.
#The winner of the election based on popular vote.

#Read Data From File
#Assign a variable for the file to load and the path.
#file_to_load = 'Resources\election_results.csv'

#open the election results and read the file.
#election_data = open(file_to_load, 'r')

#To do: perform analysis.


#close the file.
#election_data.close


#Read file modified with the with() function
#open the election results and read the file.
#with open(file_to_load) as election_data:

    #To do: Perform analysis
   # print(election_data)

#################  Open & Read Files ########

#Add our dependencies.
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = 'Resources\election_results.csv'

#open the election results and read the file.
with open(file_to_load) as election_data:

     #To do: Perform analysis
         print(election_data)



#################  Write to Files ########

# Create a filename variable to a direct or indirect path to the file.
    #file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
   #open(file_to_save, "w")





