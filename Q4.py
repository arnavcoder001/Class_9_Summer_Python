#This code gives the area and perimeter of shapes.
shape=input("Enter shape(Circle, Rectangle, Square, Triangle): ")

if shape == "Circle":
    radius = float(input("Enter the radius: "))
    area = 3.14 * radius * radius
    perimeter = 2 * 3.14 * radius

elif shape == "Rectangle":
    length = float(input("Enter the length: "))
    breadth = float(input("Enter the breadth: "))
    area = length + breadth
    perimeter = 2 * (length + breadth)

elif shape == "Square":
    side = float(input("Enter the side: "))
    area = side * side
    perimeter = 4 * side

elif shape == "Triangle":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = 1/2 * base * height
    perimeter = base + height + base

else:
    print("Invalid shape entered.")


print(f"\nshape: {shape.capitalize()}")
print(f"Perimeter: {perimeter:.2f}")
print(f"Area: {area:.2f}")
    