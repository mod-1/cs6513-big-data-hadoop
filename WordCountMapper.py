import sys
import re


def read_input(input):
    for line in input:
        # split the line into words; keep returning each word
        cleaned_text = re.sub(r'[^A-Za-z0-9,.\-\(\)\[\]]+', ' ', line) # remove all characters except A-Z, a-z, 0-9, comma, period, hyphen, parentheses, and brackets
        cleaned_text = re.sub(r'([.,-])', r' \1 ', cleaned_text) # add space before and after comma, period, and hyphen
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip() # remove extra spaces
        yield cleaned_text.split()


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)

    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # space-delimited; the trivial word count is 1
        for word in words:
            word= word.strip()
            if len(word) == 0:
                continue
            else:
                print('%s%s%d' % (word, separator, 1))


# how to test locally in bash/linus: cat  | python mapper.py
if __name__ == "__main__":
    main()
