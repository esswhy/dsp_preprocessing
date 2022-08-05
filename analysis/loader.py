from pathlib import Path
from analysis.subject import Subject
from analysis.movement import MovementData
from analysis.rotation import RotationData

MOVEMENT_FILE = 'movement.csv'
ROTATION_FILE = 'rotation.csv'
TIMEOUT_FILE = 'timeout.txt'
META_FILE = 'meta.txt'


class CorruptedDataError(Exception):
    pass


class InsufficientDataError(Exception):
    pass


class Loader:
    def __init__(self, root_dir='data'):
        self.root_dir = Path(root_dir)
        self.subjects = {}

    def load(self, force=False, learning=False):
        if not self.root_dir:
            return
        # Get participants dirs
        for participant_dir in self.root_dir.iterdir():
            file_paths = {}

            for sub_file in participant_dir.iterdir():
                if sub_file.is_dir():
                    continue
                file_paths[sub_file.name] = sub_file

            if len(file_paths.items()) != 4 and force:
                raise InsufficientDataError("Corrupted file")

            subject = Subject()
            try:
                subject.meta = load_meta(file_paths[META_FILE])
                subject.rotation_sequence = load_meta(file_paths[ROTATION_FILE])
                subject.movement_sequence = load_movement(file_paths[MOVEMENT_FILE], learning=learning)
                # TODO: add timeout here
            except KeyError as e:
                print(e)
                if not force:
                    raise CorruptedDataError("Makesure you have all the filenames correct")

            self.subjects[participant_dir.name] = subject


def load_rotation(path):
    rotation_trials = []
    return rotation_trials


def load_movement(path, learning=False):
    movement_trials = {}
    with path.open("r") as file:
        last_trial_number = 0
        skip_header_line = False
        for line in file:
            maker_pos = line.find("@")
            if skip_header_line:
                skip_header_line = False
                continue
            if line.find("@") != -1:
                last_trial_number = int(line[maker_pos+1:])
                movement_trials[last_trial_number] = []
                skip_header_line = True
            else:
                movement_trials[last_trial_number].append(MovementData.from_str(line))
    if not learning and 99 in movement_trials:
        movement_trials.pop(99)
    return movement_trials


def load_timeout(path):
    pass


def load_meta(path):
    meta_dict = {}
    with path.open("r") as file:
        for line in file:
            pair = [element.strip() for element in line.split(":")]
            if len(pair) != 2:
                continue
            meta_dict[pair[0]] = pair[1]
    return meta_dict
