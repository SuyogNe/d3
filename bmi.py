h=float(input("Enter your height : "))
w=float(input("Enter your weight in kilograms: "))
bmi=w/(h/100)**2
print("your BMI is: ",bmi)
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25:
    print("Normal weight")
elif bmi>=25 and bmi<30:
    print("Overweight")
else:
    print("Obese")
