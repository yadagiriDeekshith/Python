import pandas as pd

d = {'name': ["Raju", "Siva", "Anu"], 'age': [34, 67, 89], 'Marks': [90, 92, 96]}
data = pd.DataFrame(d)

#print(data)

#res=data.describe()

#print(res)
#res=data['name']
#res=data.head(1)
#res=data.tail(1)
#res=data[data['name']=='Raju']
#res=data[data['Marks']>90]

res=data.loc[0:1,['name','age']]

print(res)
