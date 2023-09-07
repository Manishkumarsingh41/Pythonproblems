'''Write a function named DivExp which takes TWO parameters a, b and returns a value c c=a/b).
Write suitable assertion for a greater than 0 in function DivExp and raise an exception for when
b=0. Develop a suitable program which reads two values from the console and calls a function
DivExp.'''


# import sys
# def DivExp(a,b):
#     assert a>0, "a should be greater than 0"
#     try:
#         c = a/b
#     except ZeroDivisionError:
#         print("Value of b cannot be zero")
#         sys.exit(0)
#     else:
#         return c
# val1 = int(input("Enter a value for a : "))
# val2 = int(input("Enter a value for b : "))
# val3 = DivExp(val1, val2)
# print(val1, "/", val2, "=", val3)


#==========================================================================================

'''   Develop a program to sort the contents of a text file and write the sorted contents into a separate text
 file. [Hint: Use string methods strip(), len(), list methods sort(), append(), and file methods open(),
readlines(), and write()'''
  
# import os.path
# import sys

# fname = input("Enter the filename whose contents are to be sorted: ")

# if not os.path.isfile(fname):
#     print("File", fname, "doesn't exist")
#     sys.exit(0)

# infile = open(fname, "r")
# myList = infile.readlines()
# print(myList)

# # Remove trailing \n characters
# lineList = []
# for line in myList:
#     lineList.append(line.strip())

# lineList.sort()

# outfile = open("sorted.txt", "w")
# for line in lineList:
#     outfile.write(line + "\n")

# infile.close()  # Close the input file
# outfile.close()  # Close the output file

# if os.path.isfile("sorted.txt"):
#     print("\nFile containing sorted content sorted.txt created successfully")
    
# print("sorted.txt contains", len(lineList), "lines")
# print("Contents of sorted.txt")
# print("=====================")

# rdFile = open("sorted.txt", "r")
# for line in rdFile:
#     print(line, end="")


#=============================================================================================
'''  Develop a program to print 10 most frequently appearing words in a text file. [Hint: Use
dictionary with distinct words and their frequency of occurrences. Sort the dictionary in the
reverse order of frequency and display dictionary slice of first 10 items.'''

# import sys
# import string
# import os.path

# fname = input("Enter the filename: ")

# # Sample file text.txt also provided
# if not os.path.isfile(fname):
#     print("File", fname, "doesn't exist")
#     sys.exit(0)

# infile = open(fname, "r")
# filecontents = ""

# for line in infile:
#     for ch in line:
#         if ch not in string.punctuation:
#             filecontents = filecontents + ch
#         else:
#             filecontents = filecontents + ' '

# # Replace punctuations and \n with space
# wordFreq = {}
# wordList = filecontents.split()

# # Calculate word frequency
# for word in wordList:
#     if word not in wordFreq.keys():
#         wordFreq[word] = 1
#     else:
#         wordFreq[word] += 1

# # Sort dictionary based on values in descending order
# sortedWordFreq = sorted(wordFreq.items(), key=lambda x: x[1], reverse=True)

# for i in range(10):
#     print(sortedWordFreq[i][0], "occurs", sortedWordFreq[i][1], "times")

# sortedWordFreq = sorted(wordFreq.items(), key=lambda x: x[1], reverse=True)


#=========================================================================================

'''3. Read N numbers from the console and create a list. Develop a program to print mean, variance
and standard deviation with suitable messages.'''

from math import sqrt

myList = []
num = int(input("Enter the number of elements in your list: "))

for i in range(num):
    val = int(input("Enter the element: "))
    myList.append(val)

print('The length of list1 is', len(myList))
print('List Contents:', myList)

total = 0
for elem in myList:
    total += elem

mean = total / num

total = 0
for elem in myList:
    total += (elem - mean) * (elem - mean)

variance = total / num
stdDev = sqrt(variance)

print("Mean =", mean)
print("Variance =", variance)
print("Standard Deviation =", "%.2f" % stdDev)
