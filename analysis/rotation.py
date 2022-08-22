import numpy as np
from math import cos, sin
class RotationData:
    def __init__(self, trial_name, trial_number, trial_time, rotation):
        self.trial_time = trial_time
        self.trial_name = trial_name
        self.trial_number = trial_number
        self.rotation = rotation

    @staticmethod
    def from_dict(d):
        return RotationData(d["TrialName"], d["Trial"], float(d["Time"]), float(d["Angle"]))

    pass


class RotationAnalyzer:
    def __init__(self, loader):
        self.loader = loader

    def calculate_estimation_error(self, subject_name, trial_number):
        rotation_sequence = self.loader.subjects[subject_name].rotation_sequence
        trial_name = rotation_sequence[trial_number].trial_name
        true_angle = self.loader.trial_configuration.get_true_angle(trial_name)
        estimation_angle = rotation_sequence[trial_number].rotation

        rad_true_angle = np.rad2deg(true_angle)
        rad_estimation_angle = np.rad2deg(estimation_angle)

        v1 = np.array([cos(rad_true_angle), sin(rad_estimation_angle)])
        v2 = np.array([cos(estimation_angle), sin(estimation_angle)])
        v1_u = v1 / np.linalg.norm(v1)
        v2_u = v2 / np.linalg.norm(v2)

        rad_diff = np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
        diff = np.rad2deg(rad_diff)
        return diff
    pass
