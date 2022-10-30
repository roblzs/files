import math
import random
import time

s_time = time.time()

arr_2D = [[x for x in range(1, random.randint(2, 20)) if x % 2 == 0] for _ in range(9999999)]

e_time = time.time()

total_time = e_time - s_time

print(f"Code took {math.floor(total_time)} seconds to execute")