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





#mlData
#id 		int
#current	int
#sky		int
#temp		int
#recTime	datetime
#Srise		time
#Sset 		time
#dayPerc	int




if __name__=="__main__":
	#get all current power records
	#store these in mlData (id will not allow dups)
	#check for any records with missing sky
