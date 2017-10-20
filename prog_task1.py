
file1 = open("Book1.txt" , "r")

for line in file1:
	word = line.strip()	
	words1 = word.split(',')
	
file2 = open("Book2.txt" , "r")
for line in file2:
	word2 = line.strip()
	words2 = line.split(',')
	
file3 = open("Book3.txt" , "r")
for line in file3:
	word3 = line.strip()
	words3 = word3.split(',')
list1 = []
list2 = []
	
for word in file1:
	for word in file2:
		for word in flie3:
			if word in words1 > words2 and words:
				word.apped(list1)
			return list1
			elif word in words2 > words1 and words3:
				word.append(list2)
			elif word in words3 > words2 and words1:
				

