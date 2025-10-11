#SIMPLE LIST ITERATION WITH ACTION
fruits = ["apple", "banana", "orange", "grape"]

for fruit in fruits:
    print(f"I love {fruit}")

#The range function
for number in range(10):
    print (f"count: {number}")
for i in range (1, 6):
    print(f"Number {i}")
#Range with step
for i in range(0, 10, 2):
    print(f"Even number: {i}")

#Loops with condition 
numbers = [1,2,3,4,5,6,7,8,9]
print(f"Original numbers: {numbers}")

for num in numbers:
    if num % 2 == 0:
        print(f"Even: {num}")
    else:
        print(f"odd: {num}")