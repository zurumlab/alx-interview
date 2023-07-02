#!/usr/bin/env python3
def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    triangle_size = int(input("Enter the size of Pascal's triangle: "))
    triangle = pascal_triangle(triangle_size)
    print_triangle(triangle)
