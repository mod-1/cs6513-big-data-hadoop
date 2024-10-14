# PLEASE READ THE README FILE FOR INSTRUCTIONS ON HOW TO RUN THE CODE!
import sys

def read_reducer_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    # input comes from STDIN (standard input)
    s = sys.maxsize.bit_length()
    key = "glob-ord"
    data = read_reducer_output(sys.stdin)

    for line in data:
        word, count = line
        print("%s%s%s%s%s" % (key, separator, int(count), separator, word))

# how to test locally in bash/linus: cat  | python mapper.py
if __name__ == "__main__":
    main()

