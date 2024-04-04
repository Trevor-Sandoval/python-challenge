import os
import csv
poll_csv = os.path.join("Resources","election_data.csv")

# THIS SCRIPT IS FOR THE "PyPoll PROBLEM" in Module #3 Homework

# Path to the CSV file
file_path = os.path.join("election_data.csv")

# INITIALIZE variables
total_votes = 0
candidate_votes = {}

# Read the CSV file
with open (poll_csv, encoding='utf-8') as csv_file:
    csv_read = csv.reader(csv_file, delimiter=",")
    
    # SKIP the header row
    next(csv_read, None)
    
    # Calculate TOTAL VOTES and CANDIDATE VOTES
    for row in csv_read:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the PERCENTAGE OF VOTES each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Find the winner based on POPULAR VOTES
winner = max(candidate_votes, key=candidate_votes.get)

# Print the ANALYSIS RESULTS
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the analysis results to a text file (.txt)
output_file = "analysis/election_results.txt"
with open(output_file, 'w') as output:
    output.write("Election Results\n")
    output.write("-------------------------\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        output.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
    output.write("-------------------------\n")
    output.write(f"Winner: {winner}\n")
    output.write("-------------------------\n")