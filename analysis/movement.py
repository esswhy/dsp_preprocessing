import numpy as np
from analysis.grid import Grid
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches


# H11 W11
# TopLeft 0.5, 225
# TopRight 227 225
# BottomLeft 0.5 -1
# BottomRight 227 -1
# for key, value in subjects.movement_sequence.items():

class MovementData:
    def __init__(self, trial_name, trial_number, trial_time, x, y, rotation):
        self.y = y
        self.x = x
        self.trial_time = trial_time
        self.trial_name = trial_name
        self.trial_number = trial_number
        self.rotation = rotation

    def get_vector(self):
        return np.array([float(self.x), float(self.y)])

    @staticmethod
    def from_str(s=""):
        elements = [element.strip() for element in s.split(",")]
        if len(elements) < 6:
            return None
        return MovementData(elements[0], elements[1], elements[2], elements[3], elements[4], elements[5])


class MovementAnalyzer:
    def __init__(self, origin=np.array([0.6, -1.1]), map_actual_size=np.array([226, 226]), grid_size=np.array([11, 11])):
        self.grid = Grid(origin=origin, map_actual_size=map_actual_size, grid_size=grid_size)
        pass

    def load_xy(self, subject, trial_number):
        path = []
        last_moved_block = np.zeros(2)
        for move in subject.movement_sequence[trial_number]:
            current_pos = self.grid.get_block_pos(move.get_vector())
            if np.array_equal(last_moved_block, current_pos):
                continue
            # Check offset
            offset = current_pos - last_moved_block
            if offset.dot(offset) != 1:
                path.append(current_pos)

            path.append(current_pos)
            last_moved_block = current_pos
            if np.array_equal(current_pos, np.array([7,1])):
                print("Corner case")
            print(current_pos)

        arr = np.array(path)
        x = (arr[:, 0]) - 0.5
        y = (arr[:, 1]) - 0.5
        return x, y

    def draw(self, n, x, y, bg_file="images/maze1.png", ):

        fig, ax = plt.subplots()
        ax.step(x, y)

        plt.autoscale(False)
        bg = mpimg.imread(bg_file)
        plt.imshow(bg, extent=[0, self.grid.grid_size[0], 0, self.grid.grid_size[1]])

        plt.title("Trial %d Distance: %d" % (n, len(x)))
        plt.xticks(np.arange(0, self.grid.grid_size[0]+1, step=1))
        plt.yticks(np.arange(0, self.grid.grid_size[1]+1, step=1))
        plt.grid()
        plt.show()
