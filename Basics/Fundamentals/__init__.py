# if __name__ == '__main__':
#     n = int(input())
#     constr = ""
#     for i in range (1, n):
#         constr += str(i)
#     print(constr)

#Hacker Rank: deque
from collections import deque
def DequeExample():
    d = deque()
     
    n = int(input())
     
    for i in range(0, n):
        cmd = str(input())
        toks = list(cmd.split(" "))
        print("tokens", toks)
        if toks[0] == "append":
            d.extend(toks[1:])
        if toks[0] == "appendleft":
            d.extendleft(toks[1:])
        if toks[0] == "pop":
            d.pop()
        if toks[0] == "popleft":
            d.popleft()
    output = ""
    for j in d:
        output = output + j + " "
    print(output)

#DequeExample()

#factorial
def factorial(n):
    #base case
    if(n == 0):
        return 1
    
    return n * factorial(n-1)

# print ("5! = " + str(factorial(5)))

def find_nth_fib_num(n):
    #base case
    if (n == 0) or (n == 1):
        return 1
    
    return find_nth_fib_num(n-1) + find_nth_fib_num(n-2)

             
#print("Fibonacci Sum of 30 = " + str(find_nth_fib_num(30)))

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        val = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = val
        return val

d = {1:1, 2:2}
# print("fib of 30 = " + str(fib_efficient(30, d)))

