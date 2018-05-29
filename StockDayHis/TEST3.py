#coding:utf8  
import sys  
from pandas import DataFrame    
import pandas as pd           

df = pd.read_csv('data.csv')
df.columns = ['a','b','c','d','e','f','g','h','i']
'''
df2=df
df2.drop_duplicates(subset = 'e',inplace = True)
time = df2['e']
timelist=list(time)
print time
print timelist
'''
df = df.drop('a',1)
df = df.drop('i',1)
print df
