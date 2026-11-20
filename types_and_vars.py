"""Show variables, common data types, and simple operators."""

# Store profile details in variables and use them in the introduction.
name = "Corey"
age = 33
height = 1.778

print(f"Hello, my name is {name}. I am {age} years old and {height:.3f} meters tall.")

# Add five years to the age stored above.
future_age = age + 5
print(f"In 5 years, I will be {future_age} years old.")

# Multiply the width and height to find the rectangle area.
width = 5.5
rectangle_height = 2
area = width * rectangle_height
print(f"The area of a {width} x {rectangle_height} rectangle is {area}.")

# String repetition uses the multiplication operator too.
print(("Python! " * 2).rstrip())
