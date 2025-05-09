# -*- coding: utf-8 -*-
"""pandas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AXuchcXfE078JNAUKZOW2X6bhSgey92P
"""

import pandas as pd
data=[1,2,3,4]
print(data)


Series= pd.Series(data)
print(Series)

import pandas as pd
List =pd.Series([1,2,3,4],index=['a','b','c','d'])

List

# creating data frames using list

data =[1,2,3,4,5]
df = pd.DataFrame(data)
df

series = pd.Series([4,5], index = ["a", "b"])
print(series)
type(series)
df = pd.DataFrame(series)

print(df)
type(df)

# creating dataframe using numpy

import numpy as np
import pandas as pd

array = np.array([[400,500],["abhi","ravi"]])
df = pd.DataFrame({"name" : array[1],"salary" : array[0]})

df

df = pd.DataFrame(np.random.randint(0,10,(3,3)),columns=['x1','x2','x3'])

import numpy as np
import pandas as pd

df

import pandas as pd

df1=pd.DataFrame({
    'A' : ["A0","A1","A2"],
    'B' : ["B0","B1","B2"]
})

print(df1)

df2=pd.DataFrame({
    'A' : ["A4","A5","A6"],
    'B' : ["B4","B5","B6"]
})

print(df2)

result=pd.concat([df1,df2])     # axis=0
print(result)

result=pd.concat([df1,df2], axis=1)         # axis1
print(result)

import pandas as pd

df1=pd.DataFrame({
    'A' : ["A0","A1","A2"],
    'B' : ["B0","B1","B2"]
})

df2=pd.DataFrame({
    'A' : ["A4","A5","A6"],
    'B' : ["B4","B5","B6"]
})

result=pd.concat([df1,df2], ignore_index=True)
print(result)

# 1. inner merge

import pandas as pd

df1=pd.DataFrame({
    'key' : ["a","b","c","d"],
    'value' : [1,2,3,4]
})

df2=pd.DataFrame({
    'key' : ["b","d","e","f"],
    'value' : [5,6,7,8]
})

result= pd.merge(df1,df2, on='key', how='inner')
print(result)

# left join
import pandas as pd

df1=pd.DataFrame({
    'key' : ["a","b","c","d"],
    'value' : [1,2,3,4]
})

df2=pd.DataFrame({
    'key' : ["b","d","e","f"],
    'value' : [5,6,7,8]
})

result= pd.merge(df1,df2, on='key', how='left')
print(result)

# right join
import pandas as pd

df1=pd.DataFrame({
    'key' : ["a","b","c","d"],
    'value' : [1,2,3,4]
})

df2=pd.DataFrame({
    'key' : ["b","d","e","f"],
    'value' : [5,6,7,8]
})

result= pd.merge(df1,df2, on='key', how='right')
print(result)

# outer join
import pandas as pd

df1=pd.DataFrame({
    'key' : ["a","b","c","d"],
    'value' : [1,2,3,4]
})

df2=pd.DataFrame({
    'key' : ["b","d","e","f"],
    'value' : [5,6,7,8]
})
result = pd.merge(df1, df2, on='key', how='outer')
print(result)

from google.colab import drive
drive.mount('/content/drive')



import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
file_path ='/content/drive/My Drive/Colab Notebooks/dataset/mtcars2.csv'

cars=pd.read_csv(file_path)

print(cars)

cars.mpg = cars.mpg.astype(str)

type(cars)

cars.head(10) #view first 10 records

cars.tail(2)  # view last records

cars.shape

# concise summery
cars.info()

#mean
mean_values=cars.mean(numeric_only=True)
print(mean_values)

#median
median_values=cars.median(numeric_only=True)
print(median_values)

#standers deviation
std_values=cars.std(numeric_only=True)
print(std_values)

#max values
cars.max(numeric_only=True)
cars.max

cars.count()

cars.describe()  # all statitics summery data

cars=cars.rename(columns={'Unnamed: 0':'model'})
print(cars)

cars=cars.rename(columns={'wt':'weight'})
print(cars)

