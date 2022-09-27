
##Important! You shouldn't use statistics library! ("import statistics" is not allowed)

import math
class MinHeap: #Please store and implement MinHeap data structure with an array
    def __init__(self):
        self.array = []
        self.size = 0


    def getSize(self):
        return self.size


    def swap(self, pos1, pos2):
        self.array[pos1], self.array[pos2] = self.array[pos2], self.array[pos1]
        return

    def insert(self, item): #insert new item
    ### TODO ### 
    ### input: a value ###
    ### You need not return or print anything with this function. ###
        self.array.append(item)
        self.size += 1
        if self.size == 1:
            return
        else:
            size = self.size - 1
            while size > 0 and self.array[size] < self.array[int((size-1) / 2)]:
                self.swap(size, int((size-1) / 2))
                size = int((size - 1) / 2)
        return


    def peek(self):  #Find Minimum item
        if self.size == 0:
            return
        else:
            return self.array[0]


    def removeMin(self):
    ### TODO ###
    ### You need not return or print anything with this function. ###
        if self.size == 0:
            return

        elif self.size == 1:
            self.array.pop()
            self.size -= 1
            return

        elif self.size == 2:
            self.swap(0, -1)
            self.array.pop()
            self.size -= 1
            return

        else:
            self.swap(0, -1)
            self.array.pop()
            self.size -= 1

            now = 0
            if now * 2 + 1 < self.size - 1:
                while (self.array[now] > self.array[now * 2 + 1] or self.array[now] > self.array[now * 2 + 2]):
                    if self.array[now * 2 + 1] < self.array[now * 2 + 2]:
                        self.swap(now, now * 2 + 1)
                        now = now * 2 + 1
                        
                    else:
                        self.swap(now, now * 2 + 2)
                        now = now * 2 + 2

                    if now * 2 + 1 >= self.size - 1:
                        break

            # only left
            if now * 2 + 1 == self.size - 1:
                if self.array[now] > self.array[now * 2 + 1]:
                    self.swap(now, now * 2 + 1)
                    now = now * 2 + 1
                return

            # left + right
            if now * 2 + 2 == self.size - 1:
                if self.array[now] > self.array[now * 2 + 1] or self.array[now] > self.array[now * 2 + 2]:
                    if self.array[now * 2 + 1] < self.array[now * 2 + 2]:
                        self.swap(now, now * 2 + 1)
                        now = now * 2 + 1
                        
                    else:
                        self.swap(now, now * 2 + 2)
                        now = now * 2 + 2
                return

            return



    def showMinHeap(self):  #Show MinHeap with array
        return self.array


class MaxHeap: #Please store and implement MinHeap data structure with an array
    def __init__(self):
        self.array = []
        self.size = 0


    def getSize(self):
        return self.size


    def swap(self, pos1, pos2):
        self.array[pos1], self.array[pos2] = self.array[pos2], self.array[pos1]
        return


    def insert(self, item): #insert new item
    ### TODO ###
    ### input: a value ###
    ### You need not return or print anything with this function. ###
        self.array.append(item)
        self.size += 1
        if self.size == 1:
            return
        else:
            size = self.size - 1
            while size > 0 and self.array[size] > self.array[int((size-1) / 2)]:
                self.swap(size, int((size-1) / 2))
                size = int((size - 1) / 2)
        return

    def peek(self):    #Find Maximum item
        if self.size == 0:
            return
        else:
            return self.array[0]


    def removeMax(self):   #Find Maximum item 
    ### TODO ###
    ### You need not return or print anything with this function. ###
        if self.size == 0:
            return

        elif self.size == 1:
            self.array.pop()
            self.size -= 1
            return

        elif self.size == 2:
            self.swap(0, -1)
            self.array.pop()
            self.size -= 1
            return

        else:
            self.swap(0, -1)
            self.array.pop()
            self.size -= 1

            now = 0
            if now * 2 + 1 < self.size - 1:
                while (self.array[now] < self.array[now * 2 + 1] or self.array[now] < self.array[now * 2 + 2]):
                    if self.array[now * 2 + 1] > self.array[now * 2 + 2]:
                        self.swap(now, now * 2 + 1)
                        now = now * 2 + 1
                        
                    else:
                        self.swap(now, now * 2 + 2)
                        now = now * 2 + 2

                    if now * 2 + 1 >= self.size - 1:
                        break

            # only left
            if now * 2 + 1 == self.size - 1:
                if self.array[now] < self.array[now * 2 + 1]:
                    self.swap(now, now * 2 + 1)
                    now = now * 2 + 1
                return

            # left + right
            if now * 2 + 2 == self.size - 1:
                if self.array[now] < self.array[now * 2 + 1] or self.array[now] < self.array[now * 2 + 2]:
                    if self.array[now * 2 + 1] > self.array[now * 2 + 2]:
                        self.swap(now, now * 2 + 1)
                        now = now * 2 + 1
                        
                    else:
                        self.swap(now, now * 2 + 2)
                        now = now * 2 + 2
                return
                
            return


    def showMaxHeap(self):   #Show MaxHeap with array
        return self.array


class FindMedian: 
    def __init__(self):
    ### TODO ###
    ### Your own data structure. Implementing with heap structure is highly recommended. ###
        self.minHeap = MinHeap()
        self.maxHeap = MaxHeap()

    def AddNewValues(self, NewValues):  # Add NewValues(a list of items) into your data structure
    ### TODO ### 
    ### input: a list of values ###
    ### You need not return or print anything with this function. ###
        NewValues = list(map(float, NewValues))

        for num in NewValues:
            if self.maxHeap.size == 0:
                self.maxHeap.insert(num)
                continue


            if self.maxHeap.size == self.minHeap.size:
                maxNum = self.maxHeap.peek()
                if num < maxNum:
                    self.maxHeap.insert(num)
                else:
                    self.minHeap.insert(num)


            elif self.maxHeap.size < self.minHeap.size:
                maxNum = self.maxHeap.peek()
                minNum = self.minHeap.peek()
                if num < maxNum:
                    self.maxHeap.insert(num)
                else:
                    self.minHeap.removeMin()
                    self.maxHeap.insert(minNum)
                    self.minHeap.insert(num)

            else:
                maxNum = self.maxHeap.peek()
                minNum = self.minHeap.peek()
                if num < maxNum:
                    self.maxHeap.removeMax()
                    self.minHeap.insert(maxNum)
                    self.maxHeap.insert(num)
                else:
                    self.minHeap.insert(num)

        return


    def ShowMedian(self):  # Show Median of your data structure
    ### TODO ### 
    ### You need not print anything but "return Median". ###
        if self.maxHeap.size == self.minHeap.size == 0:
            return

        if self.maxHeap.size == self.minHeap.size:
            maxNum = self.maxHeap.peek()
            minNum = self.minHeap.peek()
            return (maxNum + minNum) / 2.

        if self.maxHeap.size < self.minHeap.size:
            minNum = self.minHeap.peek()
            return minNum
        else:
            maxNum = self.maxHeap.peek()
            return maxNum


    def RemoveMedianRelatedValue(self): # Remove value(s) related with median: odd (1), even (2)
    ### TODO ###
    ### You need not return or print anything with this function. ###
        if self.maxHeap.size == self.minHeap.size == 0:
            return

        if self.maxHeap.size == self.minHeap.size:
            self.maxHeap.removeMax()
            self.minHeap.removeMin()
            return

        if self.maxHeap.size < self.minHeap.size:
            self.minHeap.removeMin()
            return

        else:
            self.maxHeap.removeMax()
            return





