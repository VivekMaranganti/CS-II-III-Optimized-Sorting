import sys
import re
from string import digits

alpDict = { 0:" ", 1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}
alpDict2 = { " ": 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

def wordtonum(w):
    n = len(w)
    num = 0
    for i in range(n):
        num = num + alpDict2[w[i]]*(27**(n-i-1))
    return num

def numtoword(num):
    word = ""
    if not num:
        return '0'
    while (num):
        mod = num % 27
        num = num // 27
        word = alpDict[mod] + word
    return word
    
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
    numlist = list(map(wordtonum,arr))
    numlist = quickSort(0, len(numlist)-1, numlist)
    sortedarray = list(map(numtoword,numlist))
    sortedarray = list(map(str.rstrip, sortedarray))
    return sortedarray

def removespecial(unsorted):
    dic = {}
    for i in range(len(unsorted)):
        word = unsorted[i]
        isAlpha = word.isalpha()
        isAscii = word.isascii()
        if not isAlpha:
            newword = ''.join(filter(str.isalnum, word))
            dic[newword] = word
            unsorted[i] = newword
        if not isAscii:
            newword = ''.join(filter(str.isascii, newword))
            dic[newword] = word
            unsorted[i] = newword
    return dic

def returnspecial(sortedl, dic):
    for i in range(len(sortedl)):
        if sortedl[i] in dic.keys():
            sortedl[i] = dic[sortedl[i]]
    return sortedl

#main

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
