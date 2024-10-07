#Dependencies
import os
import csv

#files to load and output
file_to_load = os.path.join("Resources", 'python-challenge\PyPoll\Resources\election_data.csv')  # Input file path
file_to_output = os.path.join("analysis", 'python-challenge\PyPoll\analysis\poll_analysis.txt')  # Output file path

#Start each variable
total_votes = 0 #Total number of votes cast

#Track the names of each candidate, and the votes they get
candidate_names = []
vote_counts = {}
candidate_name = ' '

#Winning Candidate and Winning Count Tracker
winning_candidate = ' '
winning_vote_count = 0

#Open CSV file
with open('python-challenge\PyPoll\Resources\election_data.csv') as election_data:
    reader = csv.reader(election_data)

    header = next(reader)
    
    for row in reader:
        #increment the total vote count
        total_votes += 1
        #retrieve the candidate name
        candidate_name = row[2]
        #if the candidate name isn't in the list, add it 
        if candidate_name not in candidate_names:
            candidate_names.append(candidate_name)
            #initialize the candidates vote count 
            vote_counts[candidate_name] = 0

        #increment that candidate's vote count
        vote_counts[candidate_name] += 1

print(vote_counts)

with open('python-challenge\PyPoll\analysis\poll_analysis.txt', "w") as poll_analysis:

    # Print the total vote count (to terminal)
    print(f'Total Votes: {total_votes}')

    # Write the total vote count to the text file
    poll_analysis.write(f"Total Votes: {total_votes}\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in vote_counts:
        # Get the vote count and calculate the percentage
        votes = vote_counts[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_vote_count:
            winning_vote_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
        poll_analysis.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

    # Generate and print the winning candidate summary
    print(f"Winner: {winning_candidate}")
    poll_analysis.write(f"Winner: {winning_candidate}\n")
