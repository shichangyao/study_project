from classExample4 import Student

class StudentGirl(Student):

    def __init__(self,name,sex,province,grade):
        super(StudentGirl,self).__init__(name,sex,province,grade)
        # Student.__init__(self,name,sex,province,grade)
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return "我不告诉你Girl名字"

    def overtime_sunday(self):
        if self.grade == 3:
            return u"补课"
        else:
            return u"不补课"

if __name__ == "__main__":
    sg = StudentGirl('huahua','female','shanghai',10)
    print(sg.get_name())
    print(sg.get_sex())
    print(sg.overtime_sunday())