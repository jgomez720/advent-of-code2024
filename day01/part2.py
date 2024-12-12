file = open('day1.txt', 'r')
f = file.readlines()
file.close()

firstColumn = []
secondColumn = []

for line in f:
    splitLine = line.split('   ')
    firstColumn.append(splitLine[0])
    secondColumn.append(splitLine[1])
    secondColumn[-1] = secondColumn[-1].replace('\n', '')

firstColumn = list(map(int, firstColumn))
secondColumn = list(map(int, secondColumn))

total_sum = 0

firstColumn.sort()
secondColumn.sort()

# print(firstColumn)
# print(secondColumn)

for i in range(len(firstColumn)):
    currentCount = secondColumn.count(firstColumn[i])
    # print(currentCount)
    total_sum += firstColumn[i] * currentCount
    
print(total_sum)