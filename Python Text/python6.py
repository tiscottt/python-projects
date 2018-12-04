#Strings

#creating strings
s= "Hello, World"
print s
#staying on same line
print 'Apple:',
print '$1.99/lb'
#string length
name = "Terry"
print len(name)
#string formatting methods
team = "Maple Leafs"
print team.upper()
print team.lower()
print team.capitalize()
print team.title()
birth_year = "1990"
state = "NY"
print birth_year.isdigit()
print state.isalpha()
#String addition
first_name = "Auston"
last_name = "Matthews"
print first_name + " " + last_name
#String multiplication
x = 'hello '
print x*5
y= '9'
print y*10
#comparing strings
c="Leafs"
d="leafs"
print c==d
#Format Strings
sentence = "Hello, and welcome to\nThe thunderdome"
print sentence
header = "Goals\tAssists\tPoints"
print header
path = "C:\\Applications\\"
print path
name2 = "  Billy   "
name3 = "*****Billy***"
print name2.strip()
print name3.strip('*')
print name3.lstrip('*')
print name3.rstrip('*')
#searching/replacing strings
text = "the the the the cat the the the the"
print text.count('the') 
print text.find('cat')
print text.replace('cat', 'dog')
