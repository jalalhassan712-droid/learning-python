class students:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def display(self):
        sum=0
        for i in self.marks:
            sum+=i
        print(f"hi {self.name} your average score is {sum/3}")


s1=students("jalal ", [98, 85, 88])
print(s1.name)
print(s1.marks)
s1.display()