# question 2.1
import re


def is_isogram(word):

    # set has no repeated characters, if length is different it is an isogram
    return len(word) > 0 and len(word) == len(set(word.lower()))


# question 2.2 

from question_2_1 import is_isogram

def test_is_isograms_with_isograms():
    # test with isograms to show it detects them
    assert is_isogram("isogram")
    assert is_isogram("chair")
    assert is_isogram("uncopyrightable")
    assert is_isogram("ambidextrously")


def test_function_with_non_isograms():
    # Test with non isograms to show it detects those cases

    assert is_isogram("ballet") is False
    assert is_isogram("gorgeous") is False


def test_function_with_empty_word():
    # test with empty word as it is not an isogram
    assert is_isogram("") is False


def test_function_with_capitalized_words():
    # test with capitalized letters, as the function lowers them
    assert is_isogram("TomMy") is False
    assert is_isogram("Total") is False
    assert is_isogram("Mama") is False
    assert is_isogram("Lula") is False

    #  capitalized but still an isogram
    assert is_isogram("Table")
    assert is_isogram("McFish")


if __name__ == "__main__":
    test_function_with_capitalized_words()
    test_function_with_empty_word()
    test_function_with_non_isograms()
    test_is_isograms_with_isograms()
