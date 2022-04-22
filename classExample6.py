class Person:

    total_person = 0
    def __init__(self,name,sex,province):
        print("Init the class")
        self.name = name
        self.sex = sex
        self.province = province
        Person.total_person += 1

    @staticmethod
    def set_new_name(new_name):
        return "new_name is:" + new_name

    @property
    def get_sex(self):
        return self.sex

    def get_name(self):
        return self.name

    @classmethod
    def set_new_province(cls,new_province):
        return "your province is:" + new_province

if __name__ == "__main__":
    print(Person.set_new_name("hanmeimei"))
    print(Person("shichangyao","male","sahnxi").get_name())
    print(Person("shichangyao","male","sahnxi").get_sex)