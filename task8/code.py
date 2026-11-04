# Case Study 80: Bus Route Performance

routes = ["Route A", "Route B", "Route C"]
passengers = [45, 60, 35]
journey_time = [40, 55, 30]
fuel = [8, 12, 6]
capacity = 50

for i in range(len(routes)):
    print("\nRoute:", routes[i])
    print("Passengers:", passengers[i])
    print("Journey Time:", journey_time[i], "minutes")
    print("Fuel Used:", fuel[i], "litres")

    if passengers[i] > capacity:
        print("Status: Overloaded")
    else:
        print("Status: Within Capacity")

    if passengers[i] > 0:
        efficiency = passengers[i] / fuel[i]
        print("Passengers per Litre:", round(efficiency, 2))

fastest = min(journey_time)
print("\nFastest Journey Time:", fastest, "minutes")
