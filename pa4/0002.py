import Median
if __name__== '__main__':
	with open("0002.txt", "w") as output:
		a = list(range(999999))
		M = Median.FindMedian()
		M.AddNewValues(a)
		output.write(str(M.ShowMedian()) + "\n")
		M.RemoveMedianRelatedValue()
		output.write(str(M.ShowMedian()))
