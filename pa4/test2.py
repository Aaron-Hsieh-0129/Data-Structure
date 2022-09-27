import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)  # python的heaqp模块是小根堆，因此要保存大根堆的话需要加上一个负号
            return

        if num > -self.max_heap[0]:
            heapq.heappush(self.min_heap, num)
            if len(self.max_heap) + 1 < len(self.min_heap):
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))  # 插入大根堆需要给值加负号
        else:
            heapq.heappush(self.min_heap, -num)
            if len(self.max_heap) > len(self.min_heap) + 1:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))  # 弹出大根堆堆顶的时候需要加负号变为正数

    def findMedian(self):
        if len(self.max_heap) > len(self.min_heap):   # 大根堆元素多一个，中位数是大根堆堆顶
            return -self.max_heap[0]
        if len(self.max_heap) < len(self.min_heap):   # 小根堆元素多一个，中位数是小根堆堆顶
            return self.min_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0])/2  # 大小跟堆元素一样多，则中位数是两者堆顶之和除以2

M = MedianFinder()
a = list(range(999999))
for i in a:
	M.addNum(i)

print(M.findMedian())