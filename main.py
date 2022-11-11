import numpy as np

from analysis import Loader
from analysis import MovementAnalyzer, RotationAnalyzer

loader = Loader()
loader.load(learning=True)
lexie_test = loader.subjects["lexietest"]

# loader.subjects contains Subject object which named after the data folder(e.g. lexietest)
# Subject contains movement_sequence, rotation_sequence (and meta)
# both are dictionary with trial_number as key
# MovementData is the value for each item in movement_sequence, it contains trial_name, trial_number, trial_time (since that trial started), x, y,
# RotationData is the value for each item in rotation_sequence, it contains trial_name, trial_number, trial_time (how much time does that trial take), rotation

# Currently the movement analyzer can only handle normal (not alternative) trials, will add that later this week
movement_analyzer = MovementAnalyzer(loader)

# rotation analyzer gives the absolute angular error for each trial (both normal and alternative)
rotation_analyzer = RotationAnalyzer(loader)

excluding = ["CY4GO", "PE12LE", "MA14BL_learn_point", "JU11SI", "sa13pe"]
# excluding=[]

# for n in range(3, 23):
#     err = rotation_analyzer.calculate_estimation_error("lexietest", n)
#     print(f"TrialNumber {n}, estimation error {err}")

errors = rotation_analyzer.calculate_all_estimation_error_for_all(3, 23, excluding=excluding)

print(errors["lexietest"][3]) # Print just one subject's error on trial 3
print(errors["lexietest"]) # Print just one subject's error on all trials


# Noted that though the trial number is always from 3-23, the starting location and target is different between pointing and wayfinding
# for n in range(3, 23):
#     X, Y = movement_analyzer.load_xy(lexie_test, trial_number=n)
#     movement_analyzer.draw(n, X, Y)
# print(movement_analyzer.calculate_efficiency_all("lexietest"))

efficiencies = movement_analyzer.calculate_efficiency_for_all(excluding=excluding)


print(efficiencies["lexietest"][3]) # Print just one subject's error on trial 3
print(efficiencies["lexietest"]) # Print just one subject's error on all trials



