This is a Python module to help solve the [Wordle](https://www.powerlanguage.co.uk/wordle/) daily puzzle.

To use the module run a python interpreter in the same directory and `import wordle`

Requires `python 3.8.6`

Usage:

`import wordle`

#### Select a random 5 letter word
Useful if you can't think of where to start:

`wordle.select()`

#### Find possible words matching letters of known and unknown positions
Uses regexp search to match a string of known-position letters to possible\ words. Any unknown letters must be represented with a fullstop `.`

e.g. `wordle.find(".d.t.")`\
will return `['adits', 'adyta', 'edits']`

The `find` method also takes an optional additional string argument of\
unknown-position letters.

e.g. `wordle.find(".at..", "bs")`\
will return `['bates', 'baths', 'batts']`


#### Find words that contain every letter
This works like an anagram finder. It takes a string of 5 letters and\
returns a list of words that contain each letter of the string:

e.g. `wordle.anagram("astte")`\
will return `['etats', 'state', 'taste', 'tates', 'teats', 'testa']`
