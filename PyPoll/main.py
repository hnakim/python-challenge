#PyPoll

#dependencies
import csv
import os

#create dictionary to contain ballots
voter_counts = {}

#path
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as election_data:
    csvreader= csv.reader(election_data)

    #header row
    header = next(csvreader)

    for row in csvreader:
        #track candidate name from row
        name = row[2]

        #if new candidate is named, add to candidates list
        if name not in voter_counts:
            voter_counts[name] = 1

        #if same candidate, add to vote count
        else:
            voter_counts[name] += 1

#calculate total number of votes cast
total_votes = sum(voter_counts.values())

#find winning count
winning_vote = max(voter_counts.values())
winner = max(voter_counts, key=voter_counts.get)

#print analysis to terminal and to txt file
output_file = os.path.join("analysis", "analysis.txt")
with open(output_file, "w") as txt_file:

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")

#loop through dictionary to get vote count
for candidate_name in voter_counts:
    votes = voter_counts[candidate_name]
    
    #calculate percentage
    percentage = (votes / (total_votes)*100)
    percentage_rounded = round(percentage, 3)

    #candidate and vote summary
    summary = f"{candidate_name}: {percentage_rounded}% ({votes})"

    print(summary)

print("----------------------------")
print(winner)
print("----------------------------")

txt_file.write
