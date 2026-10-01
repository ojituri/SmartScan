import unittest

from encoder_reader import EncoderReader


class TestEncoderReader(unittest.TestCase):

    def setUp(self):
        self.encoder = EncoderReader()

    def test_initial_counts(self):
        counts = self.encoder.get_counts()
        self.assertEqual(counts["left"], 0)
        self.assertEqual(counts["right"], 0)

    def test_left_encoder_count(self):
        self.encoder.add_left_pulses(10)
        counts = self.encoder.get_counts()
        self.assertEqual(counts["left"], 10)

    def test_right_encoder_count(self):
        self.encoder.add_right_pulses(15)
        counts = self.encoder.get_counts()
        self.assertEqual(counts["right"], 15)

    def test_both_encoder_counts(self):
        self.encoder.add_left_pulses(20)
        self.encoder.add_right_pulses(30)
        counts = self.encoder.get_counts()
        self.assertEqual(counts["left"], 20)
        self.assertEqual(counts["right"], 30)

    def test_count_accumulation(self):
        self.encoder.add_left_pulses(10)
        self.encoder.add_left_pulses(5)
        counts = self.encoder.get_counts()
        self.assertEqual(counts["left"], 15)

    def test_reset(self):
        self.encoder.add_left_pulses(10)
        self.encoder.add_right_pulses(20)
        self.encoder.reset()
        counts = self.encoder.get_counts()
        self.assertEqual(counts["left"], 0)
        self.assertEqual(counts["right"], 0)

    def test_negative_pulses_rejected(self):
        with self.assertRaises(ValueError):
            self.encoder.add_left_pulses(-1)

        with self.assertRaises(ValueError):
            self.encoder.add_right_pulses(-1)


if __name__ == "__main__":
    unittest.main()
