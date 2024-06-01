# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]

result = []
i = 0
while i < (len(data3) - 1):
    result.append(max(data3[i], data3[i+1]))
    i += 1
print(f"{data3} has the result: \n {result}")

#RESULT: [5, 6, 7, 7, 9, 11, 11, 10]