tableData =[['apple', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'mouse', 'goose']]

listMaxSize = [0,0,0]

def printTable():
    for i in range(len(tableData)):
        for el in tableData[i]:
            if listMaxSize[i] < len(el):
                listMaxSize[i] = len(el)
#    print(listMaxSize)

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(listMaxSize[j]+1), end='')
        print()
        



printTable()
#print(range(len(tableData)))