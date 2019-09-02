import csv

with open('dummyData.csv', mode='r') as dummyData:
    csv_reader = csv.reader(dummyData, delimiter=",")
    for row in csv_reader:
        print(row)
