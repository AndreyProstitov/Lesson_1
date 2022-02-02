from sys import getsizeof

odd_to_15 = int(input())

result = [n for n in range(1, odd_to_15 + 1, 2)]

print(result, getsizeof(result))
