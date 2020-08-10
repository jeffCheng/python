
# coding: utf-8

# In[1]:


import pandas as pd


# In[12]:


data = pd.Series([20,10,15])


# In[13]:


print(data)


# In[14]:


print(data.max())


# In[15]:


print(data.median())


# In[16]:


data = data*2


# In[17]:


data


# In[18]:


data=data==20
print(data)


# In[24]:


data = pd.DataFrame(
{"name": ["Amy","John", "Bod"],
 "salary":[33333, 444444 ,333333]
}
)


# In[25]:


print(data)


# In[26]:


print(data["name"])


# In[27]:


print(data["salary"])


# In[28]:


print(data.iloc[0])


# In[29]:


print(data.iloc[1])


# In[33]:


import pandas as pd
data = pd.Series([3,10,20,5,-12])
# 各種數學、統計運算
print(data.sum(),data.max(),data.prod())
print(data.mean(),data.median(),data.std())
print(data.nlargest(3),data.nsmallest(2))
# nlargest(3) => 取前三大數字
# nsmallest(2) => 取最小的兩個數字


# In[34]:


import pandas as pd
data = pd.Series(["您好","Python","Pandas"])
# 各種字串操作，都定義在str底下
print(data.str.lower(),data.str.upper(),data.str.len())
print(data.str.cat(sep=","),data.str.contains("P"))
print(data.str.replace("您好","Hello"))
# data.str.cat(sep=",") => 把每個字串都用,串接起來
# data.str.replace("您好","Hello") => Hello取代您好


# In[35]:


data = pd.Series([5,4,-2,3,7], index=["a","b","c","d","e"])
print(data)
# >>> a    5
# >>> b    4
# >>> c   -2
# >>> d    3
# >>> e    7
# >>> dtype: int64
# 觀察資料
print("資料型態", data.dtype)
print("資料數量", data.size)
print("資料索引", data.index)
# >>> 資料型態 int64
# >>> 資料數量 5
# >>> 資料索引 Index(['a', 'b', 'c', 'd', 'e'], dtype='object')


# In[36]:


data = pd.Series([5,4,-2,3,7], index=["a","b","c","d","e"])
# 取得資料：根據順序、根據索引index
print(data[2],data[0])
print(data["e"],data["d"])
# >>> -2 5
# >>> 7 3


# In[37]:


# 數字運算：基本、統計、順序
print("總和",data.sum())       # >>> 總和 17
print("最大值",data.max())     # >>> 最大值 7
print("標準差",data.std())     # >>> 標準差 3.361547262794322
print("中位數",data.median())  # >>> 中位數 4.0
print("最大的三個數",data.nlargest(3))
# >>> 最大的三個數 e    7
# >>> a    5
# >>> b    4
# >>> dtype: int64
print("累積連乘",data.prod())
print("平均值",data.mean())
# >>> -840
# >>> 3.4
print("最小的兩個數",data.nsmallest(2))
# >>> 最小的三個數 c   -2
# >>> d    3
# >>> b    4
# >>> dtype: int64


# In[38]:


# 字串運算：基本、串接、搜尋、取代
import pandas as pd
data = pd.Series(["您好","Python","Pandas"])
print(data.str.lower())  # 全部變小寫
# >>> 0        您好
# >>> 1    python
# >>> 2    pandas
# >>> dtype: object

print(data.str.upper())  # 全部變大寫
# >>> 0        您好
# >>> 1    PYTHON
# >>> 2    PANDAS
# >>> dtype: object

print(data.str.len())  # 算出每個字串的長度
# >>> 0    2
# >>> 1    6
# >>> 2    6
# >>> dtype: int64

print(data.str.cat(sep="-"))  # 把字串串起來，可以自訂串接的符號
# >>> 您好-Python-Pandas

print(data.str.contains("P"))  # 判斷每個字串是否包含特定的字元
# >>> 0    False
# >>> 1     True
# >>> 2     True
# >>> dtype: bool
print(data.str.replace("您好","哩厚"))  # 後面的字串取代前方的
# >>> 0        哩厚
# >>> 1    Python
# >>> 2    Pandas
# >>> dtype: object


# In[2]:


data = pd.DataFrame(
{"name": ["Amy","John", "Bod"],
 "salary":[33333, 444444 ,333333]
}
)


# In[3]:


data


# In[13]:


data = pd.DataFrame(
{"name": ["Amy","John", "Bod"],
 "salary":[33333, 444444 ,333333]
}, index=["a","b","c"]
)


# In[14]:


data


# In[15]:


data.size


# In[16]:


data.shape


# In[17]:


data.index


# In[18]:


data.iloc[1]


# In[20]:


data.loc['a']


# In[24]:


data["name"]


# In[25]:


names = data["name"]


# In[26]:


names.str.upper()


# In[27]:


data["r"] = [222, 32233 ,34343]


# In[29]:


data["rank"] = pd.Series([3, 4 ,1], index=["a", "b","c"])


# In[30]:


data


# In[31]:


data['cp'] = data["r"]/data["salary"]


# In[32]:


data


# In[33]:


import pandas as pd


# In[34]:


data = pd.Series([30,15,20])
condition = [True,False,True]
filteredData = data[condition]
print(filteredData)


# In[35]:


data = pd.Series([30,15,20])
condition = data > 18
print(condition)
filteredData = data[condition]
print(filteredData)


# In[36]:


data = pd.Series(["您好","Python","Pandas"])
condition = [False,True,True]
filteredData = data[condition]
print(filteredData)


# In[37]:


ata = pd.Series(["您好","Python","Pandas"])
condition = data.str.contains("P")
print(condition)
filteredData = data[condition]
print(filteredData)


# In[38]:


data = pd.DataFrame({
    "name":["Amy","Bab","Charles"],
    "salary":[30000,50000,40000]
})
print(data)
condition = [False,True,True]
filteredData = data[condition]
print(filteredData)


# In[39]:


data = pd.DataFrame({
    "name":["Amy","Bab","Charles"],
    "salary":[30000,50000,40000]
})
condition = data["salary"]>=40000
print(condition)
filteredData = data[condition]
print(filteredData)


# In[40]:


data = pd.DataFrame({
    "name":["Amy","Bab","Charles"],
    "salary":[30000,50000,40000]
})
condition = data["name"]=="Amy"
print(condition)
filteredData = data[condition]
print(filteredData)

