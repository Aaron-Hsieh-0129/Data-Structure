import numpy as np

f = open("input_4.txt", "w")

for i in range(1, 2001):
	f.writelines("PUSH " + str(i) + "\n")

#np.savetxt("input_4.txt", a, delimiter="")