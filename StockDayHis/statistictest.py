#coding=utf-8
import MySQLdb
import pandas as pd
import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
import sys


timelist = []
def isZhangTing(time, idd, df):
        df1 = df[df['stock_id']==idd]
        yesterday = getpreviousdDay(time)
        a = df1[df1['time']==time]
        b = df1[df1['time']==yesterday]
        if b.shape[0] ==0:
            return 0
        elif a.iat[0,4] >= round(b.iat[0,3]*1.1,2):
                return 1
        else:
                return 0

def NumberZhangting(time, df):
        df2 = df[df['time']==time]
        num=0
        print "the number of today is"
        print df2.shape[0]
        for i in range(0,df2.shape[0]):
                if (isZhangTing(time, df2.iat[i,0],df) == 1):
                        num+=1
                        #print num
        return num

def Daban(time, df):
        num = 0
        yesterday = getpreviousdDay(time)
        print "yesterday is "
        print yesterday
        today = df[df['time'] == time]
        print "the number of today is"
        print today.shape[0]
        total=NumberZhangting(yesterday, df)
        print "The total number is"
        print total
        for j in range(0,today.shape[0]):
                if (isZhangTing(time, today.iat[j,0], df) == 1 and isZhangTing(yesterday, today.iat[j,0],df)):
                        num += 1
        print "The num is"
        print num
        if total == 0:
           return 0
        else:
           return float(num)/total

def getpreviousdDay(str):
        index1 = timelist.index(str)
        if( index1 != -1):
                return timelist[index1-1]
        else:
                return -1


def getTimeList(s):
        cursor.execute("SELECT distinct time from alphabulldb.stockDayHis where time between %s and %s",s)
        result = cursor.fetchall()
        timelist = []
        for timeValue in result:
            timeValue = timeValue[0].strftime('%Y-%m-%d')
            timelist.append(timeValue)
        return timelist



#s1 = '2011-01-04'
#s2 = '2011-01-28'
arg = sys.argv
s1 = arg[1]
s2 = arg[2]
s = [s1,s2]

'''
timelist = getTimeList(s)
cursor.execute("SELECT * FROM stockDayHis where time between %s and %s",s)
result = cursor.fetchall()
print "before dataframe"
df = pd.DataFrame(columns=('stock_id', 'time', 'open_price', 'close_price', 'high_price', 'low_price', 'volume'))
for row in result:
        time = row[1].strftime('%Y-%m-%d')
        tmp = [row[0],time,row[2],row[3],row[4],row[5],row[6]]
        t = pd.DataFrame(tmp).T
        t.columns = df.columns
        df = pd.concat([df,t],ignore_index=True)
print "load in dataframe"
print df.shape[0]
'''

df = pd.read_csv('data.csv')
df_fortime = pd.read_csv('data.csv')
df_fortime.columns = ['a','stock_id', 'time', 'open_price', 'close_price', 'high_price', 'low_price', 'volume','b']
df.columns = ['a','stock_id', 'time', 'open_price', 'close_price', 'high_price', 'low_price', 'volume','b']
df = df.drop('a',1)
df = df.drop('b',1)
df_fortime = df_fortime.drop('a',1)
df_fortime = df_fortime.drop('b',1)
df_fortime.drop_duplicates(subset = 'time',inplace = True)
time = df_fortime['time']
timelist=list(time)
print timelist

count = 0
y = []
for str in timelist:
        if str == s1:
           continue
        else:
			count += 1
			y.append(Daban(str, df))
x = range(len(timelist))

print len(x)
print len(y)

plt.figure(figsize = (8,4))
plt.plot(x,y,"b--",linewidth=1)  
plt.xlabel("date") 
plt.ylabel("success")  
#plt.xticks(range(len(timelist)-1), timelist, **kwargs)  # Set locations and labels 
plt.title("daban")
plt.savefig("daban.png") 
print "save ok"   
plt.show()   