import pandas as pd
cars.qsec=cars.qsec.fillna(cars.qsec.mean())   # replace null values to mean
cars

#slicing of data

print(cars.iloc[ : ,4])      # [  : ALL ROWS ,4COLUMNS]

cars.iloc[ : , : ]

cars.iloc[ 2:11,5:9]

# indexing by label

cars.loc[0:6,"mpg"]

cars.loc[0:6,"mpg":"qsec"]  # more than one column

import pandas as pd
file_path ='/content/drive/My Drive/Colab Notebooks/dataset/Sample - Superstore.xls'

data=pd.read_excel(file_path)

print(data)

#drop unwanted column/rows
data= data.drop(columns=['row ID'])
print(data)

data = data.drop(index=2)
print(data)

# sorting dta

cars.sort_values(by='cyl')

cars.sort_values(by='cyl', ascending=False)

cars.sort_values(by='mpg', ascending=False)  # descending order

# filtering records more than 6 cylinder
cars['cyl'] >= 6

filter1=cars ['cyl'] >= 6
filter_new = cars[filter1]
filter_new

cars=[(cars ['cyl'] >= 6) & ( cars ['hp'] >300)]

cars[(cars['cyl']>6)&(cars['mpg']>20)]

# Commented out IPython magic to ensure Python compatibility.
# matplotlib

import matplotlib.pyplot as plt
# %matplotlib inline
y = cars['hp']
x= range(44)
plt.plot(x,y)

cars.mpg = cars.mpg.astype(str)

# Commented out IPython magic to ensure Python compatibility.
#import matplotlib
import matplotlib.pyplot  as plt
# %matplotlib inline
#see how hp varies with each car with line plot
y2 = cars['disp']
x  = range(44)
plt.plot(x,y2)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot  as plt
# %matplotlib inline
y1 = cars['hp']
y2 = cars['disp']
#see how both hp and disp varies
x  = range(44)
plt.plot(x,y1)
plt.plot(x,y2)
plt.legend()

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot  as plt
# %matplotlib inline
y1 = cars['hp']
y2 = cars['disp']
x  = range(44)
#area plot of hp and disp
plt.stackplot(x,y1,colors = 'r', alpha = 0.7)
plt.stackplot(x,y2,colors = 'c', alpha = 0.5)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot  as plt
# %matplotlib inline
y1 = cars['hp']
y2 = cars['disp']
x  = range(44)
#plot both line plot and area plot to see the margin
plt.plot(x,y1, linewidth = 2.0, color = 'c')
plt.stackplot(x,y1,colors = 'r', alpha = 0.7)
plt.plot(x,y2, linewidth = 1.0, color = 'r')
plt.stackplot(x,y2,colors = 'black', alpha = 0.5)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot  as plt
# %matplotlib inline
y = cars['hp']
x  = range(32)
#model to list
x1 = cars['model'].tolist()
#adding figure to adjust figsize
fig = plt.figure(figsize = (30,15))
#see how hp changes with bar plot
plt.bar(x1,y,color="purple", alpha=0.9)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot  as plt
# %matplotlib inline
y = cars['hp']
x  = range(32)
x1 = cars['model'].tolist()
fig = plt.figure(figsize = (17,10))
#to avoid the overlapping issue plot horizontal bar plot
plt.barh(x1,y, color="purple", alpha=0.8)

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot  as plt
# %matplotlib inline

x=np.arange(0,10,1)
y=2*x+5

plt.plot(x,y,color='green',marker='*')
plt.show()

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot  as plt
# %matplotlib inline

x=np.arange(0,10,1)
y=2*x+5

