import os
import csv

csvpath = os.path.join('', 'PyPoll/Resources', 'election_data.csv')

totalVotes = 0
candidates = []
candidateVotes = {}

with open(csvpath, newline='') as f:
  csvreader = csv.reader(f, delimiter=',')
  next(csvreader, None)
  for row in csvreader:

    candidateVotes[row[2]] += 1



print("Election Results")
print("___________________________")
print(f"Total Votes: {totalVotes}")
print("___________________________")
print(candidates)
print(candidateVotes)
