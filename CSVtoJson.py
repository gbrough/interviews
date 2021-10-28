#read data from csv file
import csv
import json


#define a function to read csv file
def read_csv(file_name):
    #read csv file
    with open(file_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        #read each row
        for row in reader:
            #print(row)
            #write to json file
            with open('data.json', 'a') as jsonfile:
                jsonfile.write(json.dumps(row))
                jsonfile.write('\n')

#call the function
read_csv('data.csv')
