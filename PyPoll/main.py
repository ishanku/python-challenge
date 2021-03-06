import os

# Module for reading CSV files
import csv
from statistics import mean
csvpath = os.path.join('.', 'Resources', 'election_data.csv')
outputpath = os.path.join('.', 'Output', 'Election_Data_Analysis_Summary.txt')
VoterList =[]
CountryList =[]
CandidateList= []
Candidates = []
CandidateVotes= []
CandidateVotePercentage= []
with open(csvpath, newline='', encoding="utf-8") as csvfile:

	# CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)

	for row in csvreader:
		VoterList.append(row[0])
		CountryList.append(row[1])
		CandidateList.append(row[2])

def unique(CandidateList):
	# For all elements
	for x in CandidateList:
		# check if exists in Candidates or not
		if x not in Candidates:
			Candidates.append(x)
			CandidateVotes.append(0)
			CandidateVotePercentage.append(0)
	# print list
	#for C in Candidates:
		#print(C)
unique(CandidateList)
for i in range(len(CandidateList)):
	#print(CandidateList[i])
	for j in range(len(Candidates)):
		if Candidates[j] == CandidateList[i]:
			CandidateVotes[j] = CandidateVotes[j] +1


for j in range(len(Candidates)):
	CandidateVotePercentage[j] = round((CandidateVotes[j]/len(VoterList))*100,2)
VoteCounter = dict(zip(Candidates,CandidateVotes))
#Find Winner
winner = max(VoteCounter, key=VoteCounter.get)

print("\n--------------------------------------------------------------------------------------------------------------------\n")
print("Election Data Analysis\n")
print("--------------------------------------------------------------------------------------------------------------------\n\n\n")
print(f"Total No Votes: {len(VoterList)}\n")
print("--------------------------------------------------------------------------------------------------------------------")
print("| No \t| List of canditates \t| Percentage of Votes\t| Total No of Votes")
print("--------------------------------------------------------------------------------------------------------------------")
for i in range(len(Candidates)) :
	if len(Candidates[i])>7 :
		print("| " + str(i+1) + "\t" +"|" + "\t" + str(Candidates[i]) + "\t" + "|" + "\t" + str(CandidateVotePercentage[i]) + "%" + "\t\t" + "|" + "\t" + str(CandidateVotes[i]) + "\t" + "|")
	else:
		print(f"| " + str(i+1) + "\t" +"|" + "\t" + str(Candidates[i]) + "\t\t" + "|" + "\t" + str(CandidateVotePercentage[i]) + "%"+ "\t\t" + "|" + "\t" + str(CandidateVotes[i]) + "\t" + "|")
print("--------------------------------------------------------------------------------------------------------------------\n")
#print(f"Winner of the Election: {Candidates[CandidateVotes.index(max(CandidateVotes))]}\n")
print(f"Winner of the Election: {winner}\n")
print("--------------------------------------------------------------------------------------------------------------------\n")


with open(outputpath,"w") as file:
	file.write("\n--------------------------------------------------------------------------------------------------------------------\n")
	file.write("Election Data Analysis\n")
	file.write("--------------------------------------------------------------------------------------------------------------------\n\n\n")
	file.write(f"Total No Votes: {len(VoterList)}\n")
	file.write("--------------------------------------------------------------------------------------------------------------------\n")
	file.write("| No \t| List of canditates \t| Percentage of Votes \t| Total No of Votes\n")
	file.write("--------------------------------------------------------------------------------------------------------------------\n")
	for i in range(len(Candidates)) :
		if len(Candidates[i])>7 :
			file.write("| " + str(i+1) + "\t" +"|" + "\t" + str(Candidates[i]) + "\t" + "|" + "\t" + str(CandidateVotePercentage[i]) + "%"+ "\t\t" + "|" + "\t" + str(CandidateVotes[i]) + "\t" + "|")
		else:
			file.write("| " + str(i+1) + "\t" +"|" + "\t" + str(Candidates[i]) + "\t\t" + "|" + "\t" + str(CandidateVotePercentage[i]) + "%"+ "\t\t" + "|" + "\t" + str(CandidateVotes[i]) + "\t" + "|")
		if winner == Candidates[i]:
			file.write("-->Winner<--")
		file.write("\n")
	file.write("-------------------------------------------------------------------------------------------------------------------\n")
	file.write(f"Winner of the Election: {winner}\n")
	file.write("--------------------------------------------------------------------------------------------------------------------\n")
