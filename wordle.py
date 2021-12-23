from constants import FIVE_LETTER_WORDS as FIVE_LETTER_WORDS
import random
import re
from typing import List, Text


def select() -> Text:
    """Selects a random five letter word."""
    i = random.randint(0, len(FIVE_LETTER_WORDS))
    return FIVE_LETTER_WORDS[i]


def find(search_string: Text) -> List[str]:
    """Matches a string of exactly 5 characters using a regular expression
    matcher. The string should contain letters where known, and a fullstop
    where the letter is not known, e.g. ".D..Y".
    """
    if not len(search_string) == 5:
        raise Exception(
            f"""The search string must be exactly 5 """
            f"""characters in length. Your entry, '{search_string}' """
            f"""is {len(search_string)}."""
        )
    else:
        matches = []
        for word in FIVE_LETTER_WORDS:
            if re.search(search_string.lower(), word):
                matches.append(word)
        return matches
