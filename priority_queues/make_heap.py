# python3

def build_heap(data):
  """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
  # The following naive implementation just sorts the given sequence
  # using selection sort algorithm and saves the resulting sequence
  # of swaps. This turns the given array into a heap, but in the worst
  # case gives a quadratic number of swaps.
  #
  # TODO: replace by a more efficient implementation
  # return a min-heap
  # convert 5 4 3 2 1 into 1 2 3 5 4

  data = [5, 4, 3, 2, 1]
  size = len(data)

  def parent(node_index):
    if node_index == 0:
      return None
    else:
      index = node_index - 1 // 2
      assert 0 <= index <= size - 1
      return index

  def left_child(node_index):
    index = 2 * node_index + 1
    if 0 <= index <= size - 1:
      return index
    else:
      return None

  def right_child(node_index):
    index = 2 * node_index + 2
    if 0 <= index <= size - 1:
      return index
    else:
      return None

  def sift_down(node_index):
    max_index = node_index
    left = left_child(node_index)
    right = right_child(node_index)

# checking tree structure
  for node_index, priority in enumerate(data):
    print(f"index: {node_index}, priority: {priority}")
    print(f"parent: {parent(node_index)}")
    print(f"left child: {left_child(node_index)}")
    print(f"right child: {right_child(node_index)}")

  def sift_down(node_index):
    min_index = node_index
    left_index = left_child(node_index)
    right_index = right_child(node_index)
    # find smallest of two children
    if data[left_index] < data[min_index]:
      min_index = left_index
    if data[right_index] < data[min_index]:
      min_index = right_index
    # now swap
    if node_index != min_index:
      data[node_index], data[min_index] = data[min_index], data[node_index]



  swaps = []
  for i in range(len(data)):
    for j in range(i + 1, len(data)):
      if data[i] > data[j]:
        swaps.append((i, j))
        data[i], data[j] = data[j], data[i]
  return swaps


def main():
  n = int(input())
  data = list(map(int, input().split()))
  assert len(data) == n

  swaps = build_heap(data)

  # print(len(swaps))
  #for i, j in swaps:
  #  print(i, j)


if __name__ == "__main__":
  main()
