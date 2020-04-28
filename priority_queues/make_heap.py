# python3


def build_heap(data):
  """
  Take a list of distinct integers and convert them into a binary min-heap structure.
  :param data: A list of distinct integers
  :return: The number of swaps needed to turn it into a min-heap.
  """

  size = len(data)

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
    min_index = node_index
    left_index = left_child(node_index)
    right_index = right_child(node_index)

    has_children = True if left_index is not None else False
    if has_children:
      if data[left_index] < data[min_index]:
        min_index = left_index
      if right_index is not None:
        if data[right_index] < data[min_index]:
          min_index = right_index

    # swap if needed
    if node_index != min_index:
      data[node_index], data[min_index] = data[min_index], data[node_index]
      swaps.append(f"{node_index} {min_index}")
      sift_down(min_index)

  swaps = []
  for i in reversed(range(0, len(data) // 2)):
    sift_down(i)

  return swaps


def main():
  n = int(input())
  data = list(map(int, input().split()))
  assert len(data) == n
  swaps = build_heap(data)
  assert len(swaps) <= 4 * n
  print(len(swaps))
  for swap in swaps:
    print(swap)


if __name__ == "__main__":
  main()
