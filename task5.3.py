def quick_sort(arr):
    if len(arr)<=1:
        return arr

    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]

    return quick_sort(left) + middle + quick_sort(right)

import unittest
import random

class TestQuickSort(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(quick_sort([]), [])

    def test_single(self):
        self.assertEqual(quick_sort([5]), [5])

    def test_sorted(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse(self):
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(quick_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3])

    def test_random(self):
        random.seed(42)
        for _ in range(5):
            arr = [random.randint(-50, 50) for _ in range(10)]
            self.assertEqual(quick_sort(arr), sorted(arr))

    def test_negative(self):
        self.assertEqual(quick_sort([-3, -1, -4, -2]), [-4, -3, -2, -1])


if __name__=='__main__':
    unittest.main()