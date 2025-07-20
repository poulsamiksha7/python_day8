##Q1 Function to add 2 numbers
# def add_num(a,b):
#    return a+b
 
# print("Sum",add_num(a=5,b=5))

##Q2 Prime checker using function
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# num = 31

# if is_prime(num):
#     print("The prime number is",num)
# else:
#     print("This is not prime number",num)

##Q3  Recursive factorial
# def factorial(n):
#     if n ==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# num=4

# print("The Factorial of",num, "is" ,factorial(num))
  
##Q4  Sum of digits (function)
# def sum_of_digits(n):
#     total=0
#     while n>0:
#         digit=n%10
#         total=total+digit
#         n=n//10

#     return total
    
# num=10
# print("The sum of numbers are", sum_of_digits(num))    

##Q5  Default arguments
# def make_tea(sugar='1 Teaspoon'):
#   print("Make tea with",sugar)

# make_tea()
# make_tea('2 teaspoon')

##Q6  Lambda function for square
# square= lambda l: l*l

# print("The square of ",square(2))

##Q7 Calculator using Functions
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     if b==0:
#         print("Cannot divide by zero!")
#     return a/b

# print("Select Operator")
# print("1.Add Numbers")
# print("2.Subtract Numbers")
# print("3.Multiply Numbers")
# print("4.Divide Number")  

# choice= input("Enter choice 1/2/3/4: ")

# num1=float(input("Enter first Number: "))
# num2=float(input("Enter first Number: "))

# if choice=='1':
#     print("The Addition of two numbers is: ",add(num1,num2))
# elif choice=='2':
#     print("The Subtraction of Numbers is: ", sub(num1,num2))
# elif choice=='3':
#     print("The Subtraction of Numbers is: ", mul(num1,num2))
# elif choice=='2':
#     print("The Subtraction of Numbers is: ", div(num1,num2))

# else:
#     print("Invalid Input!")
 ##Q8 Palindrome with function
# def is_palindrome(text):
#    text=str(text)
#    return text == text[::-1]

# value='madam'
# if is_palindrome(value):
#    print("The",value,"is Palindrome:",is_palindrome(value))
# else:
#    print("The",value,"is not Palindrome:",is_palindrome(value))

##Q9 Even/odd list filter
# def filter_even_odd(numbers):
#     even_no=[]
#     odd_no=[]
#     for num in numbers:
#         if num%2==0:
#              even_no.append(num)
#         else:
#              odd_no.append(num)
#     return even_no, odd_no

# lst=[1,21,2,32,1,3,2,2,35,5,3,4]

# even_num,odd_num=filter_even_odd(lst)

# print("The even number is:", even_num)
# print("The odd number is", odd_num)

##Q10  Function returning multiple values
def calc_mul_val(a,b):
    sum_result=a+b
    sub_result=a-b
    return sum_result, sub_result

x=7
y=5

s,sb=calc_mul_val(x,y)
print("The sum of numbers is: ", s)
print("The sub of numbers is: ",sb)

 

        

    

        

   