fig=plt.figure(figsize=(10,5))
plt.plot(x,y,linewidth =2.0,linestyle='--',color='k',alpha =1.0,marker ='p',markerfacecolor ='r')
plt.title("line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend(['line1'],loc='best')
plt.grid(True)
plt.show()

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot  as plt
# %matplotlib inline

x=np.arange(0,10,1)
y1=2*x+5
y2=3*x+10

plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title("graph1")

plt.subplot(1,2,2)
plt.plot(x,y2, color='red')
plt.title("graph2")
plt.show()

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot  as plt
# %matplotlib inline

x=np.arange(0,10,1)
y1=2*x+5
y2=3*x+10

plt.subplot(1,2,1)
plt.plot(x,y1,linewidth=2.0,linestyle="-.",color="r",alpha=0.8,marker='*')
plt.grid(True)
plt.title("graph1")

plt.subplot(1,2,2)
plt.plot(x,y2, linewidth=2.0,linestyle="-.",color="m",alpha=0.8,marker='s')
plt.grid(True)
plt.title("graph2")
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# bar plot

import numpy as np
import matplotlib.pyplot  as plt
# %matplotlib inline

data={'apple':20,'mangoes':15,'lemon':20,'orange':30}
names = list(data.keys())
values = list(data.values())

fig=plt.figure(figsize=(5,5))
plt.bar(names,values)
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# scatter chart


import matplotlib.pyplot  as plt
# %matplotlib inline
import numpy as np

a=[10,20,30,40,50,60,70,80]
b=[5,3,2,5,5,4,4,2]
x=[2,3,4,5,7,8,3,5]

plt.scatter(a,b,color='b')
plt.scatter(a,x,color='k')
plt.title('scatter')
plt.show()

# Commented out IPython magic to ensure Python compatibility.

import matplotlib.pyplot  as plt
# %matplotlib inline
import numpy as np

a=[10,20,30,40,50,60,70,80]
b=[5,3,2,5,5,4,4,2]
x=[2,3,4,5,7,8,3,5]

plt.scatter(a,b,color='b',s=100,edgecolors='y',marker='o',alpha=0.7)
plt.scatter(a,x,color='k',s=150,edgecolors='y',marker='d',alpha=1)
plt.legend(['b','x'],loc='best')
plt.title("scatter plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.savefig("scatter plot.pdf")
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# histogram

import matplotlib.pyplot  as plt
# %matplotlib inline

age=[10,17,35,65,47,80,57,46,8,84,5,54,74,65,12,45,65,34,23,29,23]
plt.hist(age,bins=[1,20,40,60,80,100])
plt.show()

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot  as plt
# %matplotlib inline

numbers=[10,12,16,19,11,20,26,28,30,38,35,34,45,60,68,64,62,70,78,75,79,85,84,94,95]
plt.hist(numbers,bins=[0,20,40,60,80,100],edgecolor='#000000',color='#ff2331')
plt.title("histogram example")
plt.xlabel("range of value")
plt.ylabel("frequency of value")
plt.grid(True)
plt.savefig("histogram plot.pdf")
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# pie charts

import matplotlib.pyplot  as plt
# %matplotlib inline

animal=['dog','cat','cow','monkey']
count=[40,23,49,60]

plt.pie(count,labels=animal,autopct='%1.1f%%',shadow=True,startangle=90,explode= (0,0.1,0,0))
plt.title("pie chart example")
plt.show

# Commented out IPython magic to ensure Python compatibility.
#donut chart

import matplotlib.pyplot  as plt
# %matplotlib inline

group_names = ["groupa","groupb","groupc"]
group_size = [20,30,50]
size_centre =[10]

a,b,c =[plt.cm.Blues,plt.cm.Reds,plt.cm.Greens]
pie1 = plt.pie(group_size,labels=group_name,autopct='%1.1f%%',radius=1.5,shadow=True,startangle=90)
pie2 = plt.pie(size_centre, radius=1.0,colors='w')
plt.show

# Commented out IPython magic to ensure Python compatibility.
# area chart
import matplotlib.pyplot  as plt
# %matplotlib inline

x=range(1,15)
y=[1,4,3,6,7,9,6,4,2,5,4,3,2,3]

plt.stackplot(x,y,colors='r',alpha=0.4)
plt.plot(x,y,color='k',marker='d')
plt.grid(True)
plt.show()











