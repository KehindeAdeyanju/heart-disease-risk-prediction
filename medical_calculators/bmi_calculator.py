
# BMI Calculator Program
# Created by Dr.Adeyanju Kehinde Eben
# This tool calculates BI and classifies it based on WHP guidelines



def calculate_bmi():
    """Calculate and display the user's BMI and category."""
    print("===BMI Calculator===")


# 1. Ask for weight
    weight = float(input("Enter your weight in kilograms (kg): "))

# 2. Ask for height
    height = float(input("Enter your height in meters (m): "))

# 3.  Calculate
    bmi = weight / (height** 2)

#4. Round BMI for cleaner output
    bmi = round(bmi, 1)
#5. Print BMI result
    print("Your BMI is:", bmi)

# Main menu for the medical calculator
    if bmi < 18.5:
        print ("Category: Underweight")
    elif bmi < 25 :
        print ("Category: Normal weight")
    elif bmi < 30 :
        print("Category: Overweight")
    else:
        print ("Category: Obese")

def calculate_bsa():
        print("=== BSA Calculator ===")
# 1. Ask for weight
        weight = float(input("Enter your weight in kilograms (kg): "))

# 2. Ask for height (in centimeters)
        height = float(input("Enter your height in centimeters (cm): "))

# 3.  Calculate BSA using Mosteller Formula
        bsa = ((height * weight) / 3600) ** 0.5

# 4.  Print BSA neatly
        print("Your BSA is:", round(bsa, 2), "m²")

def calculate_pediatrics_dose():
    print("=== Pediatric Dose Calculator ===")

# 1. Ask for Child's Weight
    weight = float(input("Enter the child's weight in kilograms (kg): "))

# 2. Ask for mg/kg dose ( the prescription strength)
    mg_per_kg = float(input("Enter the dose in mg per kg (mg/kg): "))

#7. Add minimum/maximum mg/kg inputs

    min_mg_per_kg = float(input("Enter the minimum recommended mg/kg: "))
    max_mg_per_kg = float(input("Enter the maximum recommended mg/kg: "))




#3. Calculate Total Dose
    total_dose = weight * mg_per_kg


#5.  Add max Dose Input
    max_dose = float(input("Enter the maximum allowed total dose (mg): "))
# CALCULATING REQUIRED VOLUME

    concentration = float(input("Enter the drug concentration in mg per mL: "))
    volume = total_dose / concentration   #This gives us the mL needed

#6. Add Safety Check
    if mg_per_kg < min_mg_per_kg:
        print("⚠️ WARNING: Dose per kg is below recommended minimum! ")
    elif mg_per_kg > max_mg_per_kg:
        print("⚠️ WARNING: Dose per kg exceeds recommended maximum! ")

    elif total_dose > max_dose:
        print("⚠️ WARNING: Calculated dose exceeds maximum limit!")

    else:


#4. Print total dose.
        print("\n✔️ Dose is within safe range.")
        print("Total dose to administer:", total_dose, "mg")
        print("Volume to administer:", volume, "mL\n")





print("=== Medical Calculator ===")
print("1. Calculate BMI")
print("2. Calculate BSA")
print("3. Pediatric Dose Calculator")
print("0. Exit")

choice = input("select an option (0-3) : ")
if choice == "1":
    calculate_bmi()
elif choice == "2":
    calculate_bsa()
elif choice == "3":
    calculate_pediatrics_dose()
elif choice == "0":
    print("Goodbye!")
else:
    print("Invalid choice. Please run the program again.")





