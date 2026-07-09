# 1) Ask the user to enter their height in centimeters and store it in `height`.
Height = (float(input("Enter your Height")))
HeightM = Height/100
# 2) Ask the user to enter their weight in kilograms and store it in `weight`.
Weight = (float(input("Enter Your Weight")))
# 3) Calculate BMI using the formula:
#    BMI = weight ÷ (height in meters)²
#    (Convert height from cm to meters by dividing by 100.)
#    Store the result in `BMI`.
# 4) Print the BMI value.
BMI = Weight/HeightM**2
# 5) Use if–elif–else to decide the BMI category:
#    - If BMI is 18.4 or less → print "underweight"
#    - Else if BMI is 24.9 or less → print "healthy"
#    - Else if BMI is 29.9 or less → print "over weight"
#    - Else if BMI is 34.9 or less → print "severely over weight"
#    - Else if BMI is 39.9 or less → print "obese"
#    - Else → print "severely obese"

if BMI <= 18.4:
    print("Underweight")
elif BMI <= 24.9:
    print("Healthy")
elif BMI <= 29.9:
    print("Over Weight")
elif BMI <= 34.9:
    print("Severely over weight")
elif BMI <= 39.9:
    print("Obese")
else:
    print("Severely Obese")
