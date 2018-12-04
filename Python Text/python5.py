#Example
total = 19 + 9.99 +13.97 + 20 + 15.97 +9.97+10*2
party = 8
print "Receipt for your meal"
if party >=8:
	total = total + total*.2
	print "We've added the tip automatically for parties larger than 8"
print "Total:", total
print "Thank you for dining with us today"	

#Example2 

breakfast_special = "Eggs"
breakfast_notes = "bacon and waffles"
lunch_special = "sandwich"
lunch_notes = "turkey on rye"
dinner_special = "steak"
dinner_notes = "ny strip"

meal_time = raw_input('Which meal time are you eating at [breakfast, lunch, dinner]')
print 'Specials for {}: '.format(meal_time)
if meal_time == 'breakfast':
	print breakfast_special
	print breakfast_notes
elif meal_time == 'lunch':
	print lunch_special
	print lunch_notes
elif meal_time == 'dinner':
	print dinner_special
	print dinner_notes
else:
	print "Sorry, {} isnt valid".format(meal_time)