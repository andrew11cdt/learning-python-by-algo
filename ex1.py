# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

pos = 0
neg = 0
for num in data1:
    if num < 0:
        neg += 1
    else:
        pos += 1
print(f"positive numbers: {pos}, negative numbers: {neg}")

#RESULT: positive numbers: 5, negative numbers: 7