from bs4 import BeautifulSoup

import sys
sys.argv

counter = 0
dayCounter = 0
numDays = 6
daysPerLine = 3

args = sys.argv

f = open(args[1],"r")
weather = "".join(f.readlines())
soup = BeautifulSoup(weather)
fct_days_list = soup.find_all(id="fct_days")
if(len(fct_days_list) == 0):
	exit()
fct_days = fct_days_list[0]
fctScrollContain = fct_days.find_all("div", class_="fctScrollContain")[0]

fct_days_list = list(fctScrollContain.children)[1::2]

dayLine = "|"
conditionsLine = "|"
forecastLine = "|"

lineLength = 20
if(len(args) > 2):
	daysPerLine = int(args[2])

borderLine = "+"

for i in range(daysPerLine):
	borderLine += "-" * lineLength + "+"

print borderLine

for day in fct_days_list:
	dateList = day.find_all("div", class_="fctDayDate")
	if(len(dateList) > 0 and dayCounter < numDays):
		date = day.find_all("div", class_="fctDayDate")[0]
		conditions = day.find_all("div", class_="fctHiLow")[0]
		forecast = day.find_all("div", class_="fctDayConditions")[0]

		if(counter == daysPerLine):
			print dayLine
			print conditionsLine
			print forecastLine
			print borderLine
			dayLine = "|"
			conditionsLine = "|"
			forecastLine = "|"
			counter = 0
		
		if(counter < daysPerLine):
			dayLine += date.string.strip() + (" " *  (lineLength - len(date.string.strip()))) + "|"
			conditionsLine += conditions.getText().strip() + (" " * (lineLength - len(conditions.getText().strip()))) + "|"
			forecastLine += forecast.getText().strip() + (" " * (lineLength - len(forecast.getText().strip()))) + "|"

		counter += 1
		dayCounter += 1
	else:
		pass
for i in range((len(dayLine) - 1) / 21, (daysPerLine * (lineLength + 1) + 1) / 21):
	dayLine += " " * 20 + "|"
	conditionsLine += " " * 20 + "|"
	forecastLine += " " * 20 + "|"

print dayLine
print conditionsLine
print forecastLine
print borderLine
