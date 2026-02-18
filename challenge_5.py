requests = [10, 25, 60, -3, 0, 45, 80]
full_name = "Yuvraj Verma"
L = len(full_name.replace(" ", ""))
PLI = L % 3
low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []
total_valid = 0
for r in requests:
    if r < 0:
        invalid_requests.append(r)
    elif r == 0:
        pass
    elif 1 <= r <= 20:
        low_demand.append(r)
        total_valid += 1
    elif 21 <= r <= 50:
        moderate_demand.append(r)
        total_valid += 1
    elif r > 50:
        high_demand.append(r)
        total_valid += 1
removed_count = 0
if PLI == 0:      # Rule A
    removed_count = len(low_demand)
    low_demand = []
elif PLI == 1:
    removed_count = len(high_demand)
    high_demand = []
elif PLI == 2:
    removed_count = len(low_demand) + len(high_demand)
    low_demand = []
    high_demand = []
print("Full Name Length (L):", L)
print("PLI Value:", PLI)
print("Total Valid Requests:", total_valid)
print("Removed Requests due to PLI:", removed_count)
print("\nFinal Dispatch Lists:")
print("Low Demand:", low_demand)
print("Moderate Demand:", moderate_demand)
print("High Demand:", high_demand)
print("Invalid Requests:", invalid_requests)
