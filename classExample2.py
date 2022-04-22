
class Person(object):
    total_person = 0
    def __init__(self,name,sex,province):
        print("Init the class")
        self.name = name
        self.sex = sex
        self.province = province
        Person.total_person += 1

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

if __name__ == "__main__":
    person = Person('xiaozhang','male','beijing')
    print(person.sex)
    print(person.name)
    print(person.get_name())
    print(person.total_person)
    print("*"*20)
    person2 = Person('hanmeimei','female','shanghai')
    print(person2.sex)
    print(person2.name)
    print(person2.get_name())
    print(person2.total_person)