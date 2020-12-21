from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):

    def test_list_str(self):
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_empty_args(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_not_in_result(self):
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        self.assertNotIn(('Moscow', [1, 0, 0]), actual)

    def test_empty_list(self):
        actual = fit_transform([])
        expected = []
        self.assertEqual(actual, expected)
        
