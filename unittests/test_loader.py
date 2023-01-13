import unittest
from analysis.loader import load_csv_tolist
from analysis.loader import Loader
from analysis.movement import Shortcuts


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

    def test_csv_read(self):
        string_wall_info = load_csv_tolist("../extra/walls_1.csv")
        walls = []
        for pair in string_wall_info:
            if len(pair) < 2:
                continue
            x = int(pair[0])
            y = int(pair[1])
            walls.append((x, y))
        self.assertIn((10, 6), walls)

    def test_shortcut(self):
        loader = Loader(data_dir="../data", extra_dir="../extra")
        loader.load(learning=True)
        self.assertEqual(loader.shortcuts.get_shortcut("Mailbox", "Telescope"), 4)

    def test_trial_configuration(self):
        loader = Loader(data_dir="../data", extra_dir="../extra")
        loader.load(learning=True)
        self.assertIsInstance(loader.trial_configuration.configuration["dsp1_02"], dict)
        print(loader.trial_configuration.get_true_angle("dsp1_24"))

    def test_rotation(self):
        loader = Loader(data_dir="../data", extra_dir="../extra")
        loader.load(learning=True)


if __name__ == '__main__':
    unittest.main()
