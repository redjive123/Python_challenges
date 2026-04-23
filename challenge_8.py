import random
import math
import numpy as np
import pandas as pd
def generate_data(num_students):
    data = []
    for i in range(1, num_students + 1):
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)
        performance_index = (marks * 0.6 + assignment * 0.4) * math.log(attendance + 1)
        data.append((i, marks, attendance, assignment, performance_index))
    return data
def classify_students(df):
    categories = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }
    for _, row in df.iterrows():
        sid = row['student_id']
        marks = row['marks']
        attendance = row['attendance']
        if marks < 40 or attendance < 50:
            categories["At Risk"].append(sid)
        elif 40 <= marks <= 70:
            categories["Average"].append(sid)
        elif 71 <= marks <= 90:
            categories["Good"].append(sid)
        elif marks > 90 and attendance > 80:
            categories["Top Performer"].append(sid)
    return categories
def analyze_data(df):
    marks_array = df['marks'].values
    mean_marks = np.mean(marks_array)
    median_marks = np.median(marks_array)
    std_dev = np.std(marks_array)
    manual_mean = sum(marks_array) / len(marks_array)
    correlation = np.corrcoef(df['marks'], df['attendance'])[0][1]
    min_val = np.min(marks_array)
    max_val = np.max(marks_array)
    df['normalized_marks'] = [(x - min_val) / (max_val - min_val) for x in marks_array]
    consistency = "Consistent" if std_dev < 15 else "Inconsistent"
    attendance_risk = len([a for a in df['attendance'] if a < 50]) > 3
    high_achievers = len(df[(df['marks'] > 90) & (df['attendance'] > 80)]) >= 2
    if consistency == "Consistent" and not attendance_risk and high_achievers:
        insight = "Stable Academic System"
    elif attendance_risk:
        insight = "Critical Attention Required"
    else:
        insight = "Moderate Performance"
    summary_tuple = (mean_marks, std_dev, np.max(marks_array))
    return {
        "mean": mean_marks,
        "median": median_marks,
        "std_dev": std_dev,
        "manual_mean": manual_mean,
        "correlation": correlation,
        "consistency": consistency,
        "attendance_risk": attendance_risk,
        "high_achievers": high_achievers,
        "summary_tuple": summary_tuple,
        "insight": insight
    }
num_students = 7
student_data = generate_data(num_students)
df = pd.DataFrame(student_data, columns=[
    'student_id', 'marks', 'attendance', 'assignment', 'performance_index'
])
categories = classify_students(df)
analysis = analyze_data(df)
print("\n--- Student Data ---")
print(df)
print("\n--- Categories ---")
print(categories)
print("\n--- Statistical Summary ---")
print("Mean:", analysis['mean'])
print("Median:", analysis['median'])
print("Std Dev:", analysis['std_dev'])
print("Manual Mean:", analysis['manual_mean'])
print("Correlation (Marks vs Attendance):", analysis['correlation'])
print("\n--- Tuple Output ---")
print("(mean, std_dev, max_marks):", analysis['summary_tuple'])
print("\n--- Final Insight ---")
print(analysis['insight'])