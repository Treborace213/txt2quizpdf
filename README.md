### Overview  
This program reads a `.txt` file containing quiz content and generates a PDF with formatted questions and answer space.

### How to Run  
```bash
$PATHTOMAIN/main.py $PATHTOINPUT/quiz.txt
```

The PDF will be saved in the current working directory with the same file name as the input file.
The title on the page will also have the same text as the input file name.
Any whitespace not in a block of text is ignored.

### Line Start Format  
- `!` → Subtitle  
- `?` → Question  
- `>` → Paragraph text  
- `~` → Page break  
- `#` → Comment (ignored line)

### Inline Text Commands  
- `#` → Comment (useful for writing answer notes)

#### Example:
```
# Sample quiz

! Welcome to the General Knowledge Quiz

> This quiz covers a range of general knowledge topics. Read each question carefully and answer in the space provided.

? What is the capital city of France?
? Who wrote the play "Romeo and Juliet"?
? What is the chemical symbol for water?

!Science and Maths Section

?What planet is known as the Red Planet?
?What is the square root of 64?
?Explain the process of photosynthesis in your own words.

~

!History and Geography

>Answer the following history and geography questions.

?In which year did the Titanic sink?
?Name one country that shares a border with Germany.
?What ancient civilization built the pyramids?
```