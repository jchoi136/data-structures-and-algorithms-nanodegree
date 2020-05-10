"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import pandas as pd

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

df = pd.DataFrame(calls, columns = ['calling Number', 'Receiving Number', 'timestamp','seconds'])
print(df)

# print(calls)
# print("{} spent the longest time, {} seconds, on the phone during September 2016.".format())


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

