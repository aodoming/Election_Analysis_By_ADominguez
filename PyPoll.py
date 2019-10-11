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

# Open the election results and read the file.
with open(file_to_load) as election_data:

#To do: read and analyze the data here.
#Read the file object with the reader function.
    file_reader = csv.reader(election_data)

#Print each row in the CSV file. iterarte through the file_reader variable and print each row.
    headers = next(file_reader)
    print(headers)
      

