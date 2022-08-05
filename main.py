from analysis import Loader
from analysis import MovementAnalyzer


loader = Loader()
loader.load(learning=True)
lexie_test = loader.subjects["lexietest"]
movement_analyzer = MovementAnalyzer()
n = 18
x, y = movement_analyzer.load_xy(lexie_test, trial_number=n)
movement_analyzer.draw(n, x, y)


