from pytest import mark

from problem_4_wordle import wordle_result


@mark.parametrize(('word', 'guess', 'result'), [
    ('a', 'a', '💚'),
    ('a', 'i', '🖤'),
    ('an', 'in', '🖤💚'),
    ('an', 'no', '💛🖤'),
    ('ode', 'doe', '💛💛💚'),
])
def test_wordle_result_1(word, guess, result):
    assert wordle_result(word, guess) == result


@mark.parametrize(('word', 'guess', 'result'), [
    ('ode', 'dad', '💛🖤🖤'),
    ('close', 'chess', '💚🖤💛💚🖤'),
])
def test_wordle_result_2(word, guess, result):
    assert wordle_result(word, guess) == result


@mark.parametrize(('word', 'guess', 'result'), [
    ('and', 'dad', '🖤💛💚'),
    ('guess', 'sassy', '💛🖤🖤💚🖤'),
])
def test_wordle_result_3(word, guess, result):
    assert wordle_result(word, guess) == result
