This is a Python module to help solve the [Wordle](https://www.powerlanguage.co.uk/wordle/) daily puzzle.

To use the module run a python interpreter in the same directory and `import wordle`

Requires `python 3.8.6`

Usage:

`import wordle`

#### Select a random 5 letter word
Useful if you can't think of where to start:

`wordle.select_random()`

#### Find possible words matching letters
`wordle.find(regex_str, Opt[included_letters_str], Opt[excluded_letters_str])`
Takes three positional arguments:
- A string that uses a regular expression search to match a string of known-position letters. Any unknown letters must be represented with a fullstop `.`

e.g. `wordle.find(".d.t.")`\
will return `['adits', 'adyta', 'edits']`

- A string of letters that are included, but whose position in the word is not known.

e.g. `wordle.find(".at..", "bs")`\
will return `['bates', 'baths', 'batts']`

- A string of letters that are not included in the word.

e.g `wordle.find(".e.ry", None, "bphotndiksva")`\
will return `['ferry', 'jerry', 'leery', 'merry', 'refry']`

#### Remove words that do not contain letters.
`wordle.remove(regex_string, word_list)`

Takes two arguements:  
- a regex string containing letters in the known exclusion position.
- a list of possible words

e.g if a = ['berry', 'deary', 'decry', 'derry', 'ferry', 'henry']

`wordle.remove("b.r..", a)`\
will return: ['deary', 'decry', 'henry']


#### Find words that contain every letter
This works like an anagram finder. It takes a string of 5 letters and\
returns a list of words that contain each letter of the string:

e.g. `wordle.anagram("astte")`\
will return `['etats', 'state', 'taste', 'tates', 'teats', 'testa']`


#### To run the tests:

`pytest tests.py`
