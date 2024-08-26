# Author: Yvonne Vogt
# Date: Spring Semester 2021
# Semester Project: Readability Rater

import ntpath
import os
import re
from argparse import ArgumentParser

from metrics import *


def get_argument_parser():
    """Define console argument parser."""
    parser = ArgumentParser(description="This program measures and classifies the readability of a text.")
    parser.add_argument('file', type=str, help="File/Folder of files to be evaluated.")
    parser.add_argument('-sm', '--smog', action='store_true',
                        help="Measure readability of input with SMOG INDEX.")
    parser.add_argument('-gf', '--gunningfog', action='store_true',
                        help="Measure readability of input with GUNNING FOG INDEX.")
    parser.add_argument('-fk', '--fleschkincaid', action='store_true',
                        help="Measure readability of input with FLESCH-KINCAID GRADE LEVEL SCORE.")
    parser.add_argument('-a', '--all', action='store_true', help="Measure readability of input with all three metrics.")
    parser.add_argument('-st', '--stats', action='store_true',
                        help="Calculates: type-token ratio, average sentence and word length, "
                             "average number of syllables per word, percentages of monosyllabic and "
                             "polysyllabic words per input file.")
    return parser


def get_words(text: str) -> list:
    """Split input text file into a list of words.

    :param text: The input text file to be tokenized into a list of words.
    :return: Input text file as a list of words.
    """
    word_list = []
    doc = nlp(text)
    for token in doc:
        # Ignore punctuation as token.
        if token.is_punct is False:
            word_list.append(token.text)
    return word_list


def get_sents(text: str) -> list:
    """Segment input text file into list of sentences.

    :param text: The input text file to be segmented into sentences.
    :return: The input text file segmented into a list of sentences.
    """
    sent_list = []
    doc = nlp(text)
    for sent in doc.sents:
        sent_list.append(sent.text)
    return sent_list


def main():
    parser = get_argument_parser()
    # Parse console arguments.
    args = parser.parse_args()

    # Read files or files in a folder and save them in a list.
    given_path = os.path.abspath(args.file)
    if os.path.isdir(given_path):
        path = given_path
        file_list = os.listdir(path)
    else:
        path = ntpath.split(given_path)[0]
        file_list = [args.file]

    for f in file_list:
        # Check if the file is a text file.
        if f.endswith(".txt"):
            with open(path+'\\'+f, 'r', encoding='utf-8') as f_open:
                text = f_open.read()
                text = re.sub('\n', '', text)

                # Make the lists of words and sentences of file(s) available for the imported functions.
                word_list = get_words(text)
                sent_list = get_sents(text)

                # Print output of the flags per file.
                print("-------------------------------------------------")
                print("File: "+f)
                if args.stats:
                    print("Type-Token Ratio: "+str(calculate_typetoken(word_list)))
                    print("Average word length: "+str(calculate_average_word_len(word_list)))
                    print("Average sentence length: "+str(calculate_av_sent_len(word_list, sent_list)))
                    print("Average number of syllables per word: "+str(calculate_av_num_syl_word(word_list)))
                    print("Percent of monosyllabic words: "+str(calculate_percent_monosyl_words(word_list)))
                    print("Percent of polysyllabic words: "+str(calculate_percent_polysyl_words(word_list)))
                if args.smog:
                    print("SMOG: "+str(calculate_smog(word_list, sent_list)))
                if args.gunningfog:
                    print("Gunning Fog: "+str(calculate_gunningfog(word_list, sent_list)))
                if args.fleschkincaid:
                    print("Flesch-Kincaid: "+str(calculate_fleschkincaid(word_list, sent_list)))
                if args.all:
                    print("SMOG: "+str(calculate_smog(word_list, sent_list)))
                    print("Gunning Fog: "+str(calculate_gunningfog(word_list, sent_list)))
                    print("Flesch-Kincaid: "+str(calculate_fleschkincaid(word_list, sent_list)))
                print("-------------------------------------------------")
        else:
            print("Your file "+f+" is not a text file. Please use text files only.")


if __name__ == '__main__':
    main()
