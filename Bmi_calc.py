import pandas as pd
import json

lst = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 200},
           {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
           {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
           {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
           {"Gender": "male", "HeightCm": 167, "WeightKg": 82},
           {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
final_lst = []

def calculate_bmi(data):
    # print(data)
    g1 = data['Gender']
    h1 = data['HeightCm']
    if int(h1)<0:
        raise Exception("Height can't be negative")

    w1 = data['WeightKg']
    if int(w1)<0:
        raise Exception("Weight can't be negative")

    try:
        bmi = w1 / (h1 / 100) ** 2
    except Exception as e:
        print(str(e))

    # print(g1, h1, w1, bmi)
    if bmi <= 18.4:
        return {"Height":h1,"Weight":w1,"Gender":g1,"BMI Category": "Underweight","BMI Range (kg/m²)" : "18.4 and below",
                "Health Risk":"Malnutrition Risk"}
    elif bmi >= 18.5 and bmi < 24.9:
        return {"Height":h1,"Weight":w1,"Gender":g1,"BMI Category": "Normal weight","BMI Range (kg/m²)" : "18.5 - 24.9",
                "Health Risk":"Low Risk"}
    elif bmi >= 25 and bmi < 29.9:
        return {"Height":h1,"Weight":w1,"Gender":g1,"BMI Category": "Overweight", "BMI Range (kg/m²)": "25 - 29.9",
                "Health Risk": "Enhanced risk"}
    elif bmi >= 30 and bmi < 34.9:
        return {"Height":h1,"Weight":w1,"Gender":g1,"BMI Category": "Moderately Obese","BMI Range (kg/m²)" : "30 - 34.9",
                "Health Risk":"Medium risk"}
    elif bmi >= 35 and bmi < 39.9:
        return {"Height":h1,"Weight":w1,"Gender":g1,"BMI Category": "Severely Obese", "BMI Range (kg/m²)": "35 - 39.9",
                "Health Risk": "High Risk"}
    else:
        return {"Height":h1,"Weight":w1,"Gender":g1,"BMI Category": "Very Severely Obese","BMI Range (kg/m²)" : "40 and above",
                "Health Risk":"Very High Risk"}

for data in lst:
    bmi = calculate_bmi(data)
    final_lst.append(bmi)
    print(bmi)
df = pd.DataFrame(final_lst)
total_overweight_cnt = (df['BMI Category'] == 'Overweight').sum()
print("total_overweight_cnt",total_overweight_cnt)
