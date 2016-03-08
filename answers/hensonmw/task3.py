#!/usr/bin/env python
# encoding: utf-8

"""
My 3rd program for Assignment 11

Created by Michael Henson on 07 March 2016.
Copyright 2016 Michael W Henson. All rights reserved.
"""
import argparse
import os
import string


def askingforfiles():
    parser = argparse.ArgumentParser(
        description="Asking User to Provide a input file and the output file name")
    parser.add_argument(
        "--input",
        required=True,
        help="Provide the output file from task1",
        type=str
    )
    return parser.parse_args()

def mr_t(letter, list):
    '''
    http://www.dreamincode.net/forums/topic/172876-extract-all-words-from-a-list-that-begin-with-x/
    http://stackoverflow.com/questions/16060899/alphabet-range-python
    '''
    mr_t_list = []
    with open(list, "r") as list:
        for i in list:
            if i[0] == letter:
                mr_t_list.append(i)
            else:
                pass
        return mr_t_list


def output(t_count, outputfile):
    with open(outputfile, 'w') as outputfile:
        for t_words in t_count:
            outputfile.write(t_words)


def main():
    userinput = askingforfiles()
    for letter in string.ascii_lowercase:
        #http://stackoverflow.com/questions/16060899/alphabet-range-python
        giveme_thet = mr_t(letter, userinput.input)
        mr_t_forreal = os.path.join(str.upper(letter)+"-words-"+userinput.input)
        output(giveme_thet, mr_t_forreal)


if __name__ == '__main__':
    main()
