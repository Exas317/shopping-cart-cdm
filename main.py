from datetime import datetime
import math
from multiprocessing import Pool
from multiprocessing import cpu_count
import time

SAMPLE = "Something"

CPU_UTIL = 0.2

def f(x):
	while True:
	    startTime = datetime.now()
	    while (datetime.now() - startTime).total_seconds() < CPU_UTIL:
	        math.factorial(100) # Or any other computation here
	    time.sleep(1-CPU_UTIL)

def main():
	processes = cpu_count()*2
	pool = Pool(processes)
	pool.map(f, range(processes))


if __name__ == '__main__':
	main()
