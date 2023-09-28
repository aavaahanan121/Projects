def Findparllel2d(ax, ay, bx, by):
    if (ax * bx) + (ay * ax) == 0:
        return True
    else:
        return False

def Findparllel3d(ax, ay, az, bx, by, bz):
    if (ax * bx) + (ay * ax) + (az * bz) == 0:
        return True
    else:
        return False

print(Findparllel3d(-3, -2, 2, 4, 5, 11))
