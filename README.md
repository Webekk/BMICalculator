# BMI Calculator

## 📌 Description
This is a simple **Body Mass Index (BMI) Calculator** written in Python. The program calculates BMI based on user-provided weight (kg) and height (cm) and categorizes the BMI value into different health classifications.

## 🖥️ How It Works
The BMI formula used:

\[ BMI = \frac{masa}{(wzrost / 100)^2} \]

Where:
- **masa**: Weight in kilograms (kg)
- **wzrost**: Height in centimeters (cm)

### 📊 BMI Categories
| BMI Value        | Category               |
|-----------------|-----------------------|
| **< 18.5**     | Underweight            |
| **18.5 - 24.99** | Normal Weight        |
| **25.0 - 29.99** | Overweight           |
| **30.0 - 34.99** | Obesity Class I      |
| **35.0 - 39.99** | Obesity Class II     |
| **> 40.0**      | Obesity Class III     |

## 🚀 Usage
### 1️⃣ Run the Script
Ensure you have Python installed. Copy and paste the following code into a Python file (e.g., `bmi_calculator.py`) and run it:
```python
# BMI Calculator

def BMI(masa, wzrost):
    wzrostW_Metrach = wzrost / 100
    bmi = masa / wzrostW_Metrach ** 2

    if 18.5 <= bmi <= 24.99:
        print("Normal Weight")
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
```

### 2️⃣ Input Parameters
Replace the `masa` (weight) and `wzrost` (height) values with your own measurements:
```python
print(BMI(your_weight, your_height))
```

### Example:
```python
print(BMI(70, 175))
```
#### Output:
```
Normal Weight
22.86
```

## 🛠️ Improvements
- Add **user input** to allow dynamic BMI calculation.
- Convert the script into a **GUI application** using Tkinter.
- Allow **imperial unit conversion** (lbs/inches → kg/cm).

## 📝 License
This project is open-source. Feel free to modify and distribute!

