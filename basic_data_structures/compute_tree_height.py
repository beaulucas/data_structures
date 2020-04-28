# python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeHeight:
  # example data
  # 5
  # 0  1 2 3 4 <- labels (indices)
  # 4 -1 4 1 1 <- parents
  # find the root
  # then find children of the root
  # then fild children of the children
  # then find children of the children
  # root is parent[1] +1
  # we find (3,4) children are indices where == 1 +1
  # we find no child for 3, children for 4 where indices in [3, 4] +1
  # no children for 0 or 2
  # height = 3
  # [0: 4]
  # [1: -1] <- root
  # [2: 4]
  # [3: 1]
  # [4: 1]
  # [1: -1] <- root
  # [
  def read(self):
    self.n = int(sys.stdin.readline())
    self.nodes = list(map(int, sys.stdin.readline().split()))

  def test_read(self, n, nodes):
    self.n = n
    self.nodes = nodes

  def tree_print(self):
    print(self.n, self.nodes)

  # parents[0] finds the parent of 0-node, which is 4
  # parents[4] finds parent of 4-node, which is 1
  # parents[1] finds parent of 1-node, which is -1, the root

  def build_tree(self):
    children = [None] * len(self.nodes)
    # for each node, find children so we can access it fast
    for child_index in range(0, len(self.nodes)):
      parent_index = self.nodes[child_index]
      if parent_index == -1:
        root = child_index  # finds node with -1 value and assigns it as root
      else:
        if children[parent_index] is None:
          children[parent_index] = [child_index]
        else:
          children[parent_index].append(child_index)
    if root is None:
      return 0
    else:
      print(children)
      return children

  def compute_height(self):
    children = self.build_tree()
    depth = sum(x is not None for x in children) + 1
    return depth

  def compute_height2(self):
    children = self.build_tree()
    # loop through nodes and find depth
    for child in children:
      for each_child in child:
        pass

    depth = sum(x is not None for x in children) + 1
    return depth

  def find_child(self, parent):
    # we found index 1 has the parent of root
    # now find which indices have value 1
    children = [i for i, val in enumerate(self.parent) if val == parent]
    print(children)

  def calculate_height(self):
    # find child of root, which are 3,4
    # find children of 3 and 4

    # find children of root index, then find the max height of left and right children
    children = [i for i, val in enumerate(parents) if val == root]

    for child in children:
      calculate_height(children)
    # if we find children, return 1
    cur_children = [i for i, val in enumerate(parents) if val == root]
    for child in cur_children:
      pass


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())


threading.Thread(target=main).start()
