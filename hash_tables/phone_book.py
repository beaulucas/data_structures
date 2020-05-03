# python3


class Query:
  def __init__(self, query):
    self.type = query[0]
    self.number = int(query[1])
    if self.type == "add":
      self.name = query[2]


def read_queries():
  """
  Takes a number of queries `n`, query text, and generates list of Query objects.
  :return: list of Query objects of length `n`
  """
  n = int(input())
  return [Query(input().split()) for i in range(n)]


def write_responses(result):
  """
  Prints result of query operations, each on new line.
  :param result:
  :return:
  """
  print("\n".join(result))


def process_queries(queries):
  """
  Takes in a list of Query objects and performs operations on a phone book dict object.
  :param queries: List of Query objects
  :return: list of query results
  """
  result = []
  phone_dict = {}
  for query in queries:
    if query.type == "add":
      phone_dict[query.number] = query.name
    elif query.type == "find":
      result.append(phone_dict.get(query.number, "not found"))
    elif query.type == "del":
      if phone_dict.get(query.number) is None:
        pass
      else:
        del phone_dict[query.number]
  return result


if __name__ == "__main__":
  queries = read_queries()
  result = process_queries(queries)
  write_responses(result)
