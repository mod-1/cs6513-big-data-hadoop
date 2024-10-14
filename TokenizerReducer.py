# PLEASE READ THE README FILE FOR INSTRUCTIONS ON HOW TO RUN THE CODE!
import sys

def read_reducer_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split(separator, 2)


def main():
    # input comes from STDIN (standard input)
    id = 1
    data = read_reducer_output(sys.stdin)

    for line in data:
        key, count, word = line
        print("%d%s%s" % (id, ',', word))
        id += 1


# how to test locally in bash/linus: cat  | python mapper.py
if __name__ == "__main__":
    main()

