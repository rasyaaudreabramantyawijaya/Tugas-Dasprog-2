weight_in = float(input("Weight (lb): "))
height_in = float(input("Height (in): "))

bmi = round(703 * weight_in / height_in**2)

if bmi < 18.5:
    status = "Underweight"
if 18.5 < bmi < 24.9:
    status = "Normal"
if 25.0 < bmi < 29.9:
    status = "Overweight"
if bmi > 30.0:
    status = "Obese"

# Output
print(f"BMI: {bmi}, Status: {status}")