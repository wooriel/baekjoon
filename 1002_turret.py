
# solve baekjoon turret problem

def turret(x1, y1, r1, x2, y2, r2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if dist > r1 + r2:
        return 0
    elif dist == r1 + r2:
        return 1
    elif dist < abs(r1 - r2):
        return 0
    elif dist == abs(r1 - r2):
        return 1 
    else: 
        return 2 

    
print(turret(0, 0, 3, 0, 7, 2))