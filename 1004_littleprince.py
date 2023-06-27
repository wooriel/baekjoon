
def in_planet(px, py, cx, cy, r):
    d = pow(pow(px-cx, 2) + pow(py-cy, 2), 1/2)
    if d < r:
        return 1
    else:
        return 0


if __name__ == "__main__":
    test_case = int(input())

    pts = []
    crosses = []
    planets = []
    for i in range(test_case):
        pts.append(list(map(int, input().split())))
        crosses.append(0)
        planets.append(int(input()))
        for j in range(planets[i]):
            # check if the x1 y1 and x2 y2 is in/out(out/in) of the planet
            c = list(map(int, input().split()))
            if in_planet(pts[i][0], pts[i][1], c[0], c[1], c[2]) != in_planet(pts[i][2], pts[i][3], c[0], c[1], c[2]):
                crosses[i] += 1
    

    for i in range(test_case):
        print(crosses[i])
