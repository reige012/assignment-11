#!/usr/bin/env python
# encoding: utf-8

"""
My 1st program for Assignment 11

Created by Michael Henson on 07 March 2016.
Copyright 2016 Michael W Henson. All rights reserved.
"""
import argparse
import os


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

def mr_t(list):
    '''
    http://www.dreamincode.net/forums/topic/172876-extract-all-words-from-a-list-that-begin-with-x/
    '''
    mr_t_list = []
    with open(list, "r") as list:
        for i in list:
            if i[0] == 't':
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
    giveme_thet = mr_t(userinput.input)
    mr_t_forreal = os.path.join('T-words-'+userinput.input)
    output(giveme_thet, mr_t_forreal)


if __name__ == '__main__':
    main()
