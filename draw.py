import csv
import random
import time

validtx = []
applicants = 0
csvname = 'history.csv'
entryfee = 0.01

with open(csvname, newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['description'] == 'PAYMENT RECEIVED' and float(row['moneyIn']) > entryfee:
			print("\n %s (%f) (%i)" %(row['tx'], float(row['moneyIn']), applicants + 1))
			validtx.append(row['tx'])
			applicants = applicants + 1
			
			time.sleep(0.1)
			
time.sleep(1)
print("\nOut of %i valid applicants\n\n" %(applicants))
print("The Winner is:\n")
time.sleep(5)
print("%s\n" %(random.choice(validtx)))