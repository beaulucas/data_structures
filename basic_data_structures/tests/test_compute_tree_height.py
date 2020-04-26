from basic_data_structures.compute_tree_height import TreeHeight


def test_answer():
  tree = TreeHeight()
  tree.test_read(5, [4, -1, 4, 1, 1])
  assert tree.compute_height() == 3
  tree.test_read(5, [-1, 0, 4, 0, 3]) == 4
  assert tree.compute_height() == 4
