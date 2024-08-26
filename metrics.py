# Author: Yvonne Vogt
# Date: Spring Semester 2021
# Semester Project: Readability Rater

from typing import Union
import math
import spacy
import syllables

nlp = spacy.load("en_core_web_sm")


def calculate_average_word_len(word_list: list) -> float:
    """Calculate the average word length of a word list.

    :param: word_list: The input file as a word list is taken as input.
    :return: The average word length is returned.
    """
    average_word_len = sum(len(word) for word in word_list) / len(word_list)
    return round(average_word_len, 2)


def calculate_av_sent_len(word_list: list, sent_list: list) -> float:
    """Calculate the average sentence length based on a word and sentence list.

    :param: word_list: The input file as a word list is taken as input.
    :param: sent_list: The input file as a sentence list is taken as input.
    :return: The average sentence length is returned.
    """
    average_sent_len = len(word_list) / len(sent_list)
    return round(average_sent_len, 2)


def calculate_typetoken(word_list: list) -> float:
    """Calculate the type-token ratio of a list of words.

    :param: word_list: The input file as a word list is taken as input.
    :return: The type-token ratio is returned.
    """
    num_words = len(word_list)
    type_list = [word.lower() for word in word_list]
    ttr = len(set(type_list)) / num_words
    return round(ttr, 2)


def calculate_num_polysyl_words(word_list: list) -> int:
    """Calculate the number of polysyllabic words in a list of words.

    :param: word_list: The input file as a word list is taken as input.
    :return: The number of polysyllabic words is returned.
    """
    num_polysyl = 0
    for word in word_list:
        if syllables.estimate(word) >= 3:
            num_polysyl += 1
    return num_polysyl


def calculate_percent_polysyl_words(word_list: list) -> float:
    """Calculate the percent of polysyllabic words in list of words.

    :param: word_list: The input file as a list of words is taken as input.
    :return: The percent of polysyllabic words is returned.
    """
    percent_polysyl_words = 100 * (calculate_num_polysyl_words(word_list) / len(word_list))
    return round(percent_polysyl_words, 2)


def calculate_percent_monosyl_words(word_list: list) -> float:
    """Calculate percent of monosyllabic words in a word list.

    :param: word_list: The input file as a list of words is taken as input.
    :return: The percent of monosyllabic words is returned.
    """
    num_monosyl = 0
    for word in word_list:
        if syllables.estimate(word) == 1:
            num_monosyl += 1
    percent_monosyl_words = 100 * (num_monosyl / len(word_list))
    return round(percent_monosyl_words, 2)


def calculate_av_num_syl_word(word_list: list) -> float:
    """Calculate average number of syllables per word in a word list.

    :param: word_list: The input file as a list of words is taken as input.
    :return: The average number of syllables per word is returned.
    """
    num_syll_all = 0
    for word in word_list:
        num_syll_all += syllables.estimate(word)
    average_num_syllables_word = num_syll_all / len(word_list)
    return round(average_num_syllables_word, 2)


def get_num_polysyl_words_per_30_sents(sent_list: list) -> int:
    """

    Calculate number of polysyllabic words in a sample of 30 sentences of a list of sentences (min. 30).
    :param sent_list: Input file as list of sentences is taken as input from which a sample of 30 sentences is taken and
                      the polysyllabic words in said sample counted.
    :return: The number of polysyllabic words in the sample of 30 sentences. Returns -1 in case of input containing less
             than 30 sentences.
    """
    if len(sent_list) <= 30:
        return -1
    else:
        first_10_sents = sent_list[:10]
        last_10_sents = sent_list[-10:]
        middle_index = math.trunc(len(sent_list) / 2)
        middle_10_sents = sent_list[middle_index - 5:middle_index + 5]
        sample_30_sents = first_10_sents + middle_10_sents + last_10_sents
        # Convert the list of 30 sentences into a list of words.
        sample_as_string = " ".join(sample_30_sents)
        doc = nlp(sample_as_string)
        word_list_sample_30 = []
        for token in doc:
            if token.is_punct is False:
                word_list_sample_30.append(token.text)
        # Use this word list for function that counts polysyllabic words.
        num_polysyl_words_30_sents = calculate_num_polysyl_words(word_list_sample_30)
        return num_polysyl_words_30_sents


