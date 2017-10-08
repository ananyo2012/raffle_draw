import random
import csv

participants = {}

with open('data.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		participants[row['id']] = row['name']

raffle_set = list(participants.keys())
winner_id = random.choice(raffle_set)
winner_name = participants[winner_id]

del participants[winner_id]

print(winner_name)


with open('data.csv', 'w') as csvfile:
	fieldnames = ['id', 'name']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for key in participants:
		writer.writerow({'id' : key, 'name' : participants[key]})
