def on_same_line(ax, ay, bx, by, cx, cy):
    return ax * (by - cy) + bx * (cy - ay) + cx * (ay - by) == 0


Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, input().split())
c = 0
if on_same_line(Ax, Ay, Bx, By, Cx, Cy):
    c += 1
if on_same_line(Ax, Ay, Bx, By, Dx, Dy):
    c += 1
if on_same_line(Ax, Ay, Dx, Dy, Cx, Cy):
    c += 1
if on_same_line(Cx, Cy, Bx, By, Dx, Dy):
    c += 1

print(4 if c == 0 else (3 if c == 1 else 2))
