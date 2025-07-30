import math

def mat_print(m):
    for row in m:
        print(' '.join(f"{v:.4f}" for v in row))

tx, ty = map(float, input("Enter tx ty for Translation: ").split())
theta = float(input("Enter rotation angle in degrees: "))
sx, sy = map(float, input("Enter sx sy for Scaling: ").split())

r = math.radians(theta)
cos_t, sin_t = math.cos(r), math.sin(r)

T = [[1, 0, tx],
     [0, 1, ty],
     [0, 0, 1]]

R = [[cos_t, -sin_t, 0],
     [sin_t,  cos_t, 0],
     [0,      0,     1]]

S = [[sx, 0,  0],
     [0, sy,  0],
     [0,  0,  1]]

print("\nTranslation Matrix:")
mat_print(T)
print("\nRotation Matrix:")
mat_print(R)
print("\nScaling Matrix:")
mat_print(S)


