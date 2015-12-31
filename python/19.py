# how many sundays were first day of month during 20th century (1 jan 1901 to 31 dec 2000)
# 1 jan 1900 was a monday
# 30 days month 9, 4, 6, 11
# 31 days month 1, 3, 5, 7, 8, 10, 12
# 29 days month 2 in leap years: divisible by 4, not divisible by 100 unless by 400
# 28 days month 2 otherwise
monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
monthDaysL = [31,29,31,30,31,30,31,31,30,31,30,31]

#number days 0 - 6 for Sun - Sat
#start with 1900, know 1 jan 1900 was monday
firstDayOfMonth = [1]
#the rest for 1900, which was not a leap year
for k in xrange(11):
	firstDayOfMonth.append((firstDayOfMonth[-1] + monthDays[k])%7)

def leap(y):
	b = False
	if y%4==0:
		b = True
	if y%100==0:
		b = False
	if y%400==0:
		b = True
	return b

total = 0
for y in xrange(1901,2001):
	y = 1901
	firstDayOfMonth = [(firstDayOfMonth[-1] + monthDays[11])%7]
	for k in xrange(11):
		if leap(y):
			firstDayOfMonth.append((firstDayOfMonth[-1] + monthDaysL[k])%7)
		else:
			firstDayOfMonth.append((firstDayOfMonth[-1] + monthDays[k])%7)

	total += firstDayOfMonth.count(0)

print total