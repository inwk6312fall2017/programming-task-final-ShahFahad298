import re

file = open("running-config.cfg" , "r")

for line in file:
	word = line.strip()
	print (word)
match = re.match(r"([a-z]+)([0-9]+)", 'file', re.I)
if match:
    items = match.groups()
print(items)

for int in items:
	if int ==192:
	  
