
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
max_length = len(max(words1,word2,word3))
for word in file1:
	for word in file2:
		for word in flie3:
			if len(words1) or len(words2) or len(words) == max_lenght:
			return ( max_lenght)
print(max_lenght)

