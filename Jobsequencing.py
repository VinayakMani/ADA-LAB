# WAP to represent data required for "Job Sequencing with Deadlines" using dataclass
class Data:

  def data(self, n, deadline, jobs):
    # max number of jobs you can schedule is the max deadline available.
    filledJobs = ['dummy']*max(deadline);
    i = 0
    # start assigning the jobs in a greeedy way
    while i < n:
        job = jobs[i]
        j = deadline[i]
        # assign the job from the last deadline
        while j > 0:
            if(filledJobs[j-1] == 'dummy'):
                filledJobs[j-1] = job
                break
            j = j - 1
        i = i + 1

    return filledJobs

def main():
   sins = Data()
   n = 4
   deadline = [1,3,2,2]
   # assuming jobs are sorted w.r.t  profits
   jobs = ['a', 'b', 'c', 'd']

   sjobs = sins.data(n, deadline, jobs)
   print (sjobs)  

if __name__ == "__main__":
  main()