from constants import FIVE_LETTER_WORDS as FIVE_LETTER_WORDS
import random
import re
from typing import List, Text, Optional


def select_random() -> Text:
    """Selects a random five letter word."""
    i = random.randint(0, len(FIVE_LETTER_WORDS))
    return FIVE_LETTER_WORDS[i]


def find(
    regex_string: Text,
    included_letters: Optional[Text] = None,
    excluded_letters: Optional[Text] = None,
    word_list: Optional[List] = FIVE_LETTER_WORDS,
) -> List[str]:
    """Matches a string of exactly 5 characters using a regular expression
    matcher. The string should contain letters where known, and a fullstop
    where the letter is not known, e.g. ".D..Y".

    Matches words that contain any letters in a string passed as an optional
    parameter.
    Excludes words that contain any letters in a string passed as an optional
    parameter.
    """
    if check_word_length(regex_string):
        matches = []
        for word in word_list:
            if re.search(regex_string.lower(), word):
                matches.append(word)

        if included_letters:
            refined_matches = []
            letters = set(included_letters.lower())
            for word in matches:
                if set(word) >= letters:
                    refined_matches.append(word)
            matches = refined_matches

        if excluded_letters:
            refined_matches = []
            letters = set(excluded_letters.lower())
            for word in matches:
                if not any(i in word for i in letters):
                    refined_matches.append(word)
            matches = refined_matches

        return matches


def remove(regex_string: Text, possible_words: List) -> List:
    if check_word_length(regex_string):
        matches = []
        for word in possible_words:
            for i, v in enumerate(regex_string):
                if not v == ".":
                    if word[i] == v:
                        matches.append(word)
            matches = list(set(matches))
        for match in matches:
            possible_words.remove(match)

        return possible_words


def anagram(letters: Text) -> List[str]:
    if check_word_length(letters):
        matches = []
        for word in FIVE_LETTER_WORDS:
            if sorted(letters.lower()) == sorted(word):
                matches.append(word)
        return matches


def check_word_length(word: Text) -> None:
    if not len(word) == 5:
        raise Exception(
            f"""The search string must be exactly 5 """
            f"""characters in length. Your entry, '{word}' """
            f"""is {len(word)}."""
        )
    else:
        return True
