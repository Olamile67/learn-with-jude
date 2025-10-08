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

