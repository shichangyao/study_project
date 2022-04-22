# 装饰器用于日志打印
import functools

# 这是装饰函数
def logger(func):
    @functools.wraps(func)
    def new_wrapper(*args,**kwargs):
        print(f"准备执行{func.__name__}函数")
        func(*args,**kwargs)
        print(f"{func.__name__}函数执行完毕")
    return new_wrapper

@logger
def add(x,y):
    print("add函数正在执行")
    print(f'{x}+{y}的结果为{x+y}')

add(3,4)