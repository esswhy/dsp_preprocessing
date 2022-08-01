from analysis import Loader
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches

loader = Loader()
loader.load()
# H11 W11
# TopLeft 0.5, 225
# TopRight 227 225
# BottomLeft 0.5 -1
# BottomRight 227 -1
# for key, value in subjects.movement_sequence.items():

origin = np.array([0.5, -1])


def offset_to_origin(pos):
    return pos - origin


def get_block_pos(pos):
    return np.floor(offset_to_origin(pos) / 20.6)+np.array([1, 1])


lexie_test = loader.subjects["lexietest"]
path = []
last_moved_pos = np.zeros(2)
n = 3
for move in lexie_test.movement_sequence[n]:
    current_pos = get_block_pos(move.get_vector())
    if np.array_equal(last_moved_pos, current_pos):
        continue
    path.append(current_pos)
    last_moved_pos = current_pos

arr = np.array(path)
X = (arr[:, 0])-0.5
Y = (arr[:, 1])-0.5
fig, ax = plt.subplots()

# Draw step lines
ax.step(X, Y)

plt.autoscale(False)
# Draw background
bg = mpimg.imread("images/maze1.png")
plt.imshow(bg, extent=[0, 11, 0, 11])

plt.title("Trial %d Distance: %d" % (n, len(X)))
plt.xticks(np.arange(0, 12, step=1))
plt.yticks(np.arange(0, 12, step=1))
plt.grid()
plt.show()

