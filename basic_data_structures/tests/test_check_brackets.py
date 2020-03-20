from basic_data_structures.check_brackets import find_mismatch


def test_answer():
  successes = ["[]", "{}[]", "[()]", "{[]}()", "foo(bar)"]
  for success in successes:
    assert find_mismatch(success) == "Success"
  assert find_mismatch("{") == 1
  assert find_mismatch("{[}") == 3
  assert find_mismatch(("foo(bar[i)")) == 10
  assert find_mismatch("[](()") == 3
