# Case Study 50: Route Distance Analysis

import math

# Coordinates of different locations (x, y)
points = [
    (0, 0),
    (3, 4),
    (6, 8),
    (12, 8)
]

longest = 0

for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print("Distance from", points[i], "to", points[i + 1],
          "=", round(distance, 2))

    if distance > longest:
        longest = distance
        longest_route = (points[i], points[i + 1])

print("\nLongest Route Segment:", longest_route)
print("Longest Distance:", round(longest, 2))
