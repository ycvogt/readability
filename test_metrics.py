# Author: Yvonne Vogt
# Date: Spring Semester 2021
# Semester Project: Readability Rater

import pytest

from main import *


@pytest.fixture()
def read_test_file():
    """Return a test text without line breaks for testing."""
    with open("test_file.txt", 'r', encoding='utf-8') as f:
        text = f.read()
        text = re.sub('\n', '', text)
    return text


@pytest.fixture()
def get_test_word_list(read_test_file):
    """Return test file as a word list for testing."""
    test_word_list = get_words(read_test_file)
    return test_word_list


@pytest.fixture()
def get_test_sent_list(read_test_file):
    """Return test file as a sentence list for testing."""
    test_sent_list = get_sents(read_test_file)
    return test_sent_list


def test_get_sentences(read_test_file):
    """Test sentence segmentation."""
    assert len(get_sents(read_test_file)) == 61
    assert get_sents("This is a test. To test this, I write a text.") == ["This is a test.",
                                                                          "To test this, I write a text."]


def test_get_words(read_test_file):
    """Test tokenization into list of words."""
    assert len(get_words(read_test_file)) == 764
    assert get_words("This is a test. To test this, I 'write' a text.") == ["This", "is", "a", "test", "To", "test",
                                                                            "this", "I", 'write', "a", "text"]


def test_calculate_average_word_len(get_test_word_list):
    """Test calculation of average word length."""
    assert calculate_average_word_len(get_test_word_list) == 4.62
    assert calculate_average_word_len(["To", "test", "this", "I", "write", "this", "text"]) == 3.43


def test_calculate_av_sent_len(get_test_word_list, get_test_sent_list):
    """Test calculation of average sentence length."""
    assert calculate_av_sent_len(get_test_word_list, get_test_sent_list) == 12.52
    assert calculate_av_sent_len(["This", "is", "great", "I", "am", "testing", "this"],
                                 ["This is great.", "I am testing this."]) == 3.5


def test_calculate_typetoken(get_test_word_list):
    """Test calculation of type-token ratio."""
    assert calculate_typetoken(get_test_word_list) == 0.46
    assert calculate_typetoken(["This", "is", "a", "test", "The", "dog", "barks",
                                "This", "tests", "the", "type-token", "ratio"]) == 0.83


def test_calculate_num_polysyl_words(get_test_word_list):
    """Test calculation of number of polysyllabic words."""
    assert calculate_num_polysyl_words(get_test_word_list) == 94
    assert calculate_num_polysyl_words(["unequivocally", "I", "meticulously", "communicate", "trying"]) == 3


def test_calculate_percent_polysyl_words(get_test_word_list):
    """Test calculation of percent of polysyllabic words."""
    assert calculate_percent_polysyl_words(get_test_word_list) == 12.30
    assert calculate_percent_polysyl_words(["meticulously", "be", "writing", "critical", "lucky"]) == 40.0


def test_calculate_percent_monosyl_words(get_test_word_list):
    """Test calculation of percent of monosyllabic words."""
    assert calculate_percent_monosyl_words(get_test_word_list) == 59.82
    assert calculate_percent_monosyl_words(["meticulously", "be", "writing", "critical", "lucky"]) == 20.0


def test_calculate_av_num_syl_word(get_test_word_list):
    """Test calculation of average number of words."""
    assert calculate_av_num_syl_word(get_test_word_list) == 1.56
    assert calculate_av_num_syl_word(["meticulously", "be", "writing", "critical", "lucky"]) == 2.6


def test_get_num_polysyl_words_per_30_sents(read_test_file):
    """Test calculation of number of polysyllabic words per 30 sentences."""
    assert get_num_polysyl_words_per_30_sents(get_sents(read_test_file)) == 52


def test_calculate_num_polysyl_words_gf(get_test_word_list):
    """Test calculation of number of polysyllabic words that qualify for the Gunning Fog metric."""
    assert calculate_num_polysyl_words_gf(get_test_word_list) == 43
    assert calculate_num_polysyl_words_gf(["high-tech", "Jane", "Bath", "educated", "commonly", "died", "writing",
                                           "polysyllabic", "absolute"]) == 3


def test_calculate_smog(get_test_word_list, get_test_sent_list):
    """Test calculation of SMOG metric."""
    assert calculate_smog(get_test_word_list, get_test_sent_list) == 10.21


def test_calculate_gunningfog(get_test_word_list, get_test_sent_list):
    """Test calculation of Gunning Fog metric."""
    assert calculate_gunningfog(get_test_word_list, get_test_sent_list) == 7.26


def test_calculate_fleschkincaid(get_test_word_list, get_test_sent_list):
    """Test calculation of Flesch-Kincaid metric."""
    assert calculate_fleschkincaid(get_test_word_list, get_test_sent_list) == 7.7


# Source for test_file.txt: <https://simple.wikipedia.org/wiki/Jane_Austen> (last accessed June 4, 2021).
