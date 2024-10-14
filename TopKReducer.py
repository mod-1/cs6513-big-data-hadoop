import sys
import heapq

min_heap = []
def read_mapper_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split(separator, 1)


def main():
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin)
    for line in data:
        word, count = line[1].rsplit('#', 1)
        heapq.heappush(min_heap, (int(count), word))
        if len(min_heap) > 10:
            heapq.heappop(min_heap)


# how to test locally in bash/linus: cat  | python mapper.py
if __name__ == "__main__":
    main()
    k_largest = 10 if len(min_heap) > 10 else len(min_heap)
    for count, word in  heapq.nlargest(k_largest, min_heap):
        print("%s%s%d" % (word, '\t', count))

