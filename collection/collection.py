import collections

s = '流感每年都來，2009年爆發新流感疫情，造成1312人重症、50人死亡；2015至2016年的流感季，重症患者達2018人，425人死亡，各大醫院一床難求。衛福部疾管署提醒，流感與一般感冒不同，嚴重時有致命危險，接種疫苗是最有效的預防方法。'

t = '今年度的公費流感疫苗將於十月一日開打，將提供600萬劑疫苗給符合條件者接種。流感疫苗雖然每年打，但每年民眾的疑問都不太一樣，以下整理今年民眾常見的10大流感疫苗接種問題，一次解答。'
# s共有幾個字(包含標點符號)
print(len(s))

# s共有幾個不同的字(包含標點符號)
print(len(set(s)))

# 若list_s=list(s)，那麼如何從list_s兜成字串
print(''.join(list(s)))

# 有哪些字在s與t都出現過(包含標點符號)
print(set(list(s)) & set(list(t)))

# s與t共有多少不同的字(包含標點符號)
print(len(set(list(s)) | set(list(t))))

# 有多少字只出現在s沒出現在t(包含標點符號)
print(len(set(list(s)) - set(list(t))))

# 哪一個字在s與t出現次數最多(包含標點符號)
print(collections.Counter(list(s) + list(t)).most_common(1))
