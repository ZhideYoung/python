"""
定义一个学生类，用来形容学生
"""
#定义一个空的类
class Student():
    #一个空的类，pass表示直接跳过
    #此处pass必须有
    pass

#定义一个对象
zhangdan = Student()

#在定义一个类，用来描述python的学生

class PythonStudent():
    #用None给不确定的值复制啊
    name = None
    age = 18
    course = "python"

    #需要注意的是
    # 1.def dohomework的缩进层级
    # 2.系统默认由一个self参数

    def doHomework(self):

        print("I 在做作业")
        #推荐在末尾使用return语句

        return None
#实例化一个叫dandan的人，是一个具体的人
dandan = PythonStudent()
print(dandan.name)
print(dandan.age)
#注意成员函数的调用没有传递进参数
dandan.doHomework()