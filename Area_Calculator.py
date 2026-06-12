import math

# Read the shape
shape = str(input().strip())

# Read measurements and calculate area
if shape=='rectangle':
  base=int(input().strip())
  height=int(input().strip())
  print(f"Area: {base*height:.2f}")
if shape=='triangle':
  base=int(input().strip())
  height=int(input().strip())
  print(f"Area: {base*height*0.5:.2f}")
if shape=='circle':
  ri=int(input().strip())
  print(f"Area: {math.pi*ri*ri:.2f}")
# Print the area
