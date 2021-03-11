import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def main():
    values = [i for i in range(501)]

    with Pool() as pool:
        sum_ = pool.map(slow_calculate, values)

    return sum(sum_)


# if __name__ == '__main__':
# #     start = timer()
# #
# #     print(f'starting computations on {cpu_count()} cores')
# #     values = [i for i in range(501)]
# #
# #     with Pool() as pool:
# #         sum_ = pool.map(slow_calculate, values)
# #
# #     end = timer()
# #     print(f'elapsed time: {end - start}')
# #     print(sum(sum_))
# # # 1025932
#     main()
