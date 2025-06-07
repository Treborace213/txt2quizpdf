# Overview  
This program reads a `.txt` file containing quiz content and generates a PDF with formatted questions and answer space.

# How to Run  
```bash
$PATHTOMAIN/main.py $PATHTOINPUT/quiz.txt
```

The PDF will be saved in the current working directory with the same file name as the input file.

# Markup Format Specification
Each line in the file follows one of the defined rules below. Blank lines are ignored.

## Questions

- `(` Start of an unnumbered question list.

- `[` Start of a numbered question list.

- `?x | y` A question with text `x` and answer `y`.

- `_x | y` A question with text `x` and answer `y`, followed by answer space.

- `)` End of an unnumbered question list.

- `]` End of a numbered question list.

## Other Text

- `!` followed by text. Defines a title.

- `@` followed by text. Defines a single-line paragraph.

## Layout Controls

- `-` Horizontal line.

- `~n` Vertical space of size `n`.

- `+` A page break.

## Comments

- `#` followed by text. A comment (ignored in output).