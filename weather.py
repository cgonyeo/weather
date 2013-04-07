from bs4 import BeautifulSoup

import sys
sys.argv

counter = 0
dayCounter = 0
numDays = 6
daysPerLine = 3
lineLength = 20

args = sys.argv

if(len(args) > 2):
	daysPerLine = int(args[2])
borderLine = "+"
for i in range(daysPerLine):
	borderLine += "-" * lineLength + "+"

#Open the file
f = open(args[1],"r")
weather = "".join(f.readlines())
soup = BeautifulSoup(weather)

fct_days_list = soup.find_all(id="fct_days")
if(len(fct_days_list) == 0):
	print "Error: couldn't find fct_days div"
	exit()
fct_days = fct_days_list[0]

fctScrollContain_list = fct_days.find_all("div", class_="fctScrollContain")
if(len(fctScrollContain_list) == 0):
	print "Error: couldn't find fctScrollContain div"
	exit()
fctScrollContain = fctScrollContain_list[0]

fct_days_list = list(fctScrollContain.children)[1::2]

dayLine = "|"
conditionsLine = "|"
forecastLine = "|"

nowCond = soup.find_all(id="nowCond")[0]
nowTemp = soup.find_all(id="nowTemp")[0]
condText = nowCond.getText().strip().splitlines()
tempText =  nowTemp.getText().strip().splitlines()

line1 = tempText[2] + ", " + condText[2]
line2 = tempText[4] + " " + tempText[5].strip()

numSpaces = (lineLength * daysPerLine + daysPerLine - 1) - len(line1)
line1 = "|" + (" " * (numSpaces // 2)) + line1 + (" " * (numSpaces // 2 + numSpaces % 2)) + "|"
numSpaces = (lineLength * daysPerLine + daysPerLine - 1) - len(line2)
line2 = "|" + (" " * (numSpaces // 2)) + line2 + (" " * (numSpaces // 2 + numSpaces % 2)) + "|"

print "+" + "-" * (lineLength * daysPerLine + daysPerLine - 1) + "+"
print line1.encode("utf8")
print line2.encode("utf8")

print borderLine
for day in fct_days_list:
	dateList = day.find_all("div", class_="fctDayDate")
	if(len(dateList) > 0 and dayCounter < numDays):
		date = day.find_all("div", class_="fctDayDate")[0]
		conditions = day.find_all("div", class_="fctHiLow")[0]
		forecast = day.find_all("div", class_="fctDayConditions")[0]

		if(counter == daysPerLine):
			print dayLine.encode("utf8")
			print conditionsLine.encode("utf8")
			print forecastLine.encode("utf8")
			print borderLine.encode("utf8")
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

print dayLine.encode("utf8")
print conditionsLine.encode("utf8")
print forecastLine.encode("utf8")
print borderLine.encode("utf8")
