This is a Python module to help solve the [Wordle](https://www.powerlanguage.co.uk/wordle/) daily puzzle.

To use the module run python in the same directory and `import wordle`

Requires `python 3.8.6`

Usage:

`import wordle`

#### Select a random 5 letter word
Useful if you can't think of where to start:

`wordle.select()`

#### Find possible words that match known letters
Uses regexp search to match a string of known letters to possible words.\
Any unknown letters must be represented with a fullstop `.`

e.g. `wordle.find(".d.y.")`\
will return `['adits', 'adyta', 'edits']`
