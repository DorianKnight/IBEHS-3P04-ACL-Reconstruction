import matplotlib
import matplotlib.pyplot as plt
import numpy as np


sample_data = [0, 0, 0, 0, 1, 4, 4, 5, 6, 8, 9, 20, 40, 40, 50, 53, 57, 80, 85, 89, 90, 91, 100, 110,
               115, 120, 130, 135, 141, 145, 147, 120, 100, 80, 70, 71, 40, 30, 20, 14, 15, 13, 10, 6, 2, 1, 0, 0, 0]


def plot_SEBT_graph(SEBT_data: list[float], stage: str) -> None:
    num = len(SEBT_data)
    x_values = np.arange(0, num)*0.150+0
    plt.plot(x_values, SEBT_data)
    plt.xlabel("Time (s)")
    plt.ylabel("Knee Flexion Angle (°)")
    plt.title(stage + " Portion of SEBT Test Knee Angle")
    plt.show()


#plot_SEBT_graph(sample_data, 'Anterolateral')
