# masa / kwadrat wysokosci w metrach
# KALKULATOR BMI

def BMI(masa, wzrost):
    wzrostW_Metrach = wzrost / 100
    bmi = masa / wzrostW_Metrach ** 2

    if 18.5 <= bmi <= 24.99:
        print("Normal Weight ")
    elif bmi < 18.5:
        print("Underweight")
    elif 25.0 <= bmi <= 29.99:
        print("Overweight")
    elif 30.0 <= bmi <= 34.99:
        print("Obesity Class I")
    elif 35.0 <= bmi <= 39.99:
        print("Obesity Class II")
    elif bmi > 40.0:
        print("Obesity Class III")

    return round(bmi, 2)


weight = 70
height = 170
print(BMI(weight, height))
