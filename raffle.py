import random
import csv
import time
from progress.bar import Bar

class RaffleDraw:
    def __init__(self, filename):
        self.participants = {}
        self.filename = filename
        self.read_csv(self.filename)


    def get_winner(self):
        print("\n\n")
        bar = Bar('And the winner is...', max=10)
        for i in range(10):
            [x for x in range(999999)]  # short pause
            bar.next()
        bar.finish()

        time.sleep(3)

        raffle_set = list(self.participants.keys())
        winner_id = random.choice(raffle_set)
        winner_name = self.participants[winner_id]

        del self.participants[winner_id]
        self.write_csv(self.filename)

        print("\n\n\t{}".format(winner_name))
        print("\t{}\n\n".format(winner_id))
        print("-" * 60 + "\n")

    def read_csv(self,filename):
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.participants[row['id']] = row['name']

    def write_csv(self, filename):
        with open(filename, 'w') as csvfile:
            fieldnames = ['id', 'name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for key in self.participants:
                writer.writerow({'id' : key, 'name' : self.participants[key]})


raffle = RaffleDraw('data.csv')
raffle.get_winner()
