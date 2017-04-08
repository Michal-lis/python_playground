bestStudent = {}  # dictionary
f = open('stud.txt')
for line in f:
    name, grade = line.split()
    bestStudent[grade] = name
f.close()

bestStudentStr = ""

for i in sorted(bestStudent.keys(), reverse=True):
    print(bestStudent[i] + " scored a " + i)
    bestStudentStr += bestStudent[i] + ' scored a ' + i + ".\n"
print(bestStudentStr)


outToFile=open('tworzonypliki.txt', mode = 'w', encoding='utf-8')
outToFile.write(bestStudentStr)

outToFile.close()