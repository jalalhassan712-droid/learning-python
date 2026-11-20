#Type of type casting 

#1. Explicit typecasting :-
"""The conversion of one data type into another data type done 
via developer or programmers intervation or manually as per the 
requirement in known as explicit type casting   """
#Example 
string= "15"
number= 5
string_number= int(string)
sum= number +string_number
print("The sum of both number is :", sum)
# Output 
#The sum of both number is : 20

#------------------------------------------------------------------------
#2. Implicit type casting 
"""When python automatically converts one data to another data type 
during an operation without the programmer needing to do it manually """
#Example
a= 7
b= 3.0
c = a +b
print("The sum of a and b is : ",c)
print("The data type of a :",type(a))
print("The data type of b :",type(b))
print("The data type of c :",type(c))
# Output 
#The sum of a and b is :  10.0
#The data type of a : <class 'int'>
#The data type of b : <class 'float'>
#The data type of c : <class 'float'>

