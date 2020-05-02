from priority_queues.job_queue import assign_jobs


def test_answer():
  n_workers = 1
  jobs = [1, 2, 3, 4, 5]
  hp = assign_jobs(n_workers, jobs)
  assert hp[0][0] == sum(jobs)

  n_workers = 10
  hp = assign_jobs(n_workers, jobs)
  for i in hp:
    assert i[0] <= jobs[-1]

  n_workers = pow(10, 2)
  jobs = [pow(10, 9)] * pow(10, 5)
  try:
    hp = assign_jobs(n_workers, jobs)
  except OverflowError:
    print("Overflow")
  assert len(hp) == n_workers
