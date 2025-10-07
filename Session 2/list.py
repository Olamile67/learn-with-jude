#List of favourite color
favourite_color = ["Red", "Orange", "Yellow", "Green", "Indigo", "Violet"]
print(f"My favourite colors are {favourite_color}")

#Printing the first color
first_color = favourite_color[0]
print(f"my favourite color is {first_color}")

#Adding new color
favourite_color.append("white")
print(f"After adding new color,  my new color list are {favourite_color}")

#create a list called movies
print("\n🔥 EXERCISE 1: Create Your Lists")
print("-"*30)
movies = ["Under the dome", "game of throne", "Spartacus", "Allegiant"]
numbers = [1,2,3,4,5]
my_list = []
print(f"List of my movies: {movies}")
print(f"list of numbers {numbers}")
print(f"empty list")

print("\n Accessing list items")
print("-"*30)
fruit = ["apple", "Banana", "cherry", "Date", "Elderberry"]
print(f"fruits = {fruit}")
print(f"the first fruit is {fruit[0]}")
print(f"the last fruit is {fruit[-1]}")
print(f"the middle fruit is {fruit[2]}")
print(f"the second and third fruit is {fruit[1:3]}")

print("\n Adding items to list")
print("-"*40)
colors = ["red", "blue"]
print(colors)
colors.insert(2, "grey")
print(f"color list after adding grey{colors}")
colors.append("ash")
print(f"color list after adding ash {colors}")
more_colors = ["violet", "Magenta"]
colors.extend(more_colors)
print(f"new color list{colors}")

# EXERCISE 7: List Math
print("\n Exercise 7: ,ath with Lists")
print("-"*30)
print("Given the list of test score:")
scores = [78, 85,92, 56, 24, 36] 
print(f"scores = {scores}")
print("\n Tasks:")

#finding the highest score
print("1.find the highest score")
highest_score = max(scores)
print(f"Highest score is {highest_score}")
print()

#Finding the lowet score
print("2. Find the lowest score")
lowest_score = min(scores)
print(f"Lowest score is {lowest_score}")
print()

#calculating the total average of the score
print("3. find the total average of the score")
Total_average = sum(scores) / len(scores)
print(f"The total average of the scores is {Total_average}")
print()

#Calculating the total of all scores
print("calucalte the total od all scores")
total_score = sum(scores)
print(f"The total is {total_score}")

#list sorting
print("\n\n🔥 EXERCISE 8: Sorting Lists")
print("-" * 30)
print("Given this list:")
names = ["Charlie", "Alice", "Bob", "Diana"]
print(f"names = {names}")
print("\nTasks:")

#sorting list alphabetically
print("1. Sort the list alphabetically")
names.sort()
print(f"sorted list are {names}")
print()

#Reversing the list
print("2. Reversing a list")
names.reverse()
print(f"Reversed list are {names}")
print()

#Challenge exercise
print("\n\n CHALLEMGE EXERCISE: Advanced Shoping List")
print("="*45)
print("WELCOME TO YOUR SHOPPING LIST, WHICH OPERATION WOULD YOU LIKE TO PERFORM?")
shopping_list = [ "apple", "Bread", "milk"]

def display_menu():
    print("\n SHOPPING LIST MENU:")
    print("1.View shopping list")
    print("2.Add item in shopping list")
    print("3.Remove item in shopping list")
    print("4. verify item shopping list")
    print("5.check total item shopping list")
    print("6.sort and list alphabetically")
    print("7.items with thier position")
    print("8.EXIT")
    print("*"*30)

def view_list():
    #checking if the list is empty
    if not shopping_list:
        print("your list is empty!, time to add some item")
    else:
        for i, item in enumerate(shopping_list, 1): #starting counting from 1
            print(f" {i}. {item}")
    print(f"total items: {len(shopping_list)}")

def add_item():
    item = input("\n Enter item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"Added {item} to your list")
    else:
        print("cannot add empty item!")

while True:
    display_menu()
    choice = input("Enter your choice (1-7)").strip()
    if choice == "1":
        view_list()
    elif choice == "2":
        add_item()

