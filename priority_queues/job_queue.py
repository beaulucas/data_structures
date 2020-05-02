# python3
from heapq import heappush, heappop


def assign_jobs(n_workers, jobs):
  """
  With `n` independent threads, process `m` jobs of varying times. Ensure that the thread who
  is next to finish job and/or has lowest index takes the job. Print out the index of the worker
  and the time in which they started a job.
  :param n_workers: number of workers to process jobs
  :param jobs: a list of jobs in which value is the time the job will take to complete
  :return: min-heap which is a list of lists ["time when job will finish", "index of worker"]
  """

  hp = []
  for i in range(0, n_workers):
    heappush(hp, [0, i])

  current_time = 0
  for i in range(len(jobs)):
    pop = heappop(hp)
    if current_time < pop[0]:
      current_time = pop[0]
    pop[0] = current_time + jobs[i]  # time at which task will complete

    print(pop[1], current_time)
    heappush(hp, pop)

  return hp


def main():
  n_workers, n_jobs = map(int, input().split())
  jobs = list(map(int, input().split()))
  assert len(jobs) == n_jobs

  assign_jobs(n_workers, jobs)


if __name__ == "__main__":
  main()
