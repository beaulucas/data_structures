# python3

from collections import namedtuple


# n threads, indexed from 0
# m jobs

# m jobs, the times in seconds it takes any thread to process i-th job


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
      sift_down(min_index)

  for i in reversed(range(0, len(data) // 2)):
    sift_down(i)

  return data

def assign_jobs(n_workers, jobs):
    """
    With N threads, process M jobs. Output M lines. Each line should contain two integers:
    The index of the thread which will process i-th job, and the time in seconds when it will start processing
    that job.
    :param n_workers:
    :param jobs:
    :return:
    """
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


class Threads:
    def __init__(self, n=1, busy=False, time_left=0):
        self.n = n
        self.busy = [busy] * self.n
        self.time_left = [time_left] * self.n


def assign_jobs2(n_workers, jobs):

    threads = Threads(n=n_workers)
    thread_indices = list(range(0, n_workers))
    jobs_taken = 0
    time_index = 0
    threads2 = namedtuple("threads", ["thread_index", "time_left"])
    thr = []
    for i in range(0,5):
        thr.append(threads2(i, 0))
    print(thr)
    sorted(thr, key=lambda x: x.time_left)

    AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

    # first time, assign in order
    while jobs_taken < len(jobs):
        if jobs_taken == 0:
            for ind, val in enumerate(threads.time_left):
                threads.time_left[ind] = jobs[ind]
                threads.busy[ind] = True
                thread_indices
                jobs_taken +=1
                print(f"thread index: {ind}, current time: {time_index}")
       #print(f"Jobs taken: {jobs_taken}, jobs left: {len(jobs) - jobs_taken}")
        # increment by job that will finish fastest
        time_index += threads.time_left[0]
        time_left = threads.time_left[0]
        #print(f"Current time: {time_index}")
        for ind, val in enumerate(threads.time_left):
            # check if any threads are now at 0
            threads.time_left[ind] -= time_left
            #print(f"Checking out index {ind} which has time left: {threads.time_left[ind]}")
            if threads.time_left[ind] == 0:
                threads.busy[ind] = False
                #print(f"A job finished at time {time_index} at index {ind}! Adding new job with time to take {jobs[jobs_taken]}")
                threads.time_left[ind] = jobs[jobs_taken]
                jobs_taken += 1
                print(f"thread index: {ind}, current time: {time_index}")
            else:
                pass
                #print(f" index {ind} has {threads.time_left[ind]}")
        threads.time_left = build_heap(threads.time_left)
        #print(f"Rebuilt heap: {threads.time_left}")

            # print(f"New jobs at each thread {threads.time_left}")
        #print(f"Thread processes: {threads.time_left}")

def assign_jobs3(n_workers, jobs):

   # n_workers = [0, 1]
   # jobs = [1,2,3,4,5]
    jobs_taken = 0
    time_index = 0
    x = []
    for i in range(0, n_workers):
        x.append([i, time_index])
    threads2 = namedtuple("threads", ["thread_index", "time_left"])
    thr = []

    #print(thr)
    sorted(thr, key=lambda x: x.time_left)

    # first time, assign in order
    while jobs_taken < len(jobs):
        if jobs_taken == 0:
            for i, val in enumerate(x):
                x[i][1] = jobs[i]
                print(f"{x[i][0]} {time_index}")
                jobs_taken += 1
       #print(f"Jobs taken: {jobs_taken}, jobs left: {len(jobs) - jobs_taken}")
        # increment by job that will finish fastest
        time_index += x[0][1]
        time_left = x[0][1]
        #print(f"Current time: {time_index}")
        for i, val in enumerate(x):
            if jobs_taken == len(jobs):
                break
            # check if any threads are now at 0
            x[i][1] -= time_left
            #print(f"Checking out index {ind} which has time left: {threads.time_left[ind]}")
            if x[i][1] == 0:
                x[i][1] = jobs[jobs_taken]
                jobs_taken += 1
                print(f"{x[i][0]} {time_index}")
            else:
                pass
                #print(f" index {ind} has {threads.time_left[ind]}")
        x.sort(key=lambda x: x[1])
        #print(f"Rebuilt heap: {threads.time_left}")

            # print(f"New jobs at each thread {threads.time_left}")
        #print(f"Thread processes: {threads.time_left}")



def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    jobs = build_heap(jobs)
    print(jobs)
    assert len(jobs) == n_jobs



    assign_jobs3(n_workers, jobs)

if __name__ == "__main__":
    main()
