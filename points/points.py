class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def find_distance_btw_points(self, other):

        a = self.x - other.x
        b = self.y - other.y

        distance_btw_points = (a ** 2 + b ** 2) ** 0.5

        return distance_btw_points
