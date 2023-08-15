import jieba
import jieba.analyse


stopwords = set('， 。 ： ？ ！ “ ” ‘ ’ ; { } [ ] ( ) 【 】 / \\ （ ） 、 《 》'.split())


def cut_words1(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            word_list = []
            line = line.strip("\n").strip("\r").strip("\t").strip("\"").strip()
            words = jieba.analyse.textrank(line, topK=20, withWeight=False, allowPOS=('a', 'ad', 'an', 'd', 'vd'))
            for word in words:
                if word not in stopwords:
                    word_list.append(word)
            cut_result1.write("\n".join(word_list))
            # cut_result.write("\n")
            cut_result1.flush()


def cut_words2(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            word_list = []
            line = line.strip("\n").strip("\r").strip("\t").strip("\"").strip()
            words = jieba.analyse.textrank(line, topK=20, withWeight=False, allowPOS=('a', 'ad', 'an'))
            for word in words:
                if word not in stopwords:
                    word_list.append(word)
            cut_result2.write("\n".join(word_list))
            # cut_result.write("\n")
            cut_result2.flush()


for i in range(1):
    with open('%d.txt' % (i + 2008), 'r', encoding='UTF-8') as f:
        cut_result1 = open("%d after cut_jieba.txt" % (i + 2008), 'w', encoding='UTF-8')
        cut_words1('%d.txt' % (i + 2008))
        cut_result2 = open("%d after cut_jieba.txt" % (i + 2008), 'a', encoding='UTF-8')
        cut_words2('%d.txt' % (i + 2008))

