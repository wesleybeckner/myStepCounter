import numpy as np

## TODO: Code for loading and visualizing accelerometer data
def count_steps(url):
    accel = np.array(url)
    z = np.array(accel[:,3])
    t = np.array(accel[:,0])
    points = np.diff(np.diff(z) < 0)
    points = [i[0] for i in np.argwhere(points)]
    points2 = [i[0] for i in np.argwhere(np.fabs(z[1:-1][points])>1)]
    steps = 0
    for index, time in enumerate(t[1:-1][points][points2][:-1]):
        if (z[1:-1][points][points2][index] > 0 and
            z[1:-1][points][points2][index+1] < 0):
            time_down = t[1:-1][points][points2][index+1]

            # if the time delta is less than 1 sec
            # if time_down - time <= 1:
            steps += 1
    # print(steps)
    return steps
