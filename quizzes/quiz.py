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
w = 'Week'
q = 'Question'
a = 'Answer'
e = 'Explanation'
r = 'Review'


def get_questions(week=None):
    questions = []
    with open('questions.csv', 'rt') as file:
        reader = csv.DictReader(file)
        for line in reader:
            if week and int(line[w]) != week:
                continue
            for col in [q, a, e, r]:
                line[col] = line[col].strip().replace('\\n', '\n').replace('\\t', '\t').replace('&quot;', '"').replace('&apos;', "'")
            questions.append(line)
    return questions


class Question:
    def __init__(self, number, total, as_dict):
        self.num = number
        self.total = total
        self.question = as_dict[q]
        self.answer_script = as_dict[a]
        self.review_links = as_dict[r]
        self.explanation = as_dict[e]

        self.user_answer = None  # call self.get_guess() to set this
        self.correct = None  # call self.determine_correctness() to set this

    def print_question(self):
        print(f'{PURPLE}QUESTION {self.num} of {self.total}{NORMAL}')
        print(self.question)

    def get_guess(self):
        while True:
            answer = input(ORANGE + 'Answer: ' + NORMAL)
            if answer:
                self.user_answer = answer
                break
        if DEBUG:
            print(ORANGE + 'ANSWER:\n' + BLUE + repr(answer) + '\n' + NORMAL)

    def determine_correctness(self):
        if DEBUG:
            print(ORANGE + 'ANSWER SCRIPT:\n' + BLUE + self.answer_script + '\n' + NORMAL)

        locals_ = {'ans': self.user_answer, 'correct': None}
        exec(self.answer_script, {}, locals_)
        self.correct = locals_['correct']

    @staticmethod
    def should_show_review():
        while True:
            see_review = input(ORANGE + "\nSee links for the relevant lessons? (y/N) " + NORMAL)
            if see_review.lower() == 'y':
                return True
            if see_review.lower() == 'n':
                review = False
                return False

    def print_review(self):
        print(self.review_links)
        print()
        if self.num < self.total:
            input("Press ENTER for the next question")
        else:
            input("Press ENTER to see your result")


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.reviews = {}
        self.total = len(questions)
        self.num_correct = 0

    def handle_correctness(self, question: Question):
        if question.correct:
            print(GREEN + '- Correct -' + NORMAL)
            self.num_correct += 1
        elif question.correct is False:
            self.reviews[question.num] = question.review_links
            print(RED + '- Incorrect -' + NORMAL)
        else:
            raise ValueError("Couldn't get correctness")
        print()

    def print_quiz_result(self):
        print(f'You got {self.num_correct}/{self.total}')

        num_wrong = self.total - self.num_correct

        if num_wrong == 0:
            print("Aced it!")
        elif num_wrong == 1:
            print("Well done!")
        elif num_wrong < self.total // 2:
            print("Pretty good!")
        else:
            print("You could use some more practice :)")

    @staticmethod
    def should_show_review():
        while True:
            see_review = input(
                ORANGE + "Would you like to see the review links for the questions you got wrong? (y/N) " + NORMAL)
            if see_review.lower() == 'y':
                return True
            if see_review.lower() == 'n':
                return False

    def print_review_links(self):
        for q_num, review in self.reviews.items():
            print(PURPLE + f'--- Question {q_num} ---' + NORMAL)
            print(review)
            print()

    def run_quiz(self):
        for q_num, question_dict in enumerate(self.questions, start=1):
            question = Question(q_num, self.total, question_dict)

            question.print_question()
            question.get_guess()
            question.determine_correctness()
            self.handle_correctness(question)
            time.sleep(0.7)
            print(question.explanation)
            show_review = question.should_show_review()
            if show_review:
                question.print_review()

            print('-' * 10)

        self.print_quiz_result()
        show_review = self.should_show_review()

        if show_review:
            self.print_review_links()


if __name__ == '__main__':
    week = 2  # Specify which week's quiz to run
    questions = get_questions(week)
    Quiz(questions).run_quiz()
