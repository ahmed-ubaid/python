weight=input("Enter your weight in kg(s): ")
height=input("Enter your weight in cm(s): ")
w=int(weight)
h=int(height)
bmi=int((w/((h/100)**2)))

if(bmi<18):
    print(f"Your BMI is {bmi}. You are underweight")
elif(bmi<25):
    print(f"Your BMI is {bmi}. You are healthy")
elif(bmi<30):
    print(f"Your BMI is {bmi}. You are overweight")
elif(bmi<35):
    print(f"Your BMI is {bmi}. You are obese")
else:
    print(f"Your BMI is {bmi}. You are clinically obese")





