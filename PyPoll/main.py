import os
import csv

import operator

csvpath = os.path.join('', 'PyPoll/Resources', 'election_data.csv')

totalVotes = 0
candidates = []
candidateVotes = {}

with open(csvpath, newline='') as f:
  csvreader = csv.reader(f, delimiter=',')
  next(csvreader, None)
  for row in csvreader:
    if row[2] not in candidates:
      candidates.append(row[2])
      candidateVotes[row[2]] = 0
    candidateVotes[row[2]] += 1
    totalVotes += 1



print("Election Results")
print("___________________________")
print(f"Total Votes: {totalVotes}")
print("___________________________")
for key, value in candidateVotes.items():
  print(f"{key}: {round(value/totalVotes*100, 4)}% ({value})")
print("___________________________")
print("Winner: "+max(candidateVotes.items(), key=operator.itemgetter(1))[0])
print("___________________________")
