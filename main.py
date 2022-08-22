from analysis import Loader
from analysis import MovementAnalyzer, RotationAnalyzer


loader = Loader()
loader.load(learning=True)
lexie_test = loader.subjects["lexietest"]
movement_analyzer = MovementAnalyzer(loader)
rotation_analyzer = RotationAnalyzer(loader)

for n in range(3, 23):
    err = rotation_analyzer.calculate_estimation_error("lexietest", n)
    print(f"TrialNumber {n}, estimation error {err}")
    x, y = movement_analyzer.load_xy(lexie_test, trial_number=n)
    movement_analyzer.draw(n, x, y)




