# 🩺 Medical Calculator (Python)

This project is a beginner-friendly medical calculation tool that currently includes:
- BMI Calculator (Body Mass Index with WHO classification)
- BSA Calculator (Body Surface Area using Mosteller Formula)

More medical tools will be added as the project expands.

---

## 🚀 Features

### ✔ BMI Calculator
- Inputs: weight (kg) and height (m)
- Formula: BMI = weight / (height²)
- Output: BMI rounded to 1 decimal
- WHO Classification:
  - Underweight
  - Normal weight
  - Overweight
  - Obese

### ✔ BSA Calculator
- Inputs: weight (kg) and height (cm)
- Formula (Mosteller):
  \[
  BSA = \sqrt{\frac{height(cm) \times weight(kg)}{3600}}
  \]
- Output: BSA rounded to 2 decimals in m²
### Pediatric Dose Calculator
- Weight-based dosing (mg/kg)
- Safety range validation (min vs max mg/kg)
- Absolute maximum dose warning
- Dose volume conversion (mg → mL)
- Outputs clinically formatted warnings

---

## 📊 Example Menu

=== Medical Calculator ===

1. Calculate BMI


2. Calculate BSA


3. Exit



---

## 💻 How to Run

1. Ensure Python is installed.
2. Clone or download this repository.
3. Run the script:

python bmi_calculator.py

4. Select a number from the menu.

---

## 🔍 Example Output (BMI)

=== BMI Calculator === Enter your weight in kilograms (kg): 70 Enter your height in meters (m): 1.75 Your BMI is: 22.9 Category: Normal weight

---

## 🔍 Example Output (BSA)

=== BSA Calculator === Enter your weight in kilograms (kg): 70 Enter your height in centimeters (cm): 175 Your BSA is: 1.84 m²

---

## 🧠 Skills Demonstrated

- Python basics (input, functions, conditionals)
- Medical mathematics
- WHO BMI classification
- Mosteller BSA formula
- Clean and readable code structure
- Menu-driven program design

---

## 🛠 Future Additions

- Pediatric dose calculator (mg/kg)
- Vital signs interpreter
- Drug dosing safety ranges
- Streamlit web interface
- Database logging for patient results

---

## 👨‍⚕️ Author
Dr. Adeyanu Kehinde Eben
AI in Medicine & Clinical Software Enthusiast