instances = {}


def singleton(cls):
    def get_instance(*args, **kwargs):
        cls_name = cls.__name__
        print("========1=========")
        if not cls_name in instances:
            print("========2=========")
            instance = cls(*args, **kwargs)
            instances[cls_name] = instance
        return instances[cls_name]

    return get_instance


@singleton
class User:
    _instance = None

    def __init__(self, name):
        print("========3=========")
        self.name = name

u1 = User("张三")
u1.age = 20
u2 = User('zhangsan')
u2.age
u1 is u2