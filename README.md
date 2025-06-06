### Overview  
This program reads a `.txt` file containing quiz content and generates a PDF with formatted questions and answer space.

### How to Run  
```bash
$PATHTOMAIN/main.py $PATHTOINPUT/quiz.txt
```

The PDF will be saved in the current working directory with the same file name as the input file.

### Input Format  
- No prefix → A question  
- `!` → A paragraph of text
- `---` → A horizontal line
- '$[x]' → Vertical space x units tall

#### Example:
```
!Please answer the following questions carefully.
What does CPU stand for?
What is 2 + 2?
!Write your answers clearly in the space provided.
```