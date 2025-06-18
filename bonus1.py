weight = input("enter your weight: ")
height = input("enter your height: ")
BMI = float(weight) / (float(height) ** 2)
print("your BMI is " + str(BMI))

if(BMI >= 25 and BMI <= 29.9):
    print("You are overwieght you need to work out more and watch your diet.")
elif(BMI >= 18.5 and BMI < 24.9):
    print("You are fit & healthy")
elif(BMI <= 18.5):
    print("You are underweight. Watch your health.")