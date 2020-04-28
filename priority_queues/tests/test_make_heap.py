from priority_queues.make_heap import *
import random


def test_answer():
  arr = [5, 4, 3, 2, 1]
  swaps = build_heap(arr)
  assert len(swaps) <= 4 * len(arr)


def stress_test():
  n = 100000
  max_arr = random.sample(range(0, pow(10, 9) + 1), n)
  swp = build_heap(max_arr)
  assert len(swp) <= 4 * len(max_arr)
  # descending list
  swp = build_heap(sorted(max_arr, reverse=True))
  assert len(swp) <= 4 * len(max_arr)
