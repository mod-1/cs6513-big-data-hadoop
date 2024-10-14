import sys
import heapq

min_heap = []
def read_reducer_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split(separator, 1)


def main():
    # input comes from STDIN (standard input)
    data = read_reducer_output(sys.stdin)
    # define it in init method
    for line in data:
        word, count = line
        heapq.heappush(min_heap, (int(count), word))
        if len(min_heap) > 10:
            heapq.heappop(min_heap)

# Make a class called MyReduce
# Make 2 functions: __init__ for initialising and __del__(self) -> this is where we can output the heap stuff


# how to test locally in bash/linus: cat  | python mapper.py
if __name__ == "__main__":
    main()
    k_largest = 10 if len(min_heap) > 10 else len(min_heap)
    key = "topk"
    for count, word in  heapq.nlargest(k_largest, min_heap):
        print("%s%s%s#%d" % (key, '\t', word, count))

