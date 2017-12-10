from datetime import datetime,date
import calendar

firstDay = date(1990,1,1)
lastDay= date(2000,1,1)

totalDays=(lastDay-firstDay).days

weekDays=totalDays/7
oddDays=totalDays%7

dayNum=firstDay.weekday()
dayNum=dayNum%7

weekNames=list(calendar.day_name)


for i in range(1,oddDays+1):
		if(dayNum==3):
				print "number of Thursdays: {}".format(weekDays+1)
		dayNum=(dayNum+1)%7
for j in range(i+1,oddDays+3):
		if(dayNum==3):
				print "number of Thursdays: {}".format(weekDays)
		dayNum=(dayNum+1)%7
		
		


