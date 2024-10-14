# README

This file contains the instructions to run the code for assignment 1 along with the explanation of the code. Any references made in the code are also mentioned here.

## Execution

### 2.1

```
mapred streaming -input ds8106-hw1/data -output assign1-2.1-WC -mapper "python WordCountMapper.py" -file WordCountMapper.py -reducer "python WordCountReducer.py" -file WordCountReducer.py
```

```
mapred streaming -input assign1-2.1-WC/ -output assign1-2.1-TK -mapper "python TopKMapper.py" -file TopKMapper.py -reducer "python TopKReducer.py" -file TopKReducer.py
```

### 2.2

```
mapred streaming -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.num.map.output.key.fields=2 -D mapred.text.key.partitioner.options=-k1,1 -D mapred.partitioner.class=org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner -D mapred.text.key.comparator.options=-k2,2nr -input assign1-2.1-WC -output assign1-2.2-Token -mapper "python TokenizerMapper.py" -file TokenizerMapper.py -reducer "python TokenizerReducer.py" -file TokenizerReducer.py
```

## Explanation

### 2.1
Word Count -> The first job is to count how many times a word appears in the text. The code for this part has been taken from the course content with minor modifications. These modfications include text parsing with regex.

Top K -> The second job is to find the top K words that appear in the wordcount output from the first job. The code uses a heap to keep track of the top 10 words for each mapper and outputs them at the end with a hardcoded constant key.
So the output of the mapper at this stage looks as follows:
```
topk    <word>#<count>
```
Now in the reducer we first parse the value and get the word and count fields out. We then use a heap to get the global top 10 words. For this we again use a heap to keep 10 words(maximum) in memory and print them out at the end of the reducer.

### 2.2
Tokenizer -> The input for the tokenizer code is the word count output from the first job in 2.1. We then create the following 3 fields:
```
glob-ord    <count>    <word>
```
The first field is a hardcoded constant key. The second field is the word count. The third field is the word itself. We then use the KeyFieldBasedComparator to sort the output based on the second key field(count) in descending order. We also use the KeyFieldBasedPartitioner to partition the output based on the first key field which is a constant. This is done so that all the words are sent to the same reducer in descending order of word count. We the iteratate over the iterator and print the word with an increasing id.