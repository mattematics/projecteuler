#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

h = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',\
	14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',\
	30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',\
	100:'onehundred',200:'twohundred',300:'threehundred',400:'fourhundred',500:'fivehundred',600:'sixhundred',\
	700:'sevenhundred',800:'eighthundred',900:'ninehundred',1000:'onethousand'}

letters = []
for k in xrange(1,1001):
	if k == 1000:
		letters.append(len('onethousand'))
		break
	if k > 99:
		hPlace, tPlace, oPlace = str(k)
	elif k > 9:
		hPlace, tPlace, oPlace = [0]+list(str(k))
	else:
		hPlace, tPlace, oPlace = [0,0]+list(str(k))
	hPlace, tPlace, oPlace = int(hPlace), int(tPlace), int(oPlace)
	w = ""
	if hPlace > 0:
		w += h[hPlace*100]
		if tPlace == 0 and oPlace == 0:
			letters.append(len(w))
			continue
		else:
			w += "and"
	if tPlace > 1:
		w += h[tPlace*10]
		if oPlace > 0:
			w += h[oPlace]
	elif tPlace != 0 or oPlace != 0:
		w += h[tPlace*10 + oPlace]
	letters.append(len(w))

print sum(letters)