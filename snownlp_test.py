from snownlp import SnowNLP

for i in range(1):
    with open("%d after cut_jieba fixed3.txt" % (i + 2008), 'r', encoding='UTF-8') as f:
        avg = 0
        sum = 0
        num = 0
        for line in f.readlines():
            s = SnowNLP(line)
            sentiments = s.sentiments
            sum += sentiments
            num += 1
        # print(sum)
        avg = sum / num
        print(avg)



