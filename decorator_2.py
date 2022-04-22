# 装饰器用于时间计时器

import time
import functools

# 这是装饰函数
def main_doing(func):
    @functools.wraps(func)
    def jisuan(*args,**kwargs):
        time_start = time.time()
        func(*args,**kwargs)
        time_end = time.time()
        print(f"执行函数{func.__name__}花费时间为：{time_end-time_start}")
    return jisuan

@main_doing
def wait_time(sleep_time):
    time.sleep(sleep_time)

wait_time(3)