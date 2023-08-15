import collections


'''
给所有词标号
'''
with open('total after cut_jieba fixed3.txt', 'r', encoding='UTF-8') as f:
    a = 0
    words_dict = {}
    for lines in f:
        words_dict[lines.strip('\n')] = a
        a += 1


"""
删除重复词
"""
for i in range(1):
    readtxt = "%d after cut_jieba.txt" % (i + 2008)
    writetxt = "%d after cut_jieba fixed1.txt" % (i + 2008)
    lines_seen = set()
    outfile = open(writetxt, 'w', encoding='UTF-8')
    with open(readtxt, 'r', encoding='UTF-8') as f:
        for line in f:
            if line not in lines_seen:
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()
'''
# 删除长词
'''
for i in range(1):
    result = open("%d after cut_jieba fixed2.txt" % (i + 2008), 'w', encoding='UTF-8')
    with open("%d after cut_jieba fixed1.txt" % (i + 2008), 'r+', encoding='UTF-8') as f:
        for line in f.readlines():
            word_list = []
            for word in line.split():
                if len(word) <= 2:
                    word_list.append(word)
            result.write(" ".join(word_list))
            result.write("\n")
            result.flush()
'''
# 删除空行
'''
for i in range(1):
    file1 = open("%d after cut_jieba fixed2.txt" % (i + 2008), 'r', encoding='utf-8')  # 要去掉空行的文件
    file2 = open("%d after cut_jieba fixed3.txt" % (i + 2008), 'w', encoding='utf-8')  # 生成没有空行的文件
    for line in file1.readlines():
        if line == '\n':
            line = line.strip("\n")
        file2.write(line)
    file1.close()
    file2.close()


for i in range(1):
    with open("%d after cut_jieba.txt" % (i + 2008), 'r', encoding='UTF-8') as f1:
        str1 = f1.read().split('\n')  # 将文章按照空格划分开
    with open("total after cut_jieba fixed3.txt", 'r', encoding='UTF-8') as f3, open('%d word counter test.txt' % (i + 2008), 'w', encoding='UTF-8') as f2:
        f2.write('id,word,weight' + '\n')
        for lines in f3.readlines():
            for word in lines.split():
                f2.write(str(words_dict[word]) + ',')
                f2.write(word + ',')
                for j in collections.Counter(str1).keys():
                    if word == j:
                        f2.write(str(collections.Counter(str1)[word]))
                    if word not in collections.Counter(str1).keys():
                        f2.write('0')
                        break
                f2.write('\n')

'''
with open("2014 after cut_jieba.txt", 'r', encoding='UTF-8') as f1:
    str1 = f1.read().split('\n')  # 将文章按照空格划分开
with open("total after cut_jieba fixed3.txt", 'r', encoding='UTF-8') as f3, open('2014 word counter test.txt', 'w', encoding='UTF-8') as f2:
    f2.write('id,word,weight' + '\n')
    for lines in f3.readlines():
        for word in lines.split():
            f2.write(str(words_dict[word]) + ',')
            f2.write(word + ',')
            for j in collections.Counter(str1).keys():
                if word == j:
                    f2.write(str(collections.Counter(str1)[word]))
                if word not in collections.Counter(str1).keys():
                    f2.write('0')
                    break
            f2.write('\n')
'''
