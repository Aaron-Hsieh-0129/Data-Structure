import heapq as hq
if __name__== '__main__':
	with open("test.txt", "w") as output:
		# heap1 = Median.MinHeap()
		# heap2 = Median.MaxHeap()
		heap1 = []
		heap2 = []
		a = [1, 2, 3, 4, 5, 6,12, 5]
		for i in a:
			hq.heappush(heap1, i)
			for n in heap1:
				output.write(str(n) + " ")
			output.write("\n")
		hq.heappop(heap1)
		for n in heap1:
			output.write(str(n) + " ")
		output.write("\n")

		for i in a:
			hq.heappush(heap2, -i)
			for n in heap2:
				output.write(str(-n) + " ")
			output.write("\n")
