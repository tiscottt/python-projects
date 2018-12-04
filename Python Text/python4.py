#if
a=5
if a>5:
	print "Greater than 5"
else:
	print "Five or Less"
#elif
total=40.29
if total>50:
	print "You get free shipping!"
elif total>40:
	print "spend a bit more to get free shipping"
else:
	print "Spend 50$ to get free shipping"
#try/except 
try:
	5/0
except:
	print "Divide by zero"
#try/except2
try:
	5/1
	print "Good to go!"
except:
	print "Dont do that"
#try/except3
b=5
try:
	b=b+1
	b=b/0
except:
	print "Dont do that"
	print b