# 带参数的装饰器

# 装饰函数
def say_hello(contury):
    def wrapper(func):
        def deco(*args,**kwargs):
            if contury == "american":
                print("hello")
            elif contury == "chinese":
                print("你好")
            else:
                return
            func(*args,**kwargs)
        return deco
    return wrapper

@say_hello("american")
def american():
    print("i am from american")

@say_hello("chinese")
def chinese():
    print("我来自中国")

american()
chinese()