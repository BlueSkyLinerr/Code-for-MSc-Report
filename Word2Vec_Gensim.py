import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
'''
inp = 'total after cut_jieba fixed3.txt'
model = Word2Vec(LineSentence(inp), vector_size=200, window=5, min_count=1, workers=multiprocessing.cpu_count())
model.save("word2vec_Gensim.model")
'''
# 给所有词标号
with open('total after cut_jieba fixed3.txt', 'r', encoding='UTF-8') as f:
    a = 0
    words_dict = {}
    for lines in f:
        words_dict[lines.strip('\n')] = a
        a += 1


model = Word2Vec.load("word2vec_Gensim.model")
for i in range(1):
    with open("%d after cut_jieba fixed3.txt" % (i + 2008), 'r', encoding='UTF-8') as f1, open("%dcsv.txt" % (i + 2008), 'w', encoding='UTF-8') as f2:
        f2.write('source,target,weight' + '\n')
        for line in f1.readlines():
            for word in line.split():
                for i in range(5):
                    res = model.wv.most_similar(word)
                    f2.write(str(words_dict[word]) + ',')
                    f2.write(str(words_dict[res[i][0]]) + ',')
                    f2.write(str(res[i][1]))
                    f2.write('\n')

'''

model = Word2Vec.load("word2vec_Gensim.model")
with open("2022 after cut_jieba fixed3.txt", 'r', encoding='UTF-8') as f1, open("2022csv.txt", 'w', encoding='UTF-8') as f2:
    f2.write('source,target,weight' + '\n')
    for line in f1.readlines():
        for word in line.split():
            for i in range(5):
                res = model.wv.most_similar(word)
                f2.write(str(words_dict[word]) + ',')
                f2.write(str(words_dict[res[i][0]]) + ',')
                f2.write(str(res[i][1]))
                f2.write('\n')
'''