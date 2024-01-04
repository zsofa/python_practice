import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Straight Zsofitol loptam itt mindent
def polygon_perimeter(polygon):
    polygon.append(polygon[0])

    distances = [distance(p1, p2) for p1, p2 in zip(polygon, polygon[1:] + [polygon[0]])]

    return sum(distances)
