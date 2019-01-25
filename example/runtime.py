import numpy as np
from example import algs

runtimes = [] # (size, trial, alg, assignments, conditionals) tuples

N_TRIALS = 100
SIZES = range(100, 1001, 100)
for size in SIZES:
	print(size)
	for trial in range(N_TRIALS):
		x = np.random.randint(0, size, size)
		for alg in algs.bubblesort_core, algs.quicksort_core:
			runtimes.append((size, trial, alg.__name__,) + alg(x)[1:])

with open("runtimes.txt", "w") as runtimeF:
	for line in runtimes:
		runtimeF.write("\t".join(map(str, line)) + "\n")