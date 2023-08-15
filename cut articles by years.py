import json


def read_json_file(file_path):
    """
    读取json文件
    """
    with open(f"{file_path}",encoding='utf-8') as f:
        res = json.load(f)
        #print(f"length of file{len(res)}")
        #print(f"type of file{type(res)}")
        return res


all_data = read_json_file("D:/all_data_美.json")

list_articles1 = all_data.get("articles")
list_articles2 = all_data.get("articles")
time_list = []
content_list = []

for item2 in list_articles2:
    for key2 in item2:
        item2[key2] = item2.get("date")
        item2[key2] = item2[key2].strip("\n").strip("\r").strip("\t").strip("\"").strip()
        time_list.append(item2[key2])
        break


for item1 in list_articles1:
    for key1 in item1:
        item1[key1] = item1.get("content")
        content_list.append(item1[key1])
        break


'''
for i in range(28729):
    if time_list[i][0:4] == '2008':
        f2008 = open('2008.txt', 'a+', encoding='UTF-8')
        f2008.write(content_list[i] + '\n')
        f2008.close()
    if time_list[i][0:4] == '2009':
        f2009 = open('2009.txt', 'a+', encoding='UTF-8')
        f2009.write(content_list[i] + '\n')
        f2009.close()
    if time_list[i][0:4] == '2010':
        f2010 = open('2010.txt', 'a+', encoding='UTF-8')
        f2010.write(content_list[i] + '\n')
        f2010.close()
    if time_list[i][0:4] == '2011':
        f2011 = open('2011.txt', 'a+', encoding='UTF-8')
        f2011.write(content_list[i] + '\n')
        f2011.close()
    if time_list[i][0:4] == '2012':
        f2012 = open('2012.txt', 'a+', encoding='UTF-8')
        f2012.write(content_list[i] + '\n')
        f2012.close()
    if time_list[i][0:4] == '2013':
        f2013 = open('2013.txt', 'a+', encoding='UTF-8')
        f2013.write(content_list[i] + '\n')
        f2013.close()
    if time_list[i][0:4] == '2014':
        f2014 = open('2014.txt', 'a+', encoding='UTF-8')
        f2014.write(content_list[i] + '\n')
        f2014.close()
    if time_list[i][0:4] == '2015':
        f2015 = open('2015.txt', 'a+', encoding='UTF-8')
        f2015.write(content_list[i] + '\n')
        f2015.close()
    if time_list[i][0:4] == '2016':
        f2016 = open('2016.txt', 'a+', encoding='UTF-8')
        f2016.write(content_list[i] + '\n')
        f2016.close()
    if time_list[i][0:4] == '2017':
        f2017 = open('2017.txt', 'a+', encoding='UTF-8')
        f2017.write(content_list[i] + '\n')
        f2017.close()
    if time_list[i][0:4] == '2018':
        f2018 = open('2018.txt', 'a+', encoding='UTF-8')
        f2018.write(content_list[i] + '\n')
        f2018.close()
    if time_list[i][0:4] == '2019':
        f2019 = open('2019.txt', 'a+', encoding='UTF-8')
        f2019.write(content_list[i] + '\n')
        f2019.close()
    if time_list[i][0:4] == '2020':
        f2020 = open('2020.txt', 'a+', encoding='UTF-8')
        f2020.write(content_list[i] + '\n')
        f2020.close()
    if time_list[i][0:4] == '2021':
        f2021 = open('2021.txt', 'a+', encoding='UTF-8')
        f2021.write(content_list[i] + '\n')
        f2021.close()
    if time_list[i][0:4] == '2022':
        f2022 = open('2022.txt', 'a+', encoding='UTF-8')
        f2022.write(content_list[i] + '\n')
        f2022.close()
'''
