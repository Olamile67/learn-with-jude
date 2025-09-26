#A Prpgram to introduce myself
print("A PROGRAM ABOUT MYSELF")
print("="*50)
print()
name = input("What is your name? ")
age = input("How old are you? ")
hobby = input("What did you like doing? ")
state = input("Where are you from? ")
message = "HELLO! "+ name + " from "+ state + " it is nice meeting you, you are "+ age + " years old, your hobby is "+ hobby + "." 
print(message)

#A program to ask user three question and store thier answer
print("\n" "program to ask user three question" )
print("="*50)
name = input("What is your name? ")
school = input("Which school do you attend? ")
department = input("What is your Discipline? ")
print("your name is " + name)
print( "your discipline is " , department)
print("you are schooling at " , school)
print()

#A simple Arithmetic calculator 
print("A simple arithmetic Calculator ")
print("="*50)
print()
operator = input("Which operation would you like to perform( + , -, *, /.)? ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "ERROER!!: Division by zero!"
else:
    result = "invalid operator!"
print("Result: ", result)