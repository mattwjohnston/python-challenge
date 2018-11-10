import os
import csv

csvpath = os.path.join('', 'PyBank/Resources', 'budget_data.csv')

monthCount = 0.0
totalNet = 0
averageChange = 0
greatestInc = 0
greatestIncDate = ""
greatestDec = 0
greatestDecDate = ""

lastNet = 0.0
totalChange = 0.0


with open(csvpath, newline='') as f:
  csvreader = csv.reader(f, delimiter=',')
  next(csvreader, None)
  for row in csvreader:
    monthCount += 1.0
    totalNet += int(row[1])
    change = (int(row[1])-lastNet)
    if lastNet != 0.0:
      totalChange += change
    if change > greatestInc:
      greatestInc = change
      greatestIncDate = row[0]
    elif change < greatestDec:
      greatestDec = change
      greatestDecDate = row[0]
    lastNet = int(row[1])


print("Financial Analysis")
print("___________________________")
print(f"Total Months: {monthCount}")
print(f"Total: ${totalNet}")
print(f"Average Change: {totalChange/monthCount}")
print(f"Greatest Increase in Profits: {greatestIncDate} (${greatestInc})")
print(f"Greatest Decrease in Profits: {greatestDecDate} (${greatestDec})")


output_file = os.path.join("PyBank", "output.csv")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["___________________________"])
    writer.writerow([f"Total Months: {monthCount}"])
    writer.writerow([f"Total: ${totalNet}"])
    writer.writerow([f"Average Change: {totalChange/monthCount}"])
    writer.writerow([f"Greatest Increase in Profits: {greatestIncDate} (${greatestInc})"])
    writer.writerow([f"Greatest Decrease in Profits: {greatestDecDate} (${greatestDec})"])
