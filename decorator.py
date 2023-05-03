import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Start time {start_time}')
        print(f'End time {end_time}')
        print(f'Total time {total_time:.2f} seconds')
        return result
    return timeit_wrapper

@timeit
def test_function(num: int):
    total = sum((x for x in range(0, num ** 3)))
    return total

test_function(1000)


