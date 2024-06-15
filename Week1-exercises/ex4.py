# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]

result = []
n = len(data4)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i!=j and j!=k and k!=i:
                result.append([data4[i], data4[j], data4[k]])

res_str = "\n".join(map(str, result))
print(f"All combinations are:\n{res_str}")

#RESULT:
#[1, 2, 3]
#[1, 3, 2]
#[2, 1, 3]
#[2, 3, 1]
#[3, 1, 2]
#[3, 2, 1]