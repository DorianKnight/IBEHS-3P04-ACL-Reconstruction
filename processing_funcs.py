import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math


# sample_data = [0, 0, 0, 0, 1, 4, 4, 5, 6, 8, 9, 20, 40, 40, 50, 53, 57, 80, 85, 89, 90, 91, 100, 110,
#               115, 120, 130, 135, 141, 145, 147, 120, 100, 80, 70, 71, 40, 30, 20, 14, 15, 13, 10, 6, 2, 1, 0, 0, 0]


def plot_SEBT_graph(SEBT_data: list[float], stage: str) -> None:
    num = len(SEBT_data)
    x_values = np.arange(0, num)*0.150+0
    plt.plot(x_values, SEBT_data)
    plt.xlabel("Time (s)")
    plt.ylabel("Knee Flexion Angle (°)")
    plt.title(stage + " Portion of SEBT Test Knee Angle")
    plt.savefig('sebt/'+stage + '_SEBT_KneeAngles.png', dpi=300)
    # plt.show()
    plt.close()


def get_Cof_M(loadcells: list[int]) -> None:
    # important constants stated here
    x1, y1 = -4.1, 5.85
    x2, y2 = 4.1, 5.85
    x3, y3 = -4.1, -5.85
    x4, y4 = 4.1, -5.85

    if sum(loadcells) == 0:
        return int(0), int(0)

    # calculating the center of mass value (x value) of the 4 loadcells and returning that value
    XCofM = round((loadcells[0]*x1 + loadcells[1]*x2 +
                   loadcells[2]*x3 + loadcells[3]*x4)/sum(loadcells), 2)

    # calculating the center of mass value (y value) of the 4 loadcells and returning that value
    YCofM = round((loadcells[0]*y1 + loadcells[1]*y2 +
                   loadcells[2]*y3 + loadcells[3]*y4)/sum(loadcells), 2)

    # adjusting for sensor drift
    if (XCofM, YCofM) == (x1, y1) or (XCofM, YCofM) == (x2, y2) or (XCofM, YCofM) == (x3, y3) or (XCofM, YCofM) == (x4, y4):
        return int(0), int(0)

    return XCofM, YCofM


def get_CofM_deviations(CofM_data: list[tuple]) -> None:
    x_values = []
    y_values = []
    for point in CofM_data:
        x_values.append(point[0])
        y_values.append(point[1])

    maxXdiff = max(x_values) - min(x_values)
    maxYdiff = min(y_values) - min(y_values)

    if maxXdiff > 0.20 or maxYdiff > 0.20:
        stability_score = 'low'
    elif (maxXdiff < 0.20 and maxXdiff > 0.10) or (maxYdiff < 0.2 and maxYdiff > 0.10):
        stability_score = 'medium'
    elif maxXdiff < 0.10 or maxYdiff < 0.10:
        stability_score = 'high'
    else:
        stability_score = 'undefined'

    return (maxXdiff, maxYdiff, stability_score)


def get_min_knee_angle(knee_angle_values: list[float]):
    return min(knee_angle_values)
