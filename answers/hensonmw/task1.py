#!/usr/bin/env python
# encoding: utf-8

"""
My 1st program for Assignment 11

Created by Michael Henson on 07 March 2016.
Copyright 2016 Michael W Henson. All rights reserved.
"""

from collections import Counter
import argparse
import re


def askingforfiles():
    parser = argparse.ArgumentParser(
        description="Asking User to Provide a input file and the output file name")
    parser.add_argument(
        "--input",
        required=True,
        help="Provide name of input file",
        type=str
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Provide name of output file",
        type=str
    )
    return parser.parse_args()


def cleanup_count(string):
    with open(string, "r") as string:
        string = string.read()
        list = re.split('\W+', string)
        #https://docs.python.org/2/library/re.html
        '''
        this took me forever to figure out and what to use
        since I previous got this wrong. this seems simple compared
        to previous attempted to break apart using string
        '''
        '''
        http://stackoverflow.com/questions/10134372/get-a-list-of-names-which-start-with-certain-letters
        First answer helped tell me how to put together a list comprehension.
        '''
        my_dict = [str.lower(word) for word in list]
    return my_dict


def final_count(text):
    counting = Counter(text).most_common(20)
    return counting


def output(clean_count, outputfile):
    '''Creates an output file (names with user input) of every word and its
    count from the original input file.'''
    with open(outputfile, 'w') as outputfile:
        clean_count = Counter(clean_count)
        for word, count in clean_count.items():
            outputfile.write('{0}\t{1}\n'.format(word, count))


def main():
    userinput = askingforfiles()
    clean_count = cleanup_count(userinput.input)
    counts = final_count(clean_count)
    print("And the top 20 is....")
    for item in counts:
        print("{0:<12}  {1:<12}".format(item[0], item[1]))
    output(clean_count, userinput.output)


if __name__ == '__main__':
    main()
