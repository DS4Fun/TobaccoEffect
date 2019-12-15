# import csv
#
# with open('Tobacco_cost.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#         print(row)
#         print(row[0])
#         print(row[0],row[1],row[2],)
#
with open('Tobacco_cost.csv') as file:
    d = file.read().replace("\"", "")
    # file.write(d)
    file1 = open("testfile.csv", "w")
    file1.write(d)
