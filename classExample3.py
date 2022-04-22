class Person:

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def set_purson_attribute(self,sex,province):
        self.sex = sex
        self.province = province

    def get_sex(self):
        return self.sex

if __name__ == "__main__":
    per1 = Person()
    per1.set_name("hanmeimei")
    print(per1.get_name())
    per1.set_purson_attribute("Female","shanghai")
    print(per1.get_sex())

   