# -*- coding:utf-8 -*-
import pandas as pd
data = pd.read_excel("G:\langrensha_liuzhu\9.xlsx",sheet_name="Sheet1",names=["roomName","createdOn"])

print(data)
# print(type(data))
# print(data.columns)
# print(data.loc["roomName"])
print(data.iloc[:,0].values)
data2 = data.iloc[:,0].values
print(type(data2))
# data2.to_string("./roomName.txt")
with open("./roomName.txt","w",encoding='utf-8') as f:
    for item in data2:
        print(item)
        f.write(str(item)+"，")

