#The date we need to retrieve
#1. The total numver of votes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total of votes each candidate won
#5. The winner of the eletion based on popular vote

import csv
dir (csv)
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)