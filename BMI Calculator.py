
import tkinter as tk
from tkinter import messagebox
import json
import matplotlib.pyplot as plt
import os
import numpy as np

plt.figure(figsize=(8, 5))

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be positive numbers.")
            return

        bmi = weight / (height ** 2)
        category = classify_bmi(bmi)

        user_data = {
            "weight": weight,
            "height": height,
            "bmi": bmi,
            "category": category
        }

        
        with open("user_data.txt", "a") as f:
            try:
                f.write(json.dumps(user_data) + "\n")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving your data: {e}")

        
        update_bar_chart(bmi)

        result_label.config(text=f"Your BMI is: {bmi:.2f}\nYou are classified as: {category}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values for weight and height.")

def classify_bmi(bmi):
    if bmi is None:
        return "Invalid"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def update_bar_chart(calculated_bmi):
    try:
        
        user_data = []
        with open("user_data.txt", "r") as f:
            for line in f:
                data = json.loads(line)
                user_data.append(data)

        
        categories = ["Underweight", "Normal weight", "Overweight", "Obese"]
        bmi_by_category = {category: [] for category in categories}
        for data in user_data:
            bmi_by_category[data["category"]].append(data["bmi"])

        
        avg_bmi_by_category = {category: np.mean(bmi) for category, bmi in bmi_by_category.items()}

       
        plt.clf()
        bars = plt.bar(categories, [avg_bmi for avg_bmi in avg_bmi_by_category.values()])
        
        
        if calculated_bmi:
            if calculated_bmi < 18.5:
                bars[0].set_color('red')
            elif 18.5 <= calculated_bmi < 25:
                bars[1].set_color('green')
            elif 25 <= calculated_bmi < 30:
                bars[2].set_color('orange')
            else:
                bars[3].set_color('red')

        plt.title("Average BMI by Category")
        plt.xlabel("Category")
        plt.ylabel("BMI")
        plt.grid()
        plt.pause(0.1)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while updating the bar chart: {e}")

root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack()

result_label = tk.Label(root, text="Enter your weight and height, then click 'Calculate BMI'.")
result_label.pack()

root.mainloop()
