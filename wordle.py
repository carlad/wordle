from constants import FIVE_LETTER_WORDS as FIVE_LETTER_WORDS
import random
import re
from typing import List, Text, Optional


def select() -> Text:
    """Selects a random five letter word."""
    i = random.randint(0, len(FIVE_LETTER_WORDS))
    return FIVE_LETTER_WORDS[i]


def find(search_string: Text, search_letters: Optional[Text] = None) -> List[str]:
    """Matches a string of exactly 5 characters using a regular expression
    matcher. The string should contain letters where known, and a fullstop
    where the letter is not known, e.g. ".D..Y".

    Searches for any letters in a string passed as an optional parameter.
    """
    if check_word_length(search_string):
        matches = []
        for word in FIVE_LETTER_WORDS:
            if re.search(search_string.lower(), word):
                matches.append(word)

        if search_letters:
            refined_matches = []
            letters = set(search_letters.lower())
            for word in matches:
                if set(word) >= letters:
                    refined_matches.append(word)
            matches = refined_matches

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


def anagram(search_string: Text) -> List[str]:
    if check_word_length(search_string):
        matches = []
        for word in FIVE_LETTER_WORDS:
            if sorted(search_string) == sorted(word):
                matches.append(word)
        return matches
