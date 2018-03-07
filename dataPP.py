#!/usr/bin/env python


#program to help get data into usable format
#pull power data over (can add it using id from power table, this will eliminate duplicates)
#Will need to ask for sunrise, set times 

# will need to ask for hourly sky and temp data


#can output csv file for the entire set


import MySQLdb
import sys


#need database name
db=MySQLdb.connect('localhost','root','aq12ws','client')
curs=db.cursor()


#power table 
#id 			int
#currentIn		int
#recDateTime  	datetime





#weather data

#recDatetime 	datetime
#forDate		date		key
#hour			int			key
#sky			int
#temp			int
#precip			decimal(5,3)
#cond			text
#SunRise		time
#SunSet			time


#id 		int
#current	int
#sky		int
#temp		int
#recTime	datetime
#Srise		time
#Sset 		time
#dayPerc	int


def getTwoDayData():
	#get json data from server and return it
	return None

def processServerData(data):
	#process and update database based on 

if __name__=="__main__":
	#get all current power records
	#store these in mlData (id will not allow dups)
	#request current day and Next day data from server
	
	#{day:7, month:12, year:2018,today{hours[1{sky:15,temp:45},2{sky:30,temp:47}......],sunrise:654564,sunset:6544654},tomorrow {hours[1{sky:15,temp:45},2{sky:30,temp:47}......],sunrise:654564,sunset:6544654}
	
