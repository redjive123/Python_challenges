import random
import copy
import math
import numpy as np
import pandas as pd
def generate_students(n=12):
    students = []
    for i in range(n):
        student = {
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 30), random.randint(10, 30)]
        }
        students.append(student)
    return students
def mutate_data(data, roll_number):
    mod_val = roll_number % 3
    for i in range(len(data)):
        if i % mod_val == 0:
            data[i]["marks"] += math.sqrt(data[i]["marks"])
            data[i]["scores"][0] += 5
            data[i]["attendance"] -= 10
    return data
def analyze_data(data):
    df = pd.DataFrame(data)
    marks = df["marks"].values
    mean = np.mean(marks)
    median = np.median(marks)
    std_dev = np.std(marks)
    manual_mean = sum(marks) / len(marks)
    df["normalized_marks"] = (marks - np.min(marks)) / (np.max(marks) - np.min(marks))
    return df, mean, median, std_dev, manual_mean
def detect_drift(original_mean, modified_mean, threshold=5):
    drift = abs(original_mean - modified_mean)
    if drift > threshold:
        return drift, "Critical Drift"
    elif drift > 2:
        return drift, "Minor Drift"
    else:
        return drift, "Stable Data"
def check_copy_failure(original, shallow):
    if original != shallow:
        return "Copy Failure Detected"
    return "No Copy Failure"
roll_number = 23
original_data = generate_students()
shallow_copy = original_data.copy()
deep_copy = copy.deepcopy(original_data)
mutate_data(shallow_copy, roll_number)
mutate_data(deep_copy, roll_number)
orig_df, orig_mean, _, orig_std, manual_mean = analyze_data(original_data)
shallow_df, shallow_mean, _, shallow_std, _ = analyze_data(shallow_copy)
deep_df, deep_mean, _, deep_std, _ = analyze_data(deep_copy)
drift, status = detect_drift(orig_mean, deep_mean)
failure_status = check_copy_failure(original_data, shallow_copy)
print("\nOriginal DataFrame:\n", orig_df)
print("\nShallow Copy DataFrame:\n", shallow_df)
print("\nDeep Copy DataFrame:\n", deep_df)
print("\nDrift Value:", drift)
print("Tuple:", (orig_mean, drift, orig_std))
print("\nFinal Classification:")
print(status)
print(failure_status)