import random
from progress.bar import Bar


PEOPLE = {
     0: 'people 0',
     1: 'people 1',
     2: 'people 2',
     3: 'people 3',
     4: 'people 4',
     5: 'people 5',
     6: 'people 6',
     7: 'people 7',
     8: 'people 8',
     9: 'people 9',
     10: 'people 10',
     11: 'people 11',
     12: 'people 12',
     13: 'people 13',
     14: 'people 14',
     15: 'people 15',
     16: 'people 16',
     17: 'people 17',
     18: 'people 18',
     19: 'people 19',
     20: 'people 20',
     21: 'people 21',
     22: 'people 22',
     23: 'people 23',
     24: 'people 24',
     25: 'people 25',
     26: 'people 26',
     27: 'people 27',
     28: 'people 28',
     29: 'people 29',
     30: 'people 30',
     31: 'people 31',
     32: 'people 32',
     33: 'people 33',
     34: 'people 34',
     35: 'people 35',
     36: 'people 36',
     37: 'people 37',
     38: 'people 38',
     39: 'people 39',
     40: 'people 40',
     41: 'people 41',
     42: 'people 42',
     43: 'people 43',
     44: 'people 44',
     45: 'people 45',
     46: 'people 46',
     47: 'people 47',
     48: 'people 48',
     49: 'people 49'
}


class RaffleDraw:
    PROCESSED = []

    @classmethod
    def get_winner(cls):
        print("\n\n")
        bar = Bar('And the winner is...', max=10)
        for i in range(10):
            [x for x in range(999999)]  # short pause...
            bar.next()
        bar.finish()
        key = random.choice(list(PEOPLE.keys()))
        print("\n\n\t{}".format(PEOPLE[key]))
        print("\t{}\n\n".format(key))
        print("-" * 60 + "\n")

    def parse_excel(self):
        pass