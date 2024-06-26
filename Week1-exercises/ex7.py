# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

n1 = 1000
n2 = 3000

def is_odd(num):
    return num % 2 != 0

def all_digits(num):
    return [int(x) for x in str(num)]

def is_all_digit_even(num):
    arr = all_digits(num)
    i = 0
    res = True
    while i < len(arr):
        if is_odd(arr[i]):
            res = False
            break
        i+=1
    return res

def leverage_odd_digits(num):
    digits = all_digits(num)
    res = num
    for i, digit in enumerate(digits):
        if is_odd(digit):
            inc = 10**(len(digits) - 1 - i)
            res += inc
    return res

result = ""
while n1 <= n2:
    if is_all_digit_even(n1):
        result += str(n1) + ", "
        n1 += 2
    else:
        n1 = leverage_odd_digits(n1)

result = result[:-2]
print(result)

#RESULT:
#2000, 2002, 2004, 2006, 2008, 2020, 2022, 2024, 2026, 2028, 2040, 2042, 2044, 2046, 2048, 2060, 2062, 2064, 2066, 2068, 2080, 2082, 2084, 2086, 2088, 2200, 2202, 2204, 2206, 2208, 2220, 2222, 2224, 2226, 2228, 2240, 2242, 2244, 2246, 2248, 2260, 2262, 2264, 2266, 2268, 2280, 2282, 2284, 2286, 2288, 2400, 2402, 2404, 2406, 2408, 2420, 2422, 2424, 2426, 2428, 2440, 2442, 2444, 2446, 2448, 2460, 2462, 2464, 2466, 2468, 2480, 2482, 2484, 2486, 2488, 2600, 2602, 2604, 2606, 2608, 2620, 2622, 2624, 2626, 2628, 2640, 2642, 2644, 2646, 2648, 2660, 2662, 2664, 2666, 2668, 2680, 2682, 2684, 2686, 2688, 2800, 2802, 2804, 2806, 2808, 2820, 2822, 2824, 2826, 2828, 2840, 2842, 2844, 2846, 2848, 2860, 2862, 2864, 2866, 2868, 2880, 2882, 2884, 2886, 2888