import time
from datetime import datetime
from functools import wraps


def work_time_count_perf_counter(func):
    @wraps(func)
    def work_time_count_perf_counter_wrapper(*args, **kwargs):
        start_time_perf = time.perf_counter()
        result_perf = func(*args, **kwargs)
        end_time_perf = time.perf_counter()
        total_time_perf = end_time_perf - start_time_perf
        print(f'Start time {start_time_perf:.1f}')
        print(f'End time {end_time_perf:.1f}')
        print(f'Total time {total_time_perf:.1f} seconds')
        return result_perf

    return work_time_count_perf_counter_wrapper


def work_time_count_datetime(func):
    @wraps(func)
    def work_time_count_datetime_wrapper(*args, **kwargs):
        start_time_datetime = datetime.now()
        result_datetime = func(*args, **kwargs)
        end_time_datetime = datetime.now()
        total_time_datetime = end_time_datetime - start_time_datetime
        print(f"Start time {start_time_datetime}")
        print(f"End time {end_time_datetime}")
        print(f"Total time {total_time_datetime}")
        return result_datetime

    return work_time_count_datetime_wrapper


def work_time_count_monotonic(func):
    @wraps(func)
    def work_time_count_monotonic_wrapper(*args, **kwargs):
        start_time_monotonic = time.monotonic()
        result_monotonic = func(*args, **kwargs)
        end_time_monotonic = time.monotonic()
        total_time_monotonic = end_time_monotonic - start_time_monotonic
        print(f"Start time {start_time_monotonic:.1f}")
        print(f"End time {end_time_monotonic:.1f}")
        print(f"Total time {total_time_monotonic:.1f}")
        return result_monotonic

    return work_time_count_monotonic_wrapper


@work_time_count_perf_counter
@work_time_count_datetime
@work_time_count_monotonic
def test_function(num: int):
    total = sum((x for x in range(0, num ** 3)))
    return total


test_function(1000)
