import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeHeight:
  def height(self, node):
    if node == -1:
      return 0
    if self.parent[node] in self.heights:
      self.heights[node] = self.heights[self.parent[node]] + 1
    else:
      self.heights[node] = self.height(self.parent[node]) + 1
    return self.heights[node]

  def read(self):
    self.n = int(sys.stdin.readline())
    self.parent = list(map(int, sys.stdin.readline().split()))
    self.heights = {}

  def compute_height(self):
    maxHeight = 0
    for vertex in range(self.n):
      maxHeight = max(maxHeight, self.height(vertex))
    return maxHeight


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())


threading.Thread(target=main).start()
