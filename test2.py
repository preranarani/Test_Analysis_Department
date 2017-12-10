
#importing date and datetime object
from datetime import datetime,date

#importing calendar object
import calendar

#initialising two date objects
firstDay = date(1990,2,2)
lastDay= date(2000,2,2)

#finding number of totaldays between two dates 
totalDays=(lastDay-firstDay).days

#finding the total number of week and odd days
weekDays=totalDays/7
oddDays=totalDays%7

#finding the day's name of starting day of the 1st date
dayNum=firstDay.weekday()
dayNum=dayNum%7


#creating a new list containing the names of days
weekNames=list(calendar.day_name)

#printing the number of thursdays
for i in range(1,oddDays+1):
		if(weekNames[dayNum]=='Thursday'):
				print "number of Thursdays: {}".format(weekDays+1)
		dayNum=(dayNum+1)%7
for i in range(i+1,oddDays+3):
		if(weekNames[dayNum]=='Thursday'):
				print "number of Thursdays: {}".format(weekDays)
		dayNum=(dayNum+1)%7
		
		