def is_palindrome(s):
    
    def to_chars(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans += c
        return ans
    
    def is_pal(s):
        if len(s) <= 1:
            return True
        return (s[0] == s[-1]) and is_pal(s[1:-1])
    
    return is_pal(to_chars(s))
    
# print (is_palindrome("MaM"))
# print (is_palindrome("hi"))

def print_hanoi_tower_shift(fr, to):
    print(str(fr), str(to))
    
def towers_of_hanoi(n, fr, to, spare):
    if n == 1:
        print_hanoi_tower_shift(fr, to)
        return
        
    towers_of_hanoi(n-1, fr, spare, to)
    towers_of_hanoi(1, fr, to, spare)
    towers_of_hanoi(n-1, spare, to, fr)
    
# towers_of_hanoi(3, "fr", "to", "spare")

# Permute using extra space
def permute(s):

    chars = list(s)
    
    if(len(s) == 1):
        return chars
    
    permutedList = []
    for index in range(0, len(s)):
        pivotIndex = index
        pivotChar = chars[pivotIndex]
        restPermutedWords = permute(s[0:pivotIndex] + s[pivotIndex+1:])
        permutedList += list(pivotChar + permutedWord for permutedWord in restPermutedWords)
        
    return permutedList 

# permuteList = permute("cats")
# for word in permuteList:
#     print(word)


#Permute in place. Use the swap logic and write a function

#Check if sorted

from math import floor
def IsSortedInAscending(inputArr):
#     print(str(inputArr) + " Length = " + str(len(inputArr)))
    if(len(inputArr) == 2):
        return inputArr[0] <= inputArr[1]
    isRestSorted = IsSortedInAscending(inputArr[:-1])
    return isRestSorted and (inputArr[-2] <= inputArr[-1])

#DONT DELETE this driver input. This is a beautiful test case: End result as per
# the above logic is True. But actually it is false. Because the recursive function
# decides 40<80 and 70<80 and together they are in sorted order, while it is not.
print(IsSortedInAscending([10, 20, 30, 40, 70, 80]))
print(IsSortedInAscending([10, 20, 30, 40, 80, 70]))
print(IsSortedInAscending([10, 20, 30, 40, 60, 70, 80]))
print(IsSortedInAscending([10, 20, 30, 40, 80, 70, 80]))


#HackerRank: Cube Stacking in big to small order

def IsStackableRecursiveNotWorking(cubes):
    print(cubes)
    if(len(cubes) == 1):
        return (True, cubes[0])
    if(len(cubes) == 2):
        biggerCubeSize = cubes[0] if (cubes[0] >= cubes[1]) else cubes[1]  
        return (True, biggerCubeSize)
    
    restStackable, restBigCubeSize = IsStackableRecursiveNotWorking(cubes[1:-1])
    curBiggerCubeSize = cubes[0] if (cubes[0] >= cubes[-1]) else cubes[-1]  
    return (((cubes[0] >= restBigCubeSize) and (cubes[-1] >= restBigCubeSize) and restStackable), curBiggerCubeSize)

def IsStackableNonRecursive(cubes):
    if len(cubes) == 0:
        return False
    if len(cubes) == 1:
        return True

    headIdx = 0
    tailIdx = len(cubes)-1
    stackTop = cubes[headIdx] if cubes[headIdx] >= cubes[tailIdx] else cubes[tailIdx]
    nextCandidate = stackTop
    
    while (headIdx != tailIdx) and (nextCandidate <= stackTop):
#         print("HeadIdx {}, Head {}, TailIdx {}, Tail {}".format(headIdx,cubes[headIdx],tailIdx,cubes[tailIdx]))
        if cubes[headIdx] >= cubes[tailIdx]:
            stackTop = cubes[headIdx]
            headIdx += 1
        else:
            stackTop = cubes[tailIdx]
            tailIdx -= 1
        nextCandidate = cubes[headIdx] if cubes[headIdx] >= cubes[tailIdx] else cubes[tailIdx]
        
    
    stackable = True if headIdx == tailIdx else False
    return stackable

def IsStackableHackerRankSolution(cubes):
    l = len(cubes)
    i = 0
    while i<l-1 and cubes[i]>=cubes[i+1]:
        i += 1
    
    while i<l-1 and cubes[i]<=cubes[i+1]:
        i += 1
        
    stackable = True if i == l-1 else False
    return stackable
    
        
def FindIsCubesStackable():
    n = int(input())
    cubeCount = []
    cubes = []
#     print(range(n))
    for i in range(n):
        cubeCount.append(int(input())) 
        cubes.append(list(str(input()).split(" ")))

    for i in range(n):
        print(cubes[i])
#         isStackable, biggestNum = IsStackableRecursiveNotWorking(cubes[i])
        isStackable = IsStackableNonRecursive(cubes[i])
        if isStackable == True:
            print("Yes")
        else:
            print("No")

#FindIsCubesStackable()        
        

# print(IsStackableNonRecursive([4,3,2,1,3,5]))
# print(IsStackableNonRecursive([4,3,2,1,3,4]))
# print(IsStackableNonRecursive([1,3,2]))
# print(IsStackableNonRecursive([4,4,2,2,3,5,6]))
# print(IsStackableHackerRankSolution([1]))
# print(IsStackableHackerRankSolution([]))
print(IsStackableHackerRankSolution([0,1,2,4,3,4]))




# Reverse words:
# Input: "I Love Programming"
# Output: "Programming Love I"
def reverseWords(input):
    words = list(input.split(' '))
    return words[::-1]

print(' '.join(reverseWords("I Love Programming")))


# Example program to parse a CSV File and update entries
# 1. Create an Students CSV File with the path and name specified
#        Row contains: StudentID, StudentName, Age, Sex, Father Name, Father Mobile Number
# 2. Print all CSV file contents
# 3. Append a Row(Key: Student ID)
# 4. Delete a Row(Key: Student ID)
# 5. Modify a Row

class Person:
    
    def __init__(self, name, DOB, age, sex, fatherName, motherName):
        self.details = dict({'name':name, 'DOB':DOB, 'age':age, 
                             'sex':sex, 'fatherName':fatherName, 
                             'motherName':motherName})
        
    def __str__(self):
        return self.details["name"] + "," + self.details["DOB"] + "," + str(self.details["age"]) + "," + self.details["sex"] + "," + self.details["fatherName"] + "," + self.details["motherName"]
    
class Student(Person):
    def __init__(self, studentID, name, DOB, age, sex, fatherName, motherName):
        super().__init__(name, DOB, age, sex, fatherName, motherName)
        self.details['studentID'] = studentID
        
        
    def __str__(self):
        return str(self.details['studentID']) + "," + super().__str__() 
        
#me = Person("", Premkumar Jayakumar", "22Feb1979", "38", "M", "Jayakumar Alagamalai", "Mallika Pichaimuthu")
me = Student(421, "Premkumar Jayakumar", "02/22/1979", 38, "M", "Jayakumar Alagamalai", "Mallika Pichaimuthu")
print(str(me))
print(str(me.details['studentID']))

import os
def oswalk(srcdir):
    for child in os.listdir(srcdir):
        childFullPath = os.path.join(srcdir, child)
        if os.path.isdir(childFullPath):
            oswalk(childFullPath)
        # To print only files and not directories, print only in the else case
        #else:
        print(childFullPath)
            
oswalk("G:\Songs")

def list_op():
    resList = []
    n = int(input())
    cmdLists = []
    for i in range(0,n):
        cmdList = list(x for x in input().split())
        cmdLists.append(cmdList)
    
    for i in range(0,n):
        cmdTokens = cmdLists[i]
        if cmdTokens[0] == "insert":
            resList.insert(int(cmdTokens[1]), int(cmdTokens[2]))
        elif cmdTokens[0] == "print":
            print(resList)
        elif cmdTokens[0] == "remove":
            resList.remove(int(cmdTokens[1]))
        elif cmdTokens[0] == "append":
            resList.append(int(cmdTokens[1]))
        elif cmdTokens[0] == "sort":
            resList.sort()
        elif cmdTokens[0] == "pop":
            resList.pop()
        elif cmdTokens[0] == "reverse":
            resList.reverse()
        else:
            print("Unknown Command: " + cmdTokens[0])
            

#list_op()

def chk_hash():
    print("Check Hash")
    n = int(input())
    # map syntax: map(aFunction, aSequence)
    # map basically applies the function for all the items in the sequence and returns a list
    # aSequence is basically an iterable like list
    # In this example, input().split() will return a list of "strings". The map function
    # applies the int() function on all these strings to convert them to int.
    integer_list = map(int, input().split())
    print(integer_list)
    print(tuple(integer_list))
    print(hash(tuple(integer_list)))
#chk_hash()


####################
##### MAX HEAP #####
####################
heap = []
def getParentIdx(childIdx):
    return int(((childIdx-1) / 2))
def getLeftChildIdx(parentIdx):
    return int(((parentIdx*2) + 1))
def getRightChildIdx(parentIdx):
    return int(((parentIdx*2) + 2))
nextFreeIdx = 0
lastOccupiedIdx = 0
def swap(idx1, idx2):
    temp = heap[idx1]
    heap[idx1] = heap[idx2]
    heap[idx2] = temp
def heapifyUp(curIdx):
    global lastOccupiedIdx
    global nextFreeIdx
    while curIdx > 0:
        if heap[curIdx] > heap[getParentIdx(curIdx)]:
            swap(curIdx, getParentIdx(curIdx))
            curIdx = getParentIdx(curIdx)
        else:
            break
def heapifyDown(curIdx):
    global lastOccupiedIdx
    global nextFreeIdx
    while curIdx < lastOccupiedIdx:
        leftChildIdx = getLeftChildIdx(curIdx)
        rightChildIdx = getRightChildIdx(curIdx)
        if leftChildIdx < len(heap) and heap[curIdx] < heap[leftChildIdx]:
            swap(curIdx, leftChildIdx)
            curIdx = getLeftChildIdx(curIdx)
        elif rightChildIdx < len(heap) and heap[curIdx] < heap[rightChildIdx]:
            swap(curIdx, rightChildIdx)
            curIdx = getRightChildIdx(curIdx)
        else:
            break
def insertVal(val):
    global lastOccupiedIdx
    global nextFreeIdx
    heap.append(val)
    lastOccupiedIdx = nextFreeIdx
    nextFreeIdx += 1
    heapifyUp(lastOccupiedIdx)
def getMaxVal():
    global lastOccupiedIdx
    global nextFreeIdx
    maxVal = heap[0]
    heap[0] = heap[lastOccupiedIdx]
    del heap[-1]
    heapifyDown(0)
    nextFreeIdx -= 1
    lastOccupiedIdx -= 1
    return maxVal
def getRunnerUp(arr):
    #Instead of getting input each time, modified function to receive input.
    #N = int(input())
    #arr = list(int(x) for x in input().split())
    for i in range(len(arr)):
        insertVal(arr[i])
    winner = getMaxVal()
    runnerUp = getMaxVal()
    while runnerUp == winner:
        runnerUp = getMaxVal()
    print ("RunnerUp is " + str(runnerUp))
getRunnerUp([20,60,90,10]) #Gives wrong result. Need to debug
getRunnerUp([100,90,80,70])
getRunnerUp([30,50,70,90])