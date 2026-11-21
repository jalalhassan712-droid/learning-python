
# ==========================================
# PYTHON OBJECT-ORIENTED PROGRAMMING (OOP)
# ==========================================


# 1. Classes and Objects

class Student:
    name = "Ali"
    age = 20

student1 = Student()

print("Name:", student1.name)
print("Age:", student1.age)


# 2. Constructor (__init__)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Ahmed", 21)

print("Name:", student1.name)
print("Age:", student1.age)


# 3. Instance Attributes

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Ali", 50000)
emp2 = Employee("Ahmed", 60000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)


# 4. Class Attributes

class University:
    university_name = "ABC University"

    def __init__(self, student):
        self.student = student

student1 = University("Ali")
student2 = University("Ahmed")

print(student1.university_name)
print(student2.university_name)


# 5. Instance Methods

class Car:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Car Brand:", self.brand)

car1 = Car("Toyota")
car1.display()


# 6. Class Methods

class Student:
    university = "ABC University"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_university(cls, new_name):
        cls.university = new_name

Student.change_university("XYZ University")

print(Student.university)


# 7. Static Methods

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

print("Addition:", Calculator.add(10, 20))


# 8. Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(10000)

account.deposit(5000)

print("Balance:", account.get_balance())


# 9. Public, Protected, and Private Attributes

class Person:
    def __init__(self):
        self.name = "Ali"          # Public
        self._age = 20             # Protected convention
        self.__salary = 50000      # Private name-mangled

person = Person()

print("Name:", person.name)
print("Age:", person._age)
print("Salary:", person._Person__salary)


# 10. Getters and Setters

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

emp = Employee(40000)

emp.set_salary(60000)

print("Salary:", emp.get_salary())


# 11. Single Inheritance

class Animal:
    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

dog = Dog()

dog.eat()
dog.bark()


# 12. Multiple Inheritance

class Father:
    def skills1(self):
        print("Father: Gardening")

class Mother:
    def skills2(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    pass

child = Child()

child.skills1()
child.skills2()


# 13. Multilevel Inheritance

class Grandfather:
    def house(self):
        print("Grandfather owns a house.")

class Father(Grandfather):
    def car(self):
        print("Father owns a car.")

class Son(Father):
    def bike(self):
        print("Son owns a bike.")

son = Son()

son.house()
son.car()
son.bike()


# 14. Hierarchical Inheritance

class Parent:
    def show(self):
        print("Parent class.")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()

obj1.show()
obj2.show()


# 15. super() Function

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

child = Child("Ali", 20)

print(child.name)
print(child.age)


# 16. Polymorphism

class Dog:
    def sound(self):
        print("Dog barks.")

class Cat:
    def sound(self):
        print("Cat meows.")

for animal in [Dog(), Cat()]:
    animal.sound()


# 17. Method Overriding

class Parent:
    def display(self):
        print("Parent method.")

class Child(Parent):
    def display(self):
        print("Child method.")

obj = Child()
obj.display()


# 18. Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(10, 5)

print("Rectangle Area:", rectangle.area())


# 19. Properties

class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value

student = Student(80)

student.marks = 95

print("Student Marks:", student.marks)


# 20. Magic (Dunder) Methods

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book Title: {self.title}"

    def __len__(self):
        return len(self.title)

book = Book("Python Programming")

print(book)
print("Title Length:", len(book))


# 21. Operator Overloading

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

num1 = Number(10)
num2 = Number(20)

print("Addition:", num1 + num2)


# ==========================================
# END OF PYTHON OOP
# ==========================================
