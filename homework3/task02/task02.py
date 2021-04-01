import hashlib
import random
import struct
import time
from multiprocessing import Pool, cpu_count


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def parallel_calculation():
    values = [i for i in range(501)]

    start_time = time.time()

    with Pool(cpu_count() - 1) as pool:
        sum_ = pool.map(slow_calculate, values)

    print(time.time() - start_time)

    return sum(sum_)
