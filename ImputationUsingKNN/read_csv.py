# import csv
#
# with open('Tobacco_cost.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#         print(row)
#         print(row[0])
#         print(row[0],row[1],row[2],)
#

#Here we replace all the double quotes " with empty string.
# The input is a csv file and the output is the "test.csv" file, which containes all the entries of the primary file but without double quotes
with open('Tobacco_cost.csv') as file:
    d = file.read().replace("\"", "")
    # file.write(d)
    file1 = open("testfile.csv", "w")
    file1.write(d)
