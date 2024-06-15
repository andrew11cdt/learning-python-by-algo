# Ex1: Write a NumPy program to reverse an array (first element becomes last).
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]

# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]

# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...

import numpy as np
import re
print("\n#-----------ex1-----------------\n")
input_1 = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
reversed_array = np.array(input_1)[::-1]
print("Ex1:\n reverse array: \n", input_1)
print("ex1_answer: \n", reversed_array)

print("\n")

print("\n#-----------ex2-----------------\n")
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([10, 30, 40])

ex2_result = np.isin(array1, array2)



print(f"Ex2: \n array1={array1} \n array2={array2}")
print("check each element of array1 in array2:", ex2_result)

print("\n#-----------ex3-----------------\n")

arr3 = [1,6,4,8,9,-4,-2,11]
print("Ex3: ", arr3)
print("max:", np.max(arr3))
print("min:", np.min(arr3))

print("\n#-----------ex4-----------------\n")

def count_freq(array):
    freq = dict()
    res = []
    for num in array:
        if num in freq:
            freq[num] += 1
            if num not in res:
                res.append(num)
        else:
            freq[num] = 1
    return freq

with open('story.txt', 'r') as file:
    words = re.findall(r'\b\w{2,}|[aiAI]\b', file.read())
    lowercase_words = [w.lower() for w in words]
    word_freq = count_freq(lowercase_words)
    sorted_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    result = dict(list(sorted_freq.items())[:100])
    # print(lowercase_words)
    # print(sorted_freq.items())
    print("First 100 words occur most:\n")
    for k,v in result.items():
       print(f"{k}: {v}")

