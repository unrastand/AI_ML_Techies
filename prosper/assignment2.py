import csv
import json

with open('C:/Users/USER/Downloads/housing.csv', 'r') as app:
    learner = csv.reader(app)
    index = 0
    for rent in learner:
        index += 1
        print(rent[0])