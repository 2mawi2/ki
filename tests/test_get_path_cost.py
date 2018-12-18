from unittest import TestCase

from exercises.uniform_cost_search import get_path_cost


class TestGet_path_cost(TestCase):

    def test_get_path_cost_simple(self):
        result = get_path_cost(["S", "A"])
        self.assertEqual(result, 3)

    def test_get_path_cost_two_nodes(self):
        result = get_path_cost(["S", "A", "C"])
        self.assertEqual(result, 5)

    def test_get_path_cost_two_empty(self):
        result = get_path_cost([])
        self.assertEqual(result, 0)

    def test_get_path_cost_two_single(self):
        result = get_path_cost(["S"])
        self.assertEqual(result, 0)

    def test_get_path_cost_not_starting_from_s(self):
        result = get_path_cost(["C", "A"])
        self.assertEqual(result, 2)

    def test_get_path_cost_four_nodes(self):
        result = get_path_cost(["S", "B", "C", "A"])
        self.assertEqual(result, 4)
