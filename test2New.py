
#importing date and datetime object
from datetime import datetime,date

#importing calendar object
import calendar

#take date input from user
firstDay = datetime.strptime(raw_input('date1(%Y,%m,%d) : '),'%Y,%m,%d')
lastDay=  datetime.strptime(raw_input('date2(%Y,%m,%d) : '),'%Y,%m,%d')

#find the totalDays
totalDays=(lastDay-firstDay).days

#find the accurate number of weeks(not in fraction) and remaining odd days
weekDays=totalDays/7
oddDays=totalDays%7

#find the firstday's name of the first date
dayNum=firstDay.weekday()
dayNum=dayNum%7

#save weekDays in new lilst
weekNames=list(calendar.day_name)

#print the numbers of all days present between two dates
for i in range(1,oddDays+1):
		print ("number of {0} : {1}".format(weekNames[dayNum],weekDays+1))
		dayNum=(dayNum+1)%7

for i in range(i+1,oddDays+3):
		print ("number of {0} : {1}".format(weekNames[dayNum],weekDays))
		dayNum=(dayNum+1)%7
		
		


