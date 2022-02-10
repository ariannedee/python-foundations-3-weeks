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

# CSV columns
q = 'Question'
a = 'Answer'
e = 'Explanation'
r = 'Review'

questions = []
with open('questions.csv', 'rt') as file:
    reader = csv.DictReader(file)
    for line in reader:
        for col in [q, a, e, r]:
            line[col] = line[col].strip().replace('\\n', '\n').replace('\\t', '\t').replace('&quot;', '"').replace('&apos;', "'")
        questions.append(line)

reviews = {}
total = len(questions)
num_correct = 0
for q_num, question in enumerate(questions, start=1):
    correct = None
    correct_answers = None
    incorrect_answers = None

    print(f'{PURPLE}QUESTION {q_num} of {total}{NORMAL}')
    print(question[q])
    while True:
        ans = input(ORANGE + 'Answer: ' + NORMAL)
        if ans:
            break

    if DEBUG:
        print(ORANGE + 'ANSWER:\n' + BLUE + repr(ans) + '\n' + NORMAL)
    answer_script = question[a]
    if DEBUG:
        print(ORANGE + 'ANSWER SCRIPT:\n' + BLUE + answer_script + '\n' + NORMAL)
    exec(answer_script)
    if correct:
        print(GREEN + '- Correct -' + NORMAL)
        num_correct += 1
    elif correct is False:
        reviews[q_num] = question[r]
        print(RED + '- Incorrect -' + NORMAL)
    else:
        raise ValueError("Couldn't get correctness")
    print()
    notes_string = question[e]
    time.sleep(0.7)
    print(notes_string.format(**globals()))
    while True:
        see_review = input(ORANGE + "\nSee links for the relevant lessons? (y/N) " + NORMAL)
        if see_review.lower() == 'y':
            review = True
            break
        if see_review.lower() == 'n':
            review = False
            break
    if review:
        print(question[r])
        print()
        if q_num < total:
            input("Press ENTER for the next question")
        else:
            input("Press ENTER to see your result")
    print('-' * 10)

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

while True:
    see_review = input(ORANGE + "Would you like to see the review links for the questions you got wrong? (y/N) " + NORMAL)
    if see_review.lower() == 'y':
        review = True
        break
    if see_review.lower() == 'n':
        review = False
        break
if review:
    for q_num, review in reviews.items():
        print(PURPLE + f'--- Question {q_num} ---' + NORMAL)
        print(review)
        print()