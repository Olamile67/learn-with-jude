# EXERCISE 1: Temperature Converter and Advisor
print("\nExercise 1: Temperature Advisor")
print("-"*50)
print("\nTasks: Create a program that; \n1. Takes a temperature in farenheit \n2. Convert it to celsius \n3. Gives clothing advise base on temperature")
print("\nTemperature ranges:")
print("• Above 80°F: Hot - wear light clothes")
print("• 60-80°F: Warm - comfortable clothes")
print("• 40-60°F: Cool - bring a jacket")
print("• Below 40°F: Cold - bundle up!")
def temperature_advisor():
    temperature = float(input("What is th temperature degree? "))
    conversionToCelsius = (temperature - 32) * 5/9
    print(f"Temperature: {temperature}°F ({conversionToCelsius:.1f}°C)")
    if temperature >= 80:
        print("Hot - wear light cloth")
    elif temperature >= 60 :
        print("Warm - comfortable clothes")
    elif temperature >= 40:
        print("Cool - bring a jacket")
    else:
        print("Cold - bundle up!")
temperature_advisor()

# EXERCISE 2: BMI Calculator with Categories
print("\n" + "="*50)
print("EXERCISE 2: BMI CALCULATOR")
print("="*50)

print("Create a BMI calculator that:")
print("1. Takes weight (kg) and height (m)")
print("2. Calculates BMI = weight / (height^2)")
print("3. Categorizes the result")

print("\nBMI Categories:")
print("• Below 18.5: Underweight")
print("• 18.5-24.9: Normal weight")
print("• 25.0-29.9: Overweight")
print("• 30.0 and above: Obese")
def bmi_calculator():
    weight = int(input("What is your weight in kg? "))
    height = int(input("What is your height in meter? "))
    bmi = weight / (height^2)
    print(f"Your bmi is {bmi}")
    if bmi < 18.5:
        Category = "Underweight"
        Advice = "Eat more protein"
    elif bmi in range (18.5, 24.9):
        Category = "Normal weight"
        Advice = "KEEP IT UP"
    elif bmi in range(25.0, 29.9):
        Category = "overweight"
        Advice = "LOWER YOUR COLESTEROL"
    else:
        Category = "Obese"
        Advice = "LOWER YOUR COLESTEROL AND HIT THE GYM IF YOU WANT TO LIVE LONG"
    print(f"Result is {Category}\n {Advice}")
bmi_calculator()


# EXERCISE 3: Simple ATM Machine
print("\n" + "="*50)
print("EXERCISE 3: SIMPLE ATM MACHINE")
print("="*50)

print("Create a simple ATM that:")
print("1. Has a starting balance")
print("2. Allows deposit, withdrawal, or balance check")
print("3. Validates transactions")
print("4. Shows appropriate messages")

def ATM_Machine():
    balance = 1000.00 #starting balance
    print(f"Welcome To Simple ATM \n Current balance: ${balance:.2f}")

    operation = input("Choose operstion to perform:\n1.Deposit \n2.Withdraw \n3.Balance \n ").lower

    if operation == "balance" or 1:
        print(f"Your current balance is ${balance:.2f}")
    elif operation == "Deposit" or 2:
        amount = float(input("Input the ammount to deposit: $ "))
        if amount > 0:
            balance += amount
            print(f"Deposited ${amount:.2f} \n Balance ${balance:.2f}")
        else:
            print("Invalid Amount! Must be positive")
    elif operation == "Withdrawal" or 3:
        amount = float(input("Amount to withdraw: $"))
        if amount > 0:
            if amount <= balance:
                balance -= amount
                print(f"Withdrwan :${amount:.2f} \n Remaining balance: ${balance:.2f}")
            else:
                print("Insufficient funds")
        else:
            print("Invalid Ammount! \n Must be positive.")
    else:
        print("Invalid operation!")
ATM_Machine()

# # EXERCISE 4: Quiz Grader
# print("\n" + "="*50)
# print("EXERCISE 4: QUIZ GRADER")
# print("="*50)

# print("Create a quiz grader that:")
# print("1. Asks 5 multiple choice questions")
# print("2. Checks answers against correct answers")
# print("3. Calculates score and percentage")
# print("4. Gives final grade and feedback")

