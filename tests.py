import pytest
import wordle

from constants import FIVE_LETTER_WORDS as FIVE_LETTER_WORDS
from typing import List, Text, Optional


def test_select_random():
    result = wordle.select_random

    assert FIVE_LETTER_WORDS.__contains__(result()) is True
    assert type(result()) == Text


def test_check_word_length():
    regex = "sk...."

    with pytest.raises(Exception) as e:
        wordle.check_word_length(regex)

    assert """
    The search string must be exactly 5 characters in length. 
    Your entry, 'sk....' is 6." in str(e.value).
    """


def test_find_known_positions():
    regex = ".adr."
    result = wordle.find(regex)

    assert result == ["cadre", "madre", "padre", "padri"]


def test_find_known_and_unknown_positions():
    regex = ".e..."
    unknown_positions = "dc"
    expected_result = [
        "cebid",
        "cedar",
        "ceded",
        "ceder",
        "cedes",
        "cedis",
        "cered",
        "decad",
        "decaf",
        "decal",
        "decan",
        "decay",
        "decko",
        "decks",
        "decor",
        "decos",
        "decoy",
        "decry",
        "deice",
        "demic",
        "dench",
        "deuce",
        "medic",
    ]

    result = wordle.find(regex, unknown_positions)

    assert result == expected_result


def test_find_with_excluded_letters():
    regex = ".e..."
    unknown_positions = "dc"
    excluded_letters = "muny"
    expected_result = [
        "cebid",
        "cedar",
        "ceded",
        "ceder",
        "cedes",
        "cedis",
        "cered",
        "decad",
        "decaf",
        "decal",
        "decko",
        "decks",
        "decor",
        "decos",
        "deice",
    ]

    result = wordle.find(regex, unknown_positions, excluded_letters)

    assert result == expected_result


def test_find_with_word_list():
    regex = "w..ty"
    unknown_positions = None
    excluded_letters = None
    word_list = FIVE_LETTER_WORDS
    expected_result = ["walty", "wanty", "warty", "whity", "wifty", "witty"]

    result = wordle.find(regex, unknown_positions, excluded_letters, word_list)

    assert result == expected_result


def test_remove_basic():
    regex = "cr..y"
    possible_words = ["mammy", "bammy", "pammy", "stress"]
    expected_result = ["stress"]

    result = wordle.remove(regex, possible_words)

    assert result == expected_result


def test_anagram():
    letters = "AmKer"
    expected_result = ["kerma", "maker"]

    result = wordle.anagram(letters)

    assert result == expected_result
