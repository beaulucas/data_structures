# python3

left = ["(", "[", "{"]
right = [")", "]", "}"]


def are_matching(left, right):
  """
  :param left: opening character
  :param right: closing character
  :return: whether or not characters match
  """
  return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
  """
  Find errors in the usage of different types of brackets: {}, (), [].
  If there is an error, print the 1-based index of first unmatched closing bracket.
  If there are no such mistakes, print the 1-based index of first unmatched opening bracket.
  If no mistakes, inform user that usage is correct.

  :param text: string of ASCII characters
  :return: index of error or "Success" if no error
  """

  opening_brackets_stack = []
  for ind, char in enumerate(text):
    if char in "([{":
      if len(opening_brackets_stack) == 0:
        oldest_unmatched_opening = ind
      opening_brackets_stack.append(char)
    if char in ")]}":
      last_unmatched_closing = ind
      try:
        if are_matching(opening_brackets_stack[-1], char):
          opening_brackets_stack.pop()
        else:
          return last_unmatched_closing + 1
      except IndexError:  # if this occurs, it means stack is empty
        return ind + 1

  if len(opening_brackets_stack) == 0:
    return "Success"
  else:
    return oldest_unmatched_opening + 1


def main():
  text = input()
  mismatch = find_mismatch(text)
  print(mismatch)


if __name__ == "__main__":
  main()
