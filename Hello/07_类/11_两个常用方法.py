# 定义一个person类
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
#定义一个Person类的子类Student类
class Student(Person):
    def __init__(self, name, age, gender,stu_id,grade):
        super().__init__(name, age, gender)
        self.stu_id = stu_id
        self.grade = grade
p1 = Person('Tree',18,'男')
s1 = Student('Like',19,'男',48,'二')

#方法一:isinstance(instance,class)判断某个对象是否为指定类或其子类的实例
print(isinstance(p1,Person))
print(isinstance(s1,Person))
#方法二：issubclass(subclass,class)判断某个类是否为指定类的子类
print(issubclass(Student,Person))
print(issubclass(Person,Student))
