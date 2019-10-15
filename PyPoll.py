###################                 READ  & WRITE FROM DATA    #########
# Read Data From File/using Direct path.
#Assign a variable for the file to load and the path.
file_to_load = 'Resources\election_results.csv'

# open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.
   print(election_data)


#Read Data from File(2)/using Indirect Path.
#Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

##############################################################################
# Write Files to Python- this code uses the open() & close() functions.
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file.
outfile.close()

# Write Files to Python(2)- below code uses the with statement instead of open() & close() functions.
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

       # Write three counties to the file. 
       # Add the "newline escape sequence" \n
          # Write three counties to the file.
     txt_file.write("Counties in the Election\n----------------\n")
     txt_file.write("Arapahoe\nDenver\nJefferson")

##################################################################################
#Reading the election results from file.
#Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis",  "election_analysis.txt")


#1. Initialize a total vote counter.
total_votes = 0 
#Declare a new list to hold name of candidate. 
candidate_options = []
#1. Declare an empty dictionary.
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

#To do: read and analyze the data here.
#Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read the header row. this is how we get rid of the header in the count.
    headers = next(file_reader)

    #Print each row in the CSV file. iterarte through the file_reader variable and print each row.
    for row in file_reader:
       #2.Add to the total vote count.
       total_votes += 1

       #Print the candidate name from each row.
       candidate_name = row[2]

       #If the candidate does not match any existing candidate...Get the unique candidate names of the candidates list
       if candidate_name not in candidate_options:
          #Add the candidate name to the candidate list.
          candidate_options.append(candidate_name)

          #2. Begin tracking candidate's vote count. Candidate name counted once/uniquely. 
          candidate_votes[candidate_name] = 0

       #Add a vote to that candidate's count where applicable, every iteration of rows.
       candidate_votes[candidate_name] += 1

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:

   # Print the final vote count to the terminal.
   election_results = (
      f"\nElection Results\n"
      f"-------------------------\n"
      f"Total Votes: {total_votes:,}\n"
      f"-------------------------\n")
   print(election_results, end="")

   # Save the final vote count to the text file.
   txt_file.write(election_results)
     
   #Determine the percentage of votes for each candidate by looping through the counts. 
   #1. Iterate through the candidate list.
   for candidate in candidate_votes:
      #2. Retrieve vote count of a candidate.
      votes = candidate_votes[candidate]
      #3. Calculate the percentage of votes.ha 
      vote_percentage = float(votes) / float(total_votes) * 100
      #4. Print the candidate name and percentage of votes.
      #print(f"{candidate}: received {vote_percentage:}% of the vote.")
            
      #What will above "for statement" code do: print out each candidtae's name, vote count, and percentage of votes to terminal.
      #print (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")   #(Code modified: this commented out to modify code to write to a text file)
      candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
      # Print each candidate, their voter count, and percentage to the terminal.
      print(candidate_results)
      #  Save the candidate results to our text file.
      txt_file.write(candidate_results)

      #Determine winning vote count and candidate.
      #1. Determine if the vote count that was calculated is greater than the winning_count & vote % > than winning %.
      if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate

   #What will above "if statement" code do: print out winning candidate, vote count, and percentage to terminal.
         
   #Print out the winning candidate summary.
   winning_candidate_summary = (
      f"-------------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: {winning_count:,}\n"
      f"Winning Percentage: {winning_percentage:.1f}%\n"
      f"-------------------------\n")
   print(winning_candidate_summary)

   #Save the winning candidate's name to the text file.
   txt_file.write(winning_candidate_summary)

   #Print each candidate, their voter count, and percentage to the terminal
   #print(candidate_results)
   #Save the candidate results to our text file.
   #txt_file.write(candidate_results)



         
   # #3. Print the candidate list.
   # print(candidate_options)

   # Print the candidate vote dictionary.
   #print(candidate_votes)



    


