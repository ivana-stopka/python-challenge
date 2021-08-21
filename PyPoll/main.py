# PyPoll

# Analyse the votes on PyPoll.csv and calculate the following
	# The total number of votes cast
	# The complete list of candidates who received votes
	# The percentage of votes each candidate won
	# The total number of votes each candidate won
	# The winner ofthe election based on popular vote

# Import the modules

import os
import csv
import shutil

# Print the heading
print("---------------------------")
print("Election Results")
print("---------------------------")

# Define list variables
votes = []
Khan = []
Correy = []
Li = []
O_Tooley = []
Error = []

# Set path for the csv file
PyPoll_csv = os.path.join("Resources","election_data.csv")

# Open the csv
with open(PyPoll_csv) as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=',')

	csv_header=next(csv_file)
	
	# Loop through the csv and copy data from the 3rd column [2] to a list called 'votes'
	for col in csv_reader:
 		votes.append(col[2])

# Count the number of votes by counting all the elements inside the 'votes' list
vote_count = len(votes)
print("Total Votes: ",vote_count)

print("---------------------------")

# Create a list for each candidate with their votes from the main votes list. 
for vote in votes:
	if vote == "Khan":
		Khan.append(vote)
	elif vote == "Correy":
		Correy.append(vote)
	elif vote == "Li":
		Li.append(vote)
	elif vote == "O'Tooley":
		O_Tooley.append(vote)	
	else:
		Error.append(vote)
	
# Confirm no additional candidate names were returned in the error list (or typos of candidate names) with print. Note: Once checked, I will turn this off for final analysis.
#print(Error)

# Calculate the percentage and total of votes for each candidate.
Khan_percent = len(Khan)/len(votes)
formatted_Khan_percent = "{:.3%}".format(Khan_percent)

Correy_percent = len(Correy)/len(votes)
formatted_Correy_percent = "{:.3%}".format(Correy_percent)

Li_percent = len(Li)/len(votes)
formatted_Li_percent = "{:.3%}".format(Li_percent)

O_Tooley_percent = len(O_Tooley)/len(votes)
formatted_O_Tooley_percent = "{:.3%}".format(O_Tooley_percent)

# Print results for each candidate
print("Khan: ",formatted_Khan_percent,"at",len(Khan),"votes")
print("Correy: ",formatted_Correy_percent,"at",len(Correy),"votes")
print("Li: ",formatted_Li_percent,"at",len(Li),"votes")
print("O'Tooley: ",formatted_O_Tooley_percent,"at",len(O_Tooley),"votes")

print("---------------------------")

# Calculate and print the winner
candidate_lib = {"Khan":len(Khan),"Correy":len(Correy),"Li":len(Li),"O'Tooley":len(O_Tooley)}

v=list(candidate_lib.values())
k=list(candidate_lib.keys())
winner = k[v.index(max(v))]

print("Winner: ",winner)

print("---------------------------")

# Write to a text file the results
lines = ["Election Results",
	"Total Votes: " + str(vote_count),
	"Khan: " + str(formatted_Khan_percent) + " at " + str(len(Khan)) + " votes",
	"Correy: " + str(formatted_Correy_percent) + " at " + str(len(Correy)) + " votes",
	"Li: " + str(formatted_Li_percent) + " at " + str(len(Li)) + " votes",
	"O'Tooley: " + str(formatted_O_Tooley_percent) + " at " + str(len(O_Tooley)) + " votes",
	"Winner: " + str(winner)] 
with open('results.txt','w') as f:
    f.write('\n'.join(lines))

# Move new result.txt file to Analysis folder
source = "results.txt"
destination = "Analysis"
new_path=shutil.move(source,destination)