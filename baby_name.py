import os
import pandas as pd
import numpy as np
import matplotlib
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


class BabyName:
	def __init__(self):
		self.df = get_data()


	def popular_name(self):
		# get top 10 popular name of all time
		grouped=self.df[['name','count']].groupby('name',sort=False)
		#sort=False to speed up
		#print grouped
		return grouped.sum().sort('count',ascending=False)[0:9]

	def gender_ambiguous_n(self,n):
		# get the n most gender neutral name of all time
		df = self.df.copy()
		df['count'][df['gender']=='F']*=-1
		#print df
		grouped=df[['name','gender','count']].groupby(['name'],sort=False)	
		group_sum=grouped.sum()
		group_sum['count']=group_sum['count'].abs()

		return group_sum.sort('count')[0:n]

	# get the most 3 popular name in a particular year	
	def popular_name_byyr(self,yr):
		
		grouped_yr=self.df[['name','born_yr','count']].groupby(['born_yr'],sort=False).get_group(yr)
		#print grouped.sum()
		return grouped_yr['name'].tolist()[0:3]

	def popularity_overyr(self):
		pass	

if __name__ == "__main__" :
	b = BabyName()
	print b.popular_name()
	print b.gender_ambiguous_n(3)
	# print b.gender_ambiguous_n(6)
	
	print b.popular_name_byyr(df,1910)

