import sys

def wordsort(arr):
    newarr = []
    while arr:
        lowNum = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        lowdex = 0
        for i in range(len(arr)):
            if (arr[i]<lowNum):
                lowNum=arr[i]
                lowdex=i
        print(lowNum)
        newarr.append(arr.pop(lowdex))
    return newarr




def removespecial(unsorted):
    dic = {}
    for i in range(len(unsorted)):
        word = unsorted[i]
        isAlpha = word.isalpha()
        isAscii = word.isascii()
        if not isAlpha or not isAscii:
            newword = ''.join(filter(str.isalnum, word))
            newword = ''.join(filter(str.isascii, newword))
            dic[newword] = word
            unsorted[i] = newword
    return dic


def returnspecial(sortedl, dic):
    for i in range(len(sortedl)):
        if sortedl[i] in dic.keys():
              sortedl[i] = dic[sortedl[i]]
    return sortedl



unsortedList = []
userInput = sys.stdin


for line in userInput:
           line = line.lower().strip('\n')
           append = unsortedList.append
           append(line)

dic = removespecial(unsortedList)

sortedList = wordsort(unsortedList)

sortedList = returnspecial(sortedList, dic)

for word in sortedList:
    sys.stdout.write(word)
    sys.stdout.write('\n')
