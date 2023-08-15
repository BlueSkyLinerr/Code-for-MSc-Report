import csv


for i in range(1):
    out = open('%ddata_edge.csv' % (i + 2008), 'w', newline='', encoding='UTF-8')
    csv_writer = csv.writer(out, dialect='excel')
    f = open("%dcsv.txt" % (i + 2008), "r", encoding='UTF-8')
    for line in f.readlines():
        line = line.replace(',', '\t')
        list = line.split()
        csv_writer.writerow(list)

for i in range(1):
    out = open('%ddata_node.csv' % (i + 2008), 'w', newline='', encoding='UTF-8')
    csv_writer = csv.writer(out, dialect='excel')
    f = open("%d word counter test.txt" % (i + 2008), "r", encoding='UTF-8')
    for line in f.readlines():
        line = line.replace(',', '\t')
        list = line.split()
        csv_writer.writerow(list)

'''
out = open('total_data_node.csv', 'w', newline='', encoding='UTF-8')
csv_writer = csv.writer(out, dialect='excel')
f = open("%dcsv.txt" % (i + 2008), "r", encoding='UTF-8')
for line in f.readlines():
    line = line.replace(',', '\t')
    list = line.split()
    csv_writer.writerow(list)
'''