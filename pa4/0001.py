import Median
if __name__== '__main__':
	with open("0001.txt", "w") as output:
		heap1 = Median.MinHeap()
		heap2 = Median.MaxHeap()
		a = list(range(1000))
		for i in a:
			heap1.insert(i)
			for n in heap1.showMinHeap():
				output.write(str(n) + " ")
			output.write("\n")
		heap1.removeMin()
		for n in heap1.showMinHeap():
			output.write(str(n) + " ")
		output.write("\n")
		for i in a:
			heap2.insert(i)
			for n in heap2.showMaxHeap():
				output.write(str(n) + " ")
			output.write("\n")
