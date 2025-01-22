import matplotlib.pyplot as plt
import numpy as np
import logging
import time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class PlotLines:
    def __init__(self, range: tuple[int, int] = (0, 10), amount: int = 250) -> None:
        self.sameple_set = np.random.uniform(range[0], range[1], size=(amount, 4))
        fig, (self.ax1, self.ax2) = plt.subplots(1, 2)

        self.ax1.set_title("All Lines")
        self.ax1.set_xlim(0, 10)
        self.ax1.set_ylim(0, 10)

        self.ax2.set_title("Filtered Lines")
        self.ax2.set_xlim(0, 10)
        self.ax2.set_ylim(0, 10)

    def filter(self, range: tuple[tuple[int, int], tuple[int, int]]) -> None:
        self.filtered_data = []

        x1, y1 = range[0]
        x2, y2 = range[1]

        start = time.time()

        for tmp_x1, tmp_y1, tmp_x2, tmp_y2 in self.sameple_set:
            if not (x1 <= tmp_x1 <= x2 and y1 <= tmp_y1 <= y2 and
                    x1 <= tmp_x2 <= x2 and y1 <= tmp_y2 <= y2):
                continue

            self.filtered_data.append([tmp_x1, tmp_y1, tmp_x2, tmp_y2])

        end = time.time()

        logger.info("Used time is %f", end - start)

    def plot(self) -> None:
        for x1, y1, x2, y2 in self.sameple_set:
            self.ax1.plot([x1, x2], [y1, y2])

        for x1, y1, x2, y2 in self.filtered_data:
            self.ax2.plot([x1, x2], [y1, y2])

        plt.show()


if __name__ == "__main__":
    pl = PlotLines(amount=250)
    pl.filter(((5, 0), (10, 10)))
    pl.plot()
