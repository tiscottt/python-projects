from getpass import getpass
#Processing Input and Output
number = input("Please enter a number: ")
print number
name = raw_input("Please enter your name: ")
print name
age = raw_input("Please enter your age: ")
age = float(age)
print age
weight = raw_input("Please enter your weight: ")
weight = int(weight)
print weight
password = getpass()
print password
year = raw_input("What year were you born [ex. 1980]? ")
year = year.strip()
if len(year)!=4 or not year.isdigit():
	print "Wrong year format"
else:
	print "You were born in", year
#format output
name2="hannah"
time = "morning"
print "Good "+time+", "+name2+". How are you?"

greeting="Good {}, {}. How are you doing?"
name3 = "Tony"
time2 = "Evening"
print greeting.format(time2, name3)

specials_text = "Good {time3}! Today's specials are: {special1} and {special2}."
time3= "afternoon"
food1 = "eggs"
food2= "bacon"
print specials_text.format(time3=time3, special1=food1, special2=food2)

line = "Teams in Toronto: {0}, {1}, {2}"
print line.format("Leafs", "Raps", "Jays")