import sys


sys.setrecursionlimit(10**6)

def makePartition(array, low, nums):
    pivot, part = nums[low], array
    for index in range(array, low):
        if nums[index] <= pivot:
            nums[index], nums[part] = nums[part], nums[index]
            part += 1
            nums[part], nums[low] = nums[low], nums[part]
    return part

def quickSort(array, low, nums):
    if len(nums) == 1:
        return nums
    if array < low:
        splitArr = makePartition(array, low, nums)
        quickSort(array, splitArr-1, nums)
        quickSort(splitArr+1, low, nums)
    return nums

def wordsort(arr):
    maxlen = 0
    for word in arr:
        if (len(word)>maxlen): maxlen = len(word)
    for i in range(len(arr)):
        ros = " " * (maxlen-len(arr[i]))
        arr[i] += ros
    numlist = quickSort(0, len(arr)-1, arr)
    sortedarray = list(map(str.rstrip, numlist))
    return sortedarray

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
