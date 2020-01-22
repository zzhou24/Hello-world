import multiprocessing as mp
import time
start_time=time.time()
def job(x):
    return x*x+x*x*x

def multicore():
    pool = mp.Pool(processes=90)
    res = pool.map(job, range(50000))
    return res
if __name__ == '__main__':
    final=[]
    for i in range(50000):
        res = job(i)
        final.append(res)
    print(final[-2])
# show how long the program takes    
print(time.time()-start_time)
