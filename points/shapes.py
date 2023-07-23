from points import Point


class Line:

    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.line_length = self.point_a.find_distance_btw_points(self.point_b)

    def __str__(self):
        return f'Line ({self.point_a}, {self.point_b})'


class Square:

    def __init__(self, point_a: Point, point_c: Point):
        self.point_a = point_a
        self.point_c = point_c

        point_b = Point(point_a.x, point_c.y)
        self.point_b = point_b

        point_d = Point(point_c.x, point_a.y)
        self.point_d = point_d

    def find_diagonal_length(self):
        diagonal_length = self.point_a.find_distance_btw_points(self.point_c)

        return diagonal_length

    def find_square_area(self):
        diagonal = Square.find_diagonal_length(self)
        square_area = diagonal ** 2 / 2

        return square_area

    def find_square_perimeter(self):
        diagonal = Square.find_diagonal_length(self)
        square_perimeter = (diagonal * 2) ** 0.5

        return square_perimeter


class Triangle:

    def __init__(self, point_a: Point, point_b: Point, point_c: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

        self.ab_side = self.point_a.find_distance_btw_points(self.point_b)
        self.ac_side = self.point_a.find_distance_btw_points(self.point_c)
        self.bc_side = self.point_b.find_distance_btw_points(self.point_c)

        if self.ab_side + self.bc_side <= self.ac_side or self.ab_side + self.ac_side <= self.bc_side or self.bc_side \
                + self.ac_side <= self.ab_side:
            raise Exception("It's not a triangle")

    def find_triangle_perimeter(self):
        triangle_perimeter = self.ab_side + self.ac_side + self.bc_side

        return triangle_perimeter

    def find_triangle_area(self):
        pp = Triangle.find_triangle_perimeter(self) / 2

        triangle_area = (pp * (pp - self.ac_side) * (pp - self.ab_side) * (pp - self.bc_side)) ** 0.5

        return triangle_area
