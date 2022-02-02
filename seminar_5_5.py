from sys import getsizeof
import time
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
start_time = time.time()
result_2 = [i for i in src if src.count(i) == 1]
print(result_2)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
result_3 = {i for i in src if src.count(i) == 1}
print("--- %s seconds ---" % (time.time() - start_time))
print(result_3)
print(getsizeof(result_2))
print(getsizeof(result_3))
print(type(result_2))
print(type(result_3))