def calculate_smog(word_list: list, sent_list: list) -> Union[float, str]:
    """Calculate the SMOG Grade Level.

    :param word_list: The input file as a list of words is taken as input.
    :param sent_list: The input file as a list of sentences is taken as input.
    :return: If the input file is at least 600 words long, the SMOG Grade Level will be returned.
             If not, an error message will appear.
    """
    if len(word_list) >= 600:
        grade_level = 3 + (math.sqrt(get_num_polysyl_words_per_30_sents(sent_list)))
        return round(grade_level, 2)
    else:
        fail_output = "Your input file is too short. You need a minimum of 600 words and 30 sentences to achieve a " \
                      "reliable result."
        return fail_output


def calculate_num_polysyl_words_gf(word_list: list) -> int:
    """Count polysyllabic words that are not hyphenated, qualify as polysyllabic due to common suffixes or qualify as
    proper nouns.

    :param: word_list: The input file as a word list is taken as input.
    :return: The number of polysyllabic words that are not proper nouns and do not contain hyphens or polysyllabic
             due to common suffixes.
    """
    word_list_as_string = " ".join(word_list)
    doc = nlp(word_list_as_string)
    number_polysyl_words_gf = 0
    for token in doc:
        # Ignore three-syllabic words that are proper nouns, hyphenated, or end with e.g. -ed, -ing, -es, ly.
        if syllables.estimate(token.text) == 3:
            if token.tag_ != "NNP" and token.tag_ != "NNPS":
                if token.suffix_ != "ing" and token.suffix_[-2:] != "ed" and token.suffix_[-2:] != "es" \
                        and token.suffix_[-2:] != "ly":
                    if "-" not in token.text:
                        number_polysyl_words_gf += 1
        # Ignore hyphenated words and proper nouns in words with more than three syllables.
        if syllables.estimate(token.text) > 3:
            if token.tag_ != "NNP" and token.tag_ != "NNPS":
                if "-" not in token.text:
                    number_polysyl_words_gf += 1
    return number_polysyl_words_gf


def calculate_gunningfog(word_list: list, sent_list: list) -> Union[float, str]:
    """Calculate the Gunning Fog Grade Level.

    :param: word_list: The input file as a word list is taken as input.
    :param: sent_list: The input file as a sentence list is taken as input.
    :return: If the input file is at least 300 words long, the Gunning Fog Grade Level will be returned. If not, an
             error message will appear.
    """
    if len(word_list) >= 300:
        grade_level = 0.4 * (calculate_av_sent_len(word_list, sent_list) +
                             100 * (calculate_num_polysyl_words_gf(word_list) / len(word_list)))
        return round(grade_level, 2)
    else:
        fail_output = "Your input file is too short. You need a minimum of 300 words to achieve a reliable result."
        return fail_output


def calculate_fleschkincaid(word_list: list, sent_list: list) -> Union[float, str]:
    """Calculate the Flesch-Kincaid Grade Level.

    :param: word_list: The input file as a word list is taken as input.
    :param: sent_list: The input file as a sentence list is taken as input.
    :return: If the input file is at least 300 words long, the Flesch-Kincaid Grade Level will be returned. If not, an
             error message will appear.
    """
    if len(word_list) >= 300:
        grade_level = (0.39 * calculate_av_sent_len(word_list, sent_list)) + \
                      (11.8 * calculate_av_num_syl_word(word_list)) - 15.594
        return round(grade_level, 2)
    else:
        fail_output = "Your input file is too short. You need a minimum of 300 words to achieve a reliable result."
        return fail_output
