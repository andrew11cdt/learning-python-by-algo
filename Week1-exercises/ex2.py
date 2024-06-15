# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

def find_element(data):
    freq = dict()
    res = []
    for num in data:
        if num in freq:
            freq[num] += 1
            res.append(num) if (freq[num] > k and num not in res) else None
        else:
            freq[num] = 1
    print(f"All element that has frequency greater than {k} is {res}")

find_element(data2)

#RESULT: All element that has frequency greater than 3 is [4, 3]