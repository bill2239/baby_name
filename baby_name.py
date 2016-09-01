import os
import pandas as pd
import numpy as np
fileroot = os.path.dirname(os.path.abspath(__file__))
def get_data():
	#import data from government into pandas dataframe
	dict_list=[]
	# interate over all the states baby name data
	for root, dirs, files in os.walk(os.path.join(fileroot,'namesbystate')):
		for file in files:
			if file.endswith(".TXT"):
				print (os.path.join(root, file))
				fin=open(os.path.join(root, file),'r')
				for line in fin.readlines():
					arr=line.strip().split(',')
					#df=pd.DataFrame(arr,columns=['state', 'gender', 'born_yr', 'name', 'count'])
					dict_tmp={'state':arr[0],'gender':arr[1],'born_yr':int(arr[2]),'name':arr[3],'count':int(arr[4])}
					dict_list.append(dict_tmp)
					

	df=pd.DataFrame(dict_list)
	return df

def popular_name(df):
	# get top 10 popular name of all time
	grouped=df[['name','count']].groupby('name',sort=False)
	#sort=False to speed up
	#print grouped
	print grouped.sum().sort('count',ascending=False)[0:9]

def gender_ambiguous_n(df):
	# get the most 20 gender neutral name of all time
	
	df['count'][df['gender']=='F']*=-1
	grouped=df[['name','gender','count']].groupby(['name'],sort=False)	
	group_sum=grouped.sum()
	group_sum['count']=group_sum['count'].abs()

	print group_sum.sort('count')[0:19]
	
def popular_name_byyr(df,yr):
	
	grouped_yr=df[['name','born_yr','count']].groupby(['born_yr'],sort=False).get_group(yr)
	#print grouped.sum()
	return grouped_yr['name'].tolist()[0:3]

	# for name, group in grouped:
	# 	print group
	# 	print group.sum()

	# 	raw_input('please enter')


df=get_data()
#popular_name(df)
#gender_ambiguous_n(df)
print popular_name_byyr(df,1910)