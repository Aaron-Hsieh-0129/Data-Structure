import json
import time
import argparse
import heapq

# --- TODO START --- #
# You can define any class or function
# You can import any python standard library : https://docs.python.org/3/library/
# However, you are not allowed to import any libraries other than python standard library, (such as numpy)
# --- TODO END --- #

def solution(json_input):
    # --- TODO START --- #
    # json_sum = [0]

    array = json_input['array']
    k = json_input['topk']
    n = len(array)

    k_sum = []
    k_sum.append(0)
    k_sum.append(array[0])
    for i in range(2, n+1):
        k_sum.append(k_sum[i-1] + array[i-1])

    minHeap = []
    heapq.heapify(minHeap)

    for i in range(1, n+1, 1):
        for j in range(i, n+1, 1):
            tmp = k_sum[j] - k_sum[i-1]
            if len(minHeap) < k:
                heapq.heappush(minHeap, tmp)

            else:
                if minHeap[0] < tmp:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, tmp)

    json_sum = sorted(minHeap, reverse=True)
    # --- TODO END --- #
    return json_sum

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='input_1.json')
    parser.add_argument('--output', default='output_1.json')
    args = parser.parse_args()
    json_input = json.load(open(args.input, "r"))
    t1 = time.time()
    json_output = solution(json_input)
    t2 = time.time()
    json.dump(json_output, open(args.output, "w"))
    print("runtime of %s : %s" % (args.input, t2 - t1))

