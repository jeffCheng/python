#隨機模組
import random
#隨機選取 
data=random.choice([1,5,6,10,20])
print(data)
data=random.sample([1,5,6,10,20],3)
print(data)
# 隨機調換順序(洗牌的概念)
data=[10,20,30,40]
random.shuffle(data)
print(data)

# 隨機取得亂數
data=random.random() #0~1之間的隨機亂數 
print(data)
data=random.uniform(30,60) #30~60之間的隨機亂數 
print(data)

# 取得常態分配亂數
data=random.normalvariate(100,10)
#平均數100，標準差10 得到資料大{多數}在90~100間
print(data)

#統計模組 
import statistics as stat
data=stat.mean([1,3,5,7])#平均數
print(data)
data=stat.median([1,30,5,7,9])#中位數
print(data)
data=stat.stdev([1,30,5,7,9])#標準差
print(data)