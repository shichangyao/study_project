from classExample2 import Person

class Student(Person):

    def __init__(self,name,sex,province,grade):
        super(Student,self).__init__(name,sex,province)
        # Person.__init__(self,name,sex,province)
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return "我不告诉你student名字"

    def get_nick_name(self):
        name = Person.get_name(self)
        if name.startswith("xiao"):
            return "small_"+name
        else:
            return name

if __name__ == "__main__":
    student = Student('xiaozhengnan','男','陕西','大三')
    print(student.get_sex())
    print(student.get_grade())
    print(student.get_name())
    print(student.get_nick_name())