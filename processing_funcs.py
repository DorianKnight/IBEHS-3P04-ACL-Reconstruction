import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
from collections import defaultdict
from plotting import *


# sample_data = [0, 0, 0, 0, 1, 4, 4, 5, 6, 8, 9, 20, 40, 40, 50, 53, 57, 80, 85, 89, 90, 91, 100, 110,
#               115, 120, 130, 135, 141, 145, 147, 120, 100, 80, 70, 71, 40, 30, 20, 14, 15, 13, 10, 6, 2, 1, 0, 0, 0]


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


# ONLY FOR TESTING // DELETE LATER
a = [(1.6209302325581396, -1.4965116279069766), (1.4548387096774191, -
                                                 1.5096774193548386), (1.5043165467625896, -1.0521582733812949), (1.3666666666666665, -1.6316326530612246),
     (1.1832214765100668, -2.080872483221476), (0.8424657534246573, -1.1219178082191779), (0.7653333333333333, -
                                                                                           0.7799999999999998), (1.010958904109589, -0.8013698630136988), (1.1549295774647887, -0.32957746478873207),
     (1.4033557046979863, 0.43187919463087227), (1.6785234899328856, 0.03926174496644311), (
    1.7335570469798656, -0.35335570469798644), (1.589795918367347, 0.0397959183673471),
    (1.544155844155844, 0.4558441558441558), (1.1714285714285713, -0.4558441558441558), (0.43617021276595747, -1.8670212765957446), (0.43617021276595747, 0.7053191489361701), (0.6594405594405592, 1.104545454545455), (1.5476821192052979, 0.11622516556291398), (1.5769230769230764, -0.6954545454545458), (1.5375, -0.07312499999999993), (0.9595744680851063, 0.2074468085106383), (1.384415584415584, 0.9876623376623378), (1.6746478873239437,
                                                                                                                                                                                                                                                                                                                                                                                                                                  0.9063380281690144), (1.7038961038961038, 1.1396103896103893), (1.7105960264900664, -0.6586092715231787), (1.5228571428571427, 0.0835714285714289), (1.6346405228758167, -0.19117647058823528), (1.6506493506493505, -0.07597402597402664), (1.2356164383561643, -0.4808219178082195), (0.8519480519480519, -0.8357142857142859), (0.7202702702702702, -0.7114864864864862), (0.5228187919463088, -0.03926174496644311), (0.8960264900662253, -0.19370860927152317), (1.0819444444444444, -0.5687499999999999), (1.03943661971831, 0.4119718309859155), (1.3289655172413792, 0.36310344827586233), (1.2551020408163265, 1.3132653061224493), (1.1232876712328765, 2.8047945205479454), (1.3479452054794518, 2.484246575342466), (1.5853333333333333, 1.1700000000000004), (1.4933774834437084, 1.5884105960264894), (1.5340136054421767, 2.029591836734694), (1.4436619718309855, 2.8838028169014076), (1.4213333333333331, 2.262), (0.6648648648648647, 0.5533783783783786), (0.5447552447552448, -0.8590909090909089), (0.8613445378151258, -1.4256302521008402), (1.198461538461538, -1.35), (1.5374999999999996, 0.7312500000000002), (1.3666666666666667, 1.95), (1.9421052631578943, 2.155263157894737), (1.7571428571428567, 3.6214285714285706), (1.3666666666666667, 3.6214285714285706), (1.64, 1.7549999999999994), (1.9421052631578943, 0.9236842105263157), (1.9421052631578943, 0.9236842105263157), (1.6882352941176468, 1.032352941176471), (1.9421052631578943, 0.9236842105263157), (1.822222222222222, 1.2999999999999998), (2.2777777777777772, 1.2999999999999998), (2.3736842105263154, 1.5394736842105259), (2.170588235294117, 1.0323529411764705), (2.1705882352941175, 0.34411764705882364), (2.05, 0.0), (1.9133333333333333, 1.1700000000000004), (1.1181818181818182, 1.5954545454545452), (-1.3666666666666665, 5.849999999999999), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
b = [(1.40335, 0.43187), (1.678523, 0.03926), (1.73355, -0.3533)]

CofM_data = {
    'Anterior': [a, b],
    'Anterolateral': [a, b],
    'Anteromedial': [a, b],
    'Lateral': [a, b],
    'Medial': [a, b],
    'Posterolateral': [a, b],
    'Posteromedial': [a, b],
    'Posterior': [a, b]
}
# ONLY FOR TESTING ABOVE DELETE LATER!!!


def get_CofM_deviations(CofM_data: dict) -> dict:
    std_op_x = defaultdict()
    std_nonop_x = defaultdict()
    std_op_y = defaultdict()
    std_nonop_y = defaultdict()
    std_x_diff = defaultdict()
    std_y_diff = defaultdict()

    total_x = 0
    total_y = 0

    for item in CofM_data:
        op_leg_data = filter_for_calcs(CofM_data[item][0])
        nonop_leg_data = filter_for_calcs(CofM_data[item][1])
        std_op_x[item] = np.std([point[0] for point in op_leg_data])
        std_op_y[item] = np.std([point[1] for point in op_leg_data])
        std_nonop_x[item] = np.std([point[0] for point in nonop_leg_data])
        std_nonop_y[item] = np.std([point[1] for point in nonop_leg_data])
        std_x_diff[item] = round(abs(std_op_x[item] - std_nonop_x[item]), 3)
        std_y_diff[item] = round(abs(std_op_y[item] - std_nonop_y[item]), 3)
        total_x += std_x_diff[item]
        total_y += std_y_diff[item]

    avg_x_diff = round(total_x/8, 2)
    avg_y_diff = round(total_y/8, 2)

    if avg_x_diff > 1 or avg_y_diff > 1:
        stability_score = 'Low 🔴. The balancing of the patient highly differs from the non-operative and operative leg. \
        Please book appointment with patient soon if necessary.'
    elif (avg_x_diff > 0.3 and avg_x_diff <= 1) or (avg_y_diff > 0.3 and avg_y_diff <= 1):
        stability_score = 'Medium 🟡. The balancing of the patient moderately differs from the non-operative and operative leg.\
            Clinician intervention may be required.'
    else:
        stability_score = 'High 🟢. The balancing of the patient does not differ substantially from the non-operative and operative leg. \
            Recovery on track.'

    return stability_score, std_x_diff, std_y_diff


def get_knee_angle_scores(SEBT_data):
    angle_diffs = defaultdict()

    total_diffs = 0
    for item in SEBT_data:
        angle_diffs[item] = max(SEBT_data[item][1]) - max(SEBT_data[item][0])
        total_diffs += angle_diffs[item]

    avg_angle_diff = round((total_diffs/8), 2)

    if avg_angle_diff > 10:
        stability_score = 'Low 🔴. The knee could be highly unstable and there is a severe cause of concern.'
    elif avg_angle_diff > 5 and avg_angle_diff < 10:
        stability_score = 'Medium 🟡. The knee might be minorly unstable and there might be a minor cause of concern.'
    elif avg_angle_diff <= 5:
        stability_score = 'High 🟢. The knee is likely stable and there is no cause of concern.'

    return stability_score, angle_diffs


# print(get_CofM_deviations(CofM_data))
