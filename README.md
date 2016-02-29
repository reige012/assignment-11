# Assignment 11

## Task 1

In the file `c-darwin-chapter-1.txt` is Chapter 1 from Darwin's Origin of Species.  Similar to your previous assignment, write a program to count word usage in the text within this file (you are free to use most/all of that previous code).  Have this program print out, in decreasing order (most common to least common) the 20 most common words and the count of each word used. Your program should contain a `main` loop and an `ifmain` statement, it should be formatted correctly, and you should **use `argparse`** to get the name of the input and output files from the user.  You may use any type of dictionary object in your code.  You should print your Top 20 results to the screen using the `.format()` string method, and your results should be prettily spaced (again, using `.format()`) so that the column of words and word counts are justified left, like so:

```
the         100
a           80
and         70
during      50
```

You should also *write* your results for *ALL* words to a file, formatted in tab-delimited format (again, use the `.format()` method).  Tab-delimited data look like:

```
word\tcount\n
the\t100\n
a\t80\n
and\t70\n
during\t50\n
```

## Task 2

Write a program that uses `argparse` to get the name of the tab-delimited file you created above from the user.  Read that file into your program, and determine count of all words that start with the letter "t" (or "T").  Using the `os.path` module, write these t-starting words to a new tab-delimited file that has the same name as the input file, but with "T-words" prepended to the input filename.  For example, if the input filename is "all-word-counts.txt", then your output file of t-words should be "T-words-all-word-counts.txt".  You can accomplish these filename manipulations using the `os.path` module. Your program should contain a `main` loop and an `ifmain` statement, and it should be formatted correctly.


## Task 3

Getting the t-words is all good, but your boss wants you to output a separate file for words that start with all letters of the alphabet.  So, modify your program from Task 2 to output 26 files, the names of which should begin with the appropriate letter of the alphabet (e.g. `A-words-all-word-counts.txt`, `B-words-all-word-counts.txt`, `C-words-all-word-counts.txt`) and the contents of which should be those words that start with the corresponding letter and the counts of those words in Darwin's text.  Format each file, as above, in tab-delimited format. Your program should contain a `main` loop and an `ifmain` statement, and it should be formatted correctly.

