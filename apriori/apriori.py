from utils import get_apriori
import csv

data = []
with open('adult.csv', newline='') as csvfile:
    for row in  csv.reader(csvfile, delimiter=',', quotechar='|'):
        data.append(row)

result = get_apriori(data, 3, 3)

for item in result.items():
    print(item)

