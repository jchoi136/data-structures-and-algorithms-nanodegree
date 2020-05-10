"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

dic = {}

for item in texts:
    dic[item[0]] = 1
    dic[item[1]] = 1

for item in calls:
    dic[item[0]] = 1
    dic[item[1]] = 1


print("There are {} different telephone numbers in the records.".format(len(dic)))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
