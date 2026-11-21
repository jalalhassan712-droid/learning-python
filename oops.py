class employee:
    def __init__(self, role, salary,dep):
        self.role = role
        self.salary = salary  
        self.dep = dep
    def show(self):
        
        print("Role:", self.role)
        print("Salary:", self.salary)
        print("Department:", self.dep)
class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
em1= employee("manager", 5776, "cs")
em1= engineer("john", 25)
em1.show()