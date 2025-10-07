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
    print(f"Result is {Category}, {Advice}")
bmi_calculator()
