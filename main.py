import numpy as np

from analysis import Loader
from analysis import MovementAnalyzer, RotationAnalyzer

loader = Loader(data_dir='data/2')
loader.load(learning=True, alternative=True)
subject1 = loader.subjects["1031_T3"]
movement_analyzer = MovementAnalyzer(loader)

#rotation_analyzer = RotationAnalyzer(loader)

# excluding = ["PE12LE", "MA14BL_learn_point", "JU11SI", "sa13pe", "CY4GO"]
# excluding=[]

# for n in range(3, 23):
#     err = rotation_analyzer.calculate_estimation_error("lexietest", n)
#     print(f"TrialNumber {n}, estimation error {err}")

#errors = rotation_analyzer.calculate_all_estimation_error_for_all(3, 23, excluding=excluding)

#print(errors["lexietest"][3])  # Print just one subject's error on trial 3
#print(errors["lexietest"])  # Print just one subject's error on all trials

movement_analyzer.plot_all(subject1, 3, 10)

efficiencies = movement_analyzer.calculate_efficiency_for_all(3, 10, reverse_divide=True)

print(efficiencies["1031_T3"][3])  # Print just one subject's error on trial 3
print(efficiencies["1031_T3"])  # Print just one subject's error on all trials

from analysis import Exporter

Exporter.export_efficiency_to_csv(efficiencies, "mean.csv", operation="mean")
