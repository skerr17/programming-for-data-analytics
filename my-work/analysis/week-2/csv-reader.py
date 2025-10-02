# In this program we will read in the data from the ' data.csv' file 
# and output each line as a list. from Lab 1 Q 1, 2, 3, 4, 5
# Auther: Stephen Kerr

import csv

FILENAME = 'data.csv'
DATADIR = '../../data/'

'''
with open(DATADIR + FILENAME, 'rt') as fp:
    reader = csv.reader(fp, delimiter=',')
    linecount = 0
    total_age = 0
    for line in reader:
        if not linecount: # firt row (header)
            print(f'{line}\n--------------------------')

        else: # all following lines
            print(line)
            total_age += int(line[1]) # sum ages starting from line 2 thus index 1
        
        linecount += 1
    print('--------------------------')
    print(f'Average age; {total_age/(linecount -1):.1f}') # -1 to not count the header row

'''


# Using DictReader to read in the data from the csv file
with open(DATADIR + FILENAME, 'rt') as fp:
    reader = csv.DictReader(fp, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total_age = 0
    for line in reader:
        print(line)
        total_age += int(line['age']) # sum ages starting from line 2 thus index 1
        linecount += 1
    print('--------------------------')
    print(f'Average age; {total_age/(linecount):.1f}') # -1 to not count the header row
