# Case Study 90: Campus Energy and Water Audit

buildings = ["Block A", "Block B", "Block C"]

# Electricity usage in units and water usage in litres
electricity = [
    [100, 120, 110],
    [200, 180, 220],
    [80, 90, 85]
]

water = [
    [1000, 1100, 1050],
    [2000, 2200, 2100],
    [800, 850, 900]
]

electricity_rate = 8
water_rate = 0.05

costs = []

for i in range(len(buildings)):
    total_electricity = sum(electricity[i])
    total_water = sum(water[i])

    electricity_cost = total_electricity * electricity_rate
    water_cost = total_water * water_rate
    total_cost = electricity_cost + water_cost

    costs.append((buildings[i], total_cost))

    print("\nBuilding:", buildings[i])
    print("Electricity Units:", total_electricity)
    print("Water Used:", total_water, "litres")
    print("Electricity Cost: Rs.", electricity_cost)
    print("Water Cost: Rs.", water_cost)
    print("Total Cost: Rs.", total_cost)

    if total_electricity > 400 or total_water > 4000:
        print("Warning: High Consumption")
    else:
        print("Consumption: Within Limit")

costs.sort(key=lambda x: x[1], reverse=True)

print("\nBuildings Ranked by Total Cost:")

for building, cost in costs:
    print(building, "- Rs.", cost)
