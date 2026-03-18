n = int(input("Enter number of transactions: "))
transactions = []
for i in range(n):
    t = int(input(f"Enter transaction {i+1}: "))
    transactions.append(t)
categories = {
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": []
}
for t in transactions:
    if t <= 0:
        categories["invalid"].append(t)
    elif t <= 500:
        categories["normal"].append(t)
    elif t <= 2000:
        categories["large"].append(t)
    else:
        categories["high_risk"].append(t)
valid_transactions = [t for t in transactions if t > 0]
total_value = sum(valid_transactions)
transaction_count = len(transactions)
frequent = transaction_count > 5
large_spending = total_value > 5000
suspicious = len(categories["high_risk"]) >= 3
if suspicious:
    risk = "High Risk"
elif large_spending or frequent:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"
summary = (total_value, transaction_count, risk)
print("\n--- Transaction Report ---")
print("Categorized Transactions:")
for key, value in categories.items():
    print(f"{key}: {value}")
print("\nTotal Transaction Value:", summary[0])
print("Number of Transactions:", summary[1])
print("Final Risk Classification:", summary[2])
