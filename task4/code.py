# Case Study 40: Traffic Flow and Congestion Analysis

roads = ["Road A", "Road B", "Road C"]
vehicles = [450, 800, 600]
capacity = 700

highest = 0
peak_road = ""
    
for i in range(len(roads)):
    print("\nRoad:", roads[i])
    print("Vehicle Count:", vehicles[i])

    if vehicles[i] > capacity:
        print("Congestion: High")
    elif vehicles[i] >= 500:
        print("Congestion: Medium")
    else:
        print("Congestion: Low")

    if vehicles[i] > highest:
        highest = vehicles[i]
        peak_road = roads[i]

print("\nPeak Traffic Road:", peak_road)
print("Maximum Vehicle Count:", highest)
