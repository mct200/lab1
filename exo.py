import math

def calc_distance(point1, point2):
    distance_squared = 0
    for i in range(len(point1)):
        distance_squared += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance_squared)

def calculate_distances(points1, points2):
    distances = []
    for i in range(len(points1)):
        distances.append(calc_distance(points1[i], points2[i]))
    return distances

points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]

distances = calculate_distances(points1, points2)

print(distances)
