import pylab as P

def split_line(pt1, pt2):
    """Given two complex numbers p1 and p2 return a list of the
    necessary points pairwise.
    """
    # The points we generate are p1, p2, p3, p4 and p5
    p1, p5 =  pt1, pt2
    diff = pt2 - pt1
    segment = diff/3.0
    p2 = p1 + segment
    p4 = p5 - segment
    # Now rotate a line given by 60degrees.
    # Recall that complex multiplication does this easily.
    # Complex numbers are defined by complex(a, b) also.
    p3 = p2 + segment*complex(P.cos(P.pi/3), P.sin(P.pi/3))
    return [(p1, p2), (p2, p3), (p3, p4), (p4, p5)]

def koch(n):
    start = complex(0, 0)
    end = complex(1, 0)
    points = [(start, end)]
    for level in range(n):
        new_points = []
        for (p1, p2) in points:
            new_points.extend(split_line(p1, p2))
        points = new_points
    points.insert(0, (start, points[0][0]) )
    points.append((points[-1][1], end))
    return points

def plot_koch(n):
    points = koch(n)
    x = [t[0].real for t in points]
    y = [t[0].imag for t in points]

    P.plot(x, y, 'r-')
    P.ylim(0, 1)
    P.xlim(0, 1)

