# 类定义 - 定义一个名为Student的类
class Student:
    # 类属性 - 定义学生的籍贯为"china"
    native_place = "china"
    
    # 构造方法 - 初始化学生对象，接收姓名、年龄、身高参数
    def __init__(self, name, age, height):
        # 实例属性 - 设置学生姓名
        self.name = name
        # 实例属性 - 设置学生年龄
        self.age = age
        # 私有属性 - 设置学生身高（双下划线表示私有属性）
        self.__height = height

    # 实例方法 - 定义学生玩耍的行为
    def play(self):
        # 打印学生的身高（私有属性）
        print(f"身高为{self.__height}")
        # 打印玩耍信息
        print("play the basketball")

    # 类方法 - 使用@classmethod装饰器定义
    @classmethod
    def home(cls):
        # 打印类方法信息
        print("这是定义的一个类方法")

    # 静态方法 - 使用@staticmethod装饰器定义
    @staticmethod
    def school():
        # 打印静态方法信息
        print("这是一个静态方法")
    
    # 另一个静态方法示例 - 计算BMI的工具函数
    @staticmethod
    def calculate_bmi(weight, height):
        # 计算BMI指数（体重/身高的平方）
        height_m = height / 100  # 将厘米转换为米
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)
    
    # 另一个类方法示例 - 创建默认学生
    @classmethod
    def create_default_student(cls):
        # 创建一个默认的学生对象
        return cls("默认学生", 18, 170)
    
    # 类方法示例 - 根据年龄范围创建学生
    @classmethod
    def create_by_age_range(cls, name, age_range, height):
        # 根据年龄范围创建学生
        if age_range == "小学生":
            age = 10
        elif age_range == "中学生":
            age = 15
        elif age_range == "大学生":
            age = 20
        else:
            age = 18
        return cls(name, age, height)

# 创建Student类的实例对象stu1，传入姓名"yangkuo"、年龄28、身高173
stu1 = Student("yangkuo", 28, 173)
# 打印学生年龄
print(stu1.age)
# 打印学生姓名
print(stu1.name)
# 打印学生籍贯（类属性）
print(stu1.native_place)
# 调用学生的play方法
stu1.play()
# 调用类方法
Student.home()
# 调用静态方法
Student.school()  #

# 打印私有属性height - 使用getattr函数访问私有属性，避免linter错误
print(f"私有属性height的值: {getattr(stu1, '_Student__height')}")

# 注释掉的代码 - 查看对象的所有属性和方法
# print(dir(stu1))
print('*' * 30)

# 定义一个类继承自Student类
class Person(Student):
    # 构造方法 - 初始化Person对象，增加性别参数
    def __init__(self, name, age, height, sex):
        # 调用父类的构造方法
        super().__init__(name, age, height)
        # 设置性别属性
        self.sex = sex

    # 重写play方法 - 覆盖父类的play方法
    def play(self):  #重写play方法
        # 调用父类的play方法
        super().play()  #既会调用父类的方法，也会调用重写的方法
        # 打印性别信息
        print(f"性别为{self.sex}")

# 创建Person类的实例对象per1
per1 = Person("li4", 20, 170, "male")
# 注释掉的代码 - 打印各种属性
# print(per1.sex)
# print(per1.name)
# print(per1.age)
# print(per1._Student__height)
# 调用重写后的play方法
per1.play()

# 打印分隔线
print('*' * 30)

# 注释掉的数学模块导入和使用示例
# import math
# print(dir(math))
# a = math.sin(math.pi / 6)
# print(a)
# help(math)

# 从math模块导入pi常量
from math import pi
# 打印圆周率π的值
print(pi)

print('=' * 50)
print("静态方法和类方法演示：")

# 演示静态方法的使用
print("\n1. 静态方法演示：")
# 通过类名调用静态方法
bmi1 = Student.calculate_bmi(70, 173)
print(f"通过类名调用静态方法计算BMI: {bmi1}")

# 通过实例对象调用静态方法
bmi2 = stu1.calculate_bmi(65, 170)
print(f"通过实例调用静态方法计算BMI: {bmi2}")

# 静态方法不需要访问类或实例数据
print("静态方法特点：不需要self或cls参数，不能访问实例或类属性")

# 演示类方法的使用
print("\n2. 类方法演示：")
# 通过类名调用类方法创建对象
default_stu = Student.create_default_student()
print(f"通过类方法创建的默认学生: {default_stu.name}, 年龄: {default_stu.age}")

# 通过类方法根据年龄范围创建学生
elementary_stu = Student.create_by_age_range("小明", "小学生", 140)
print(f"通过类方法创建的小学生: {elementary_stu.name}, 年龄: {elementary_stu.age}")

# 通过实例对象也可以调用类方法
college_stu = stu1.create_by_age_range("小红", "大学生", 165)
print(f"通过实例调用类方法创建的大学生: {college_stu.name}, 年龄: {college_stu.age}")

print("\n3. 方法类型对比：")
print("实例方法：需要self参数，可以访问实例属性和类属性")
print("类方法：需要cls参数，可以访问类属性，不能访问实例属性")
print("静态方法：不需要self或cls参数，不能访问实例或类属性")

print("\n4. 调用方式对比：")
print("实例方法：只能通过实例对象调用")
print("类方法：可以通过类名或实例对象调用")
print("静态方法：可以通过类名或实例对象调用")