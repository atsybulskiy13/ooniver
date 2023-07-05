from points import Point
from shapes import Line, Square, Triangle

if __name__ == '__main__':

    point_a = Point(1, 1)
    point_b = Point(1, 3)
    point_c = Point(3, 3)

    line_1 = Line(point_a, point_b)

    print(point_a, point_b)

    print(line_1)

    print(f'Line length - {line_1.find_line_length()}')

    square_1 = Square(point_a, point_b)
    print(square_1.find_square_area())
    print(square_1.find_square_perimeter())

    triangle1 = Triangle(point_a, point_b, point_c)
    print(triangle1.find_triangle_perimeter())
    print(triangle1.find_triangle_area())
