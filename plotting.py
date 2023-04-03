import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def filter_for_calcs(points: list[tuple]):
    new_points = []
    x1, y1 = -4.1, 5.85
    x2, y2 = 4.1, 5.85
    x3, y3 = -4.1, -5.85
    x4, y4 = 4.1, -5.85
    for point in points:
        if point != (x1, y1) and point != (x2, y2) and point != (x3, y3) and point != (x4, y4) and point != (0, 0):
            new_points.append(point)
    return new_points


def plot_CofM_deviations(op_leg_data: list[(float, float)], nonop_leg_data: list[(float, float)], stage: str):
    operative_leg = filter_for_calcs(op_leg_data)
    nonoperative_leg = filter_for_calcs(nonop_leg_data)

    fig, (ax1, ax2) = plt.subplots(1, 2)

    for point in operative_leg:
        ax2.plot(point[0], point[1], color='red',
                 label='original', marker='o', markersize=3)
    for point in nonoperative_leg:
        ax1.plot(point[0], point[1], color='green',
                 label='original', marker='o', markersize=3)
    ax1.set_xlim([-5, 5])
    ax1.set_ylim([-6, 6])
    ax2.set_xlim([-5, 5])
    ax2.set_ylim([-6, 6])
    fig.set_size_inches(10, 5)
    ax1.grid()
    ax2.grid()
    ax1.plot([-4.1, -4.1], [-5.85, 5.85], 'b--', lw=1)
    ax1.plot([4.1, 4.1], [-5.85, 5.85], 'b--', lw=1)
    ax1.plot([-4.1, 4.1], [5.85, 5.85], 'b--', lw=1)
    ax1.plot([-4.1, 4.1], [-5.85, -5.85], 'b--', lw=1)
    ax1.plot([-4.1, 4.1], [0, 0], c='0.50', lw=1.25)
    ax1.plot([0, 0], [-5.85, 5.85], c='0.50', lw=1.25)
    ax2.plot([-4.1, -4.1], [-5.85, 5.85], 'b--', lw=1)
    ax2.plot([4.1, 4.1], [-5.85, 5.85], 'b--', lw=1)
    ax2.plot([-4.1, 4.1], [5.85, 5.85], 'b--', lw=1)
    ax2.plot([-4.1, 4.1], [-5.85, -5.85], 'b--', lw=1)
    ax2.plot([-4.1, 4.1], [0, 0], c='0.50', lw=1.25)
    ax2.plot([0, 0], [-5.85, 5.85], c='0.50', lw=1.25)
    fig.subplots_adjust(wspace=None, hspace=None)
    fig.suptitle(f'{stage} SEBT Test')
    ax1.set_title(
        f'Non-Operative Leg CofM Deviations', fontsize=10)
    ax2.set_title(
        f'Operative Leg CofM Deviations', fontsize=10)
    ax1.set_xlabel('CofM X Coordinate (cm)')
    ax1.set_ylabel('CofM Y Coordinate (cm)')
    ax2.set_xlabel('CofM X Coordinate (cm)')
    ax2.set_ylabel('CofM Y Coordinate (cm)')
    stage = stage.replace(" ", "_")
    fig.savefig(f'CofM_images/{stage}_CofM_Deviations', dpi=300)


def plot_SEBT_graph(op_leg_data: list[float], nonop_leg_data: list[float], stage: str) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_ylim([0, 170])
    ax2.set_ylim([0, 170])
    ax1.grid()
    ax2.grid()
    fig.set_size_inches(12, 5)
    num1 = len(op_leg_data)
    num2 = len(nonop_leg_data)

    x_values_op = (np.arange(0, num1)*0.150+0).tolist()
    x_values_nonop = (np.arange(0, num2)*0.150+0).tolist()

    x_index_nonop = nonop_leg_data.index(max(nonop_leg_data))
    x_index_op = op_leg_data.index(max(op_leg_data))
    annotation_nonop = (x_values_nonop[x_index_nonop], max(nonop_leg_data))
    annotation_op = (x_values_op[x_index_op], max(op_leg_data))

    ax2.plot(x_values_op, op_leg_data)
    ax1.plot(x_values_nonop, nonop_leg_data)
    ax1.set_title(
        f'Non-Operative Leg Knee Angles', fontsize=10)
    ax2.set_title(
        f'Operative Leg Knee Angles', fontsize=10)
    ax1.set_xlabel("Time (s)")
    ax2.set_ylabel("Knee Flexion Angle (°)")
    ax2.set_xlabel("Time (s)")
    ax1.set_ylabel("Knee Flexion Angle (°)")
    ax1.annotate(f'max angle: {annotation_nonop[1]}°', xy=annotation_nonop)
    ax2.annotate(f'max angle: {annotation_op[1]}°', xy=annotation_op)
    ax1.plot(annotation_nonop[0], annotation_nonop[1], color='red',
             label='original', marker='o', markersize=4)

    ax2.plot(annotation_op[0], annotation_op[1], color='red',
             label='original', marker='o', markersize=4)

    fig.suptitle(f'{stage} SEBT Test')
    stage = stage.replace(" ", "_")
    fig.savefig('sebt/'+stage+'_SEBT_KneeAngles.png', dpi=300)


# plot_SEBT_graph([3, 90, 3], [2, 98, 2], 'Anterior Non-Operative')