# def quiz_grader_solution():
#     questions = [
#         "What is the capital of France? (a) London (b) Paris (c) Berlin: ",
#         "What is 2 + 2? (a) 3 (b) 4 (c) 5: ",
#         "Which planet is closest to the sun? (a) Venus (b) Mercury (c) Mars: ",
#         "What is the largest ocean? (a) Atlantic (b) Indian (c) Pacific: ",
#         "Who wrote 'Romeo and Juliet'? (a) Shakespeare (b) Dickens (c) Austen: "
#     ]
    
#     correct_answers = ['b', 'b', 'b', 'c', 'a']
#     user_answers = []
# #Ask question 
#     for i, question in enumerate(questions, 1):
#         print(f"Question{i}:{questions} ")
#         answer = input("Your Answer: ").lower()
#         user_answers.append(answer)
#         print()
#     #Grading the quiz 
#     correct_count = 0
#     print("Quiz Result:")
#     print("-"*20)

#     for i, (user_ans, correct_ans) in enumerate(zip(user_answers, correct_answers), 1):
#         if user_ans == correct_ans:
#             print(f"Question{i}: ✅Correct")
#             correct_count += 1
#         else:
#             print(f"Question {i}: ❌ wrong, (correct Answer is {correct_ans})")
#     #Calculate the final result
#     percentage = correct_count / len(questions) * 100

#     print(f"Final score: {correct_count}/{len(questions)} ({percentage:.0f}%)")

#     if percentage >= 90:
#         grade = "A"
#         feedback = "Excellent Work!"
#     elif percentage >= 80:
#         grade = "B"
#         feedback = "Good Job!"
#     elif percentage >=70:
#         grade = "C"
#         feedback = "Satisfactory"
#     elif percentage >= 60:
#         grade = "D"
#         feedback = "Needs improvement"
#     else:
#         grade = "F"
#         feedback = "Study more and try again"
#     print(f"Grade {grade} ")
#     print(f"feedback: {feedback}")
# quiz_grader_solution()

# EXERCISE 5: Rock Paper Scissors Game
print("\n" + "="*50)
print("EXERCISE 5: ROCK PAPER SCISSORS")
print("="*50)

print("Create a Rock Paper Scissors game that:")
print("1. Gets player choice")
print("2. Generates computer choice randomly")
print("3. Determines winner using game rules")
print("4. Shows results clearly")

def Rock_Paper_Scissors():
    import random

    choices = ["rock", "paper", "scissors"]

    print("Let's play Rock Paper Scissors!")
    player_choice = input("Choose rock, paper or scissors: ").lower()

    if player_choice not in choices:
        print("Invalid choice!!")
        return
    
    computer_choice = random.choice(choices)

    print(f"You choose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

#Determine winner
    if player_choice == computer_choice:
        result = "it's a tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
<<<<<<< HEAD
        result = "Computer win!"
    print(f"Result: {result}")
Rock_Paper_Scissors()

# EXERCISE 6: Age Group Classifier
print("\n" + "="*50)
print("EXERCISE 6: AGE GROUP CLASSIFIER")
print("="*50)

print("Create an age classifier that:")
print("1. Takes person's age")
print("2. Classifies into appropriate group")
print("3. Provides relevant information for each group")

print("\nAge groups:")
print("• 0-2: Baby")
print("• 3-12: Child") 
print("• 13-19: Teenager")
print("• 20-64: Adult")
print("• 65+: Senior")
def Age_Classifier():
    age = int(input("What is your age? "))

    if age < 3:
        group = "Baby"
    elif age < 13:
        group = "Child"
    elif age < 20:
        group = "teenager"
    elif age < 65:
        group = "Adult"
    else:
        group = "Senior"
    print(f"Age is {age} \n Your group is {group}")
Age_Classifier()
    
=======
        grade = "F"
        feedback = "Study more and try again"
    print(f"Grade {grade} ")
    print(f"feedback: {feedback}")
quiz_grader_solution()
>>>>>>> b3409455fc0453a518e1dddd47e40e0a21961caf
