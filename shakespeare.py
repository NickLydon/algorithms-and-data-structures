from random import randint
shakespeare = "methinks it is like a weasel"


def rand_string():
    a_code = 97
    letters_in_alphabet = 26

    chars = [chr(c + a_code) for c in range(0, letters_in_alphabet)] + [' ']
    randints = [
        randint(0, letters_in_alphabet) for _ in range(0, len(shakespeare))
    ]
    randchars = [chars[rand] for rand in randints]
    return reduce(lambda a, b: a + b, randchars)


def score(sample):
    return sum([1 if sample[i] == c else 0 for i, c in enumerate(shakespeare)])


def run():
    iteration = 1
    best_score = 0
    best_guess = ""
    while True:
        sample = rand_string()
        this_score = score(sample)
        if this_score == len(shakespeare):
            print(sample)
            break
        elif this_score > best_score:
            best_guess = sample
            best_score = this_score
            print(best_score)

        if iteration % 1000000 == 0:
            print(best_guess)

        iteration += 1


run()