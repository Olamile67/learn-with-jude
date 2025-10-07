#create a dictionary for a car
print("\n Create a  Car dictionary")
print("-"*30)

car = {
  "brand":"Toyota",
  "model":"Camry",
  "year":2020,
  "color":"blue"
 }
#Access and modify
print("\n Tasks: \n -print the car brand \n-change the color to red \n-Add milage to 15000" )
#Task 1
print(f"\ncar: {car}")

#Task 2 printing the car brand
print(f"\n Car brand: {car['brand']}")

#Task 3: chnage the color to red
car["color"]="red"
print(f"\nNew color:{car['color']}")

#Task 4: Add milage 
car["Milage"] = 15000
print(f"\nUpdated car attribute: {car}")

#Exercise 2 Dictionary method
print("\n Exercise 2: Dictionary method")
print("-"*40)
print("\n TASKS: \n 1. Get all keys \n2. Get all Values \n3. Check if age exists \n4. Get 'phone' with default 'Not provide'")
student = {
    "name":"Olalekan",
    "age": 19,
    "course": "pyhton", 
}
#Task 1 getting the keys only
print(f"\nGetting all keys:{student.keys()}")

#Task 2 Getting all values
print(f"\nGetting all values:{student.values()}")

#Task 3 check if age exist
if "age" in student:
    print(f"\n AGE:{student['age']}")

#Task 4 et 'phone' with default 'Not provide
if "phone" in student:
    print(f"phone:{student['phone']}")
else:
    print(f"Not Provided")

#Exercise 3 building a food menu
print("\n Exercise 3: Building a food menu")
print("-"*50)
print("\nTask: Add 3 items with prices ")

#Creating the menu
food_menu = {}

#Adding items
food_menu["rice"]= 1200
food_menu["beans"]=1000
food_menu["yam"]= 1500
print(f"Updated food_menu: {food_menu}")

#Simple Calculator
print("\nExercise 5: Simple calculator using lambda")
print("-"*50)
operations = {
    "add": lambda x,y: x+y,
    "subtract": lambda x,y: x-y,
    "multiply": lambda x,y: x*y,
}
print("\nTasks: Try each operation on [5,3]")
print()
print(f"Addition: {operations['add'](5,3)}")
print(f"subtration: {operations['subtract'](5,3)}")
print(f"Multiply: {operations['multiply'](5,3)}")

#Exercise 6 word counter
print("\nExercise 6: Word Counter")
print("-"*50)
text = "Python is great Python is fun"
word_count = {}
for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)