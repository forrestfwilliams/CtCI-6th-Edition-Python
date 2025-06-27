import string
from collections import Counter


def is_palindrome_forrest(phrase):
    phrase = [c for c in phrase.lower() if c in string.ascii_lowercase]
    phrase_is_odd = len(phrase) % 2 == 1
    counter = Counter(phrase)
    seen_odd = False
    for key in counter:
        if counter[key] % 2 == 1:
            if not phrase_is_odd:
                return False
            elif seen_odd:
                return False
            seen_odd = True

    return True


print(is_palindrome_forrest('taco cat'))
