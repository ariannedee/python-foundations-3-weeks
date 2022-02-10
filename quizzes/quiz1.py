import csv
import time

DEBUG = False  # If True, print out answer script

# Console colours
NORMAL = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'

# Timing
AFTER_RESULT = 0.5
AFTER_NOTES = 3
AFTER_QUIZ = 0.5

# CSV columns
q = 'Question'
a = 'Answer'
n = 'Notes'
e = 'Execute'

questions = []
with open('questions.csv', 'rt') as file:
    reader = csv.DictReader(file)
    for line in reader:
        for col in [q, a, n]:
            line[col] = line[col].strip().replace('\\n', '\n').replace('\\t', '\t')
        questions.append(line)


total = len(questions)
num_correct = 0
for i, question in enumerate(questions):
    correct = None
    correct_answers = None
    incorrect_answers = None

    print(f'{BLUE}QUESTION {i + 1}{NORMAL}')
    ans = input(question[q]+ '\n' + ORANGE + 'Answer: ' + NORMAL)

    answer_script = question[a]
    if DEBUG:
        print(ORANGE + 'ANSWER SCRIPT:\n' + BLUE + answer_script + '\n' + NORMAL)
    exec(answer_script)

    if correct:
        print(GREEN + 'Correct!' + NORMAL)
        num_correct += 1
    elif correct is False:
        print(RED + 'Incorrect' + NORMAL)
    else:
        raise ValueError("Couldn't get correctness")
    notes_string = question[n]
    time.sleep(AFTER_RESULT)
    print(notes_string.format(**globals()))
    time.sleep(AFTER_NOTES)
    print('-' * 10)

time.sleep(AFTER_QUIZ)
print(f'You got {num_correct}/{total}')

num_wrong = total - num_correct

if num_wrong == 0:
    print("Aced it!")
elif num_wrong == 1:
    print("Well done!")
elif num_wrong < total // 2:
    print("Pretty good!")
else:
    print("You could use some more practice :)")
