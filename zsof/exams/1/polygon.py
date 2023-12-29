import math


def calculate_distance(point1, point2):
    # két pont közti távolság
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def polygon_perimeter(polygon):
    # utolsó pontot összekapcsoljuk az elsővel, hogy zárt polygont kapjunk
    polygon.append(polygon[0])

    # kerület
    perimeter = 0
    for i in range(len(polygon) - 1):
        perimeter += calculate_distance(polygon[i], polygon[i + 1])

    return perimeter


print(polygon_perimeter([(0, 0), (1, 0), (0, 1)]))